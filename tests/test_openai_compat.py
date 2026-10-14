"""The real HTTP client, exercised against a local OpenAI-compatible server backed by the fake model."""

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from ltg import prompts
from ltg.config import load_config
from ltg.fake import FakeModel
from ltg.models import CallLog, ModelError, OpenAICompatClient
from ltg.orchestrator import Pipeline

ROLE_BY_SYSTEM = {
    prompts.LEDGER_WRITER: "ledger_writer",
    prompts.DRAFTER: "drafter",
    prompts.FACT_EXTRACTOR: "fact_extractor",
    prompts.ISSUE_VERIFIER: "issue_verifier",
    prompts.INSTRUCTION_WRITER: "instruction_writer",
    prompts.RUBRIC_WRITER: "rubric_writer",
    prompts.ANSWER_WRITER: "answer_writer",
    prompts.JUDGE: "judge",
    prompts.SOLVER: "solver",
}


@pytest.fixture
def server():
    fake = FakeModel(seed=7)
    state = {"fail_next": 0, "auth": [], "models": []}

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            state["auth"].append(self.headers.get("Authorization"))
            state["models"].append(body["model"])
            if state["fail_next"]:
                state["fail_next"] -= 1
                self.send_response(503)
                self.end_headers()
                self.wfile.write(b"busy")
                return
            system, user = body["messages"][0]["content"], body["messages"][1]["content"]
            content = fake.complete(ROLE_BY_SYSTEM[system], system, user)
            resp = {"choices": [{"message": {"content": "```json\n" + content + "\n```"}}], "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
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
    from ltg.models import render_input

    out = client.complete("solver", prompts.SOLVER, render_input({"instruction": "x", "documents": []}))
    assert "answer" in out
    assert [r.ok for r in log.records] == [False, True]


def test_client_gives_up_after_retries(server, monkeypatch):
    url, state = server
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    monkeypatch.setattr("ltg.models.time.sleep", lambda s: None)
    state["fail_next"] = 5
    with pytest.raises(ModelError):
        OpenAICompatClient(url, "m", max_retries=1).complete("solver", prompts.SOLVER, "x")
