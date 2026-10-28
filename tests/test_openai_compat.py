"""The real HTTP client, exercised against a local OpenAI-compatible server backed by the fake model."""

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from ltg import prompts
from ltg.config import load_config
from ltg.fake import FakeModel
from ltg.models import CallLog, ModelError, OpenAICompatClient, call_text, render_input
from ltg.orchestrator import Pipeline

ROLE_BY_SYSTEM = {
    prompts.LEDGER_WRITER: "ledger_writer",
    prompts.DRAFTER: "drafter",
    prompts.FACT_EXTRACTOR: "fact_extractor",
    prompts.FACT_MATCHER: "fact_matcher",
    prompts.ISSUE_VERIFIER: "issue_verifier",
    prompts.INSTRUCTION_WRITER: "instruction_writer",
    prompts.RUBRIC_WRITER: "rubric_writer",
    prompts.ANSWER_WRITER: "answer_writer",
    prompts.JUDGE: "judge",
    prompts.SOLVER_STEP: "solver",
    prompts.SOLVER_WRITE: "solver",
}


@pytest.fixture
def server():
    fake = FakeModel(seed=7)
    state = {"fail_next": 0, "drop_next": 0, "rate_next": 0, "auth": [], "models": [], "finish_reason": "stop", "think": ""}

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            state["auth"].append(self.headers.get("Authorization"))
            state["models"].append(body["model"])
            state.setdefault("bodies", []).append(body)
            if state["drop_next"]:  # hang up without answering, like a server going down mid-request
                state["drop_next"] -= 1
                self.close_connection = True
                return
            if state["rate_next"]:
                state["rate_next"] -= 1
                self.send_response(429)
                self.send_header("x-ratelimit-reset", "7")
                self.end_headers()
                return
            if state["fail_next"]:
                state["fail_next"] -= 1
                self.send_response(503)
                self.end_headers()
                self.wfile.write(b"busy")
                return
            system, user = body["messages"][0]["content"], body["messages"][1]["content"]
            content = fake.complete(ROLE_BY_SYSTEM[system], system, user)
            message = {"content": state["think"] + "```json\n" + content + "\n```"}
            resp = {"choices": [{"message": message, "finish_reason": state["finish_reason"]}], "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
            data = json.dumps(resp).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    yield f"http://127.0.0.1:{httpd.server_port}/v1", state
    httpd.shutdown()


def test_pipeline_runs_through_http_client(server, tmp_path, monkeypatch):
    url, state = server
    monkeypatch.setenv("TEST_KEY", "secret")
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    cfg = load_config(None, {
        "run": {"out_dir": str(tmp_path), "n_matters": 2, "seed": 7},
        "backend": {"kind": "openai_compat", "base_url": url, "api_key_env": "TEST_KEY", "default_model": "small", "models": {"solver": "big"}},
    })
    rep = Pipeline(cfg).run()
    assert rep["errors"] == 0 and rep["candidates"] == 2
    assert set(state["auth"]) == {"Bearer secret"}
    assert {"small", "big"} <= set(state["models"])
    assert rep["model_calls"]["solver"]["input_tokens"] > 0


def test_client_retries_server_errors(server, monkeypatch):
    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    state["fail_next"] = 1
    log = CallLog()
    client = OpenAICompatClient(url, "m", log=log, max_retries=2)
    client_sleep = []
    monkeypatch.setattr("ltg.models.time.sleep", lambda s: client_sleep.append(s))
    out = client.complete("solver", prompts.SOLVER_WRITE, render_input({"instruction": "x", "files": [], "steps": []}))
    assert "cannot assess" in out
    assert [r.ok for r in log.records] == [False, True]


def test_client_gives_up_after_retries(server, monkeypatch):
    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    monkeypatch.setattr("ltg.models.time.sleep", lambda s: None)
    state["fail_next"] = 5
    with pytest.raises(ModelError):
        OpenAICompatClient(url, "m", max_retries=1).complete("solver", prompts.SOLVER_WRITE, "x")


def test_client_rejects_truncated_output(server, monkeypatch):
    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    state["finish_reason"] = "length"
    with pytest.raises(ModelError, match="truncated"):
        OpenAICompatClient(url, "m").complete("solver", prompts.SOLVER_WRITE, render_input({"instruction": "x", "files": [], "steps": []}))


def test_client_strips_reasoning_blocks(server, monkeypatch):
    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    state["think"] = "<think>\nThe answer is {not json}.\n</think>\n"
    out = call_text(OpenAICompatClient(url, "m"), "solver", prompts.SOLVER_WRITE, render_input({"instruction": "x", "files": [], "steps": []}))
    assert out.startswith("I cannot assess")


def test_one_role_can_use_its_own_backend(server, tmp_path, monkeypatch):
    """Opus-style generation on one backend, the solver on an OpenAI-compatible endpoint (vLLM, NRP)."""
    url, state = server
    monkeypatch.setenv("SOLVER_KEY", "solver-secret")
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    cfg = load_config(None, {
        "run": {"out_dir": str(tmp_path), "n_matters": 1, "seed": 7},
        "backend": {"kind": "fake", "roles": {"solver": {"kind": "openai_compat", "base_url": url,
                                                         "api_key_env": "SOLVER_KEY", "model": "open-model"}}},
    })
    rep = Pipeline(cfg).run()
    assert rep["errors"] == 0
    assert state["models"] and set(state["models"]) == {"open-model"}  # only solver calls reached the endpoint
    assert len(state["models"]) == rep["model_calls"]["solver"]["calls"]
    assert set(state["auth"]) == {"Bearer solver-secret"}


def test_role_extra_body_reaches_the_request(server, monkeypatch):
    """Per-role server fields (NRP's reasoning_effort) are sent with every call from that role only."""
    from ltg.config import build_client

    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    cfg = load_config(None, {"backend": {"kind": "openai_compat", "base_url": url, "default_model": "gen", "roles": {
        "solver": {"model": "open-model", "extra_body": {"reasoning_effort": "low"}}}}})
    client = build_client(cfg, CallLog())
    empty = render_input({"instruction": "x", "files": [], "steps": []})
    client.complete("solver", prompts.SOLVER_WRITE, empty)
    client.complete("judge", prompts.JUDGE, render_input({"response": "x", "criteria": []}))
    solver_body, judge_body = state["bodies"]
    assert solver_body["model"] == "open-model" and solver_body["reasoning_effort"] == "low"
    assert solver_body["max_tokens"] == cfg.backend.max_tokens  # the standard fields are still there
    assert judge_body["model"] == "gen" and "reasoning_effort" not in judge_body


def test_role_backend_rejects_unknown_keys():
    from ltg.config import build_client

    cfg = load_config(None, {"backend": {"kind": "fake", "roles": {"solver": {"kind": "fake", "modle": "x"}}}})
    with pytest.raises(ValueError, match="unknown keys"):
        build_client(cfg, CallLog())


def test_client_survives_dropped_connections_and_honours_rate_limits(server, monkeypatch):
    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    slept = []
    monkeypatch.setattr("ltg.models.time.sleep", lambda s: slept.append(s))
    state["drop_next"], state["rate_next"] = 1, 1
    log = CallLog()
    out = OpenAICompatClient(url, "m", log=log, max_retries=3).complete(
        "solver", prompts.SOLVER_WRITE, render_input({"instruction": "x", "files": [], "steps": []}))
    assert "cannot assess" in out
    assert [r.ok for r in log.records] == [False, False, True]
    assert slept[1] == 7  # waited as long as the 429 asked
