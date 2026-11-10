"""`scripts/build_handoff.py`: the task folder for the lab's post-training agent, and its grader on gold and flawed memos."""

import json
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from ltg.config import load_config
from ltg.fake import FakeModel
from ltg.orchestrator import Pipeline

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_handoff import main as build_main  # noqa: E402


class _Judge(BaseHTTPRequestHandler):
    """An OpenAI-compatible endpoint that answers as the fake model's judge."""

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        system, user = (m["content"] for m in body["messages"])
        reply = json.dumps({"choices": [{"message": {"content": FakeModel().complete("judge", system, user)}, "finish_reason": "stop"}]})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(reply.encode())

    def log_message(self, *a):
        pass


def test_handoff_folder_and_grader(tmp_path):
    # ratios chosen so the 6 fake matters give both train and dev tasks
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path / "run"), "n_matters": 6, "seed": 7},
                             "splits": {"ratios": {"train": 0.5, "dev": 0.5, "test": 0.0}}})
    Pipeline(cfg).run()
    out = tmp_path / "handoff" / "v0"
    assert build_main(["--out", str(out), "--runs", str(tmp_path / "run"), "--base-model", "Org/Base-1B"]) == 0

    files = sorted(str(p.relative_to(out)) for p in out.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    assert [f for f in files if not f.startswith("grade/ltg/")] == ["README.md", "data/train.jsonl", "grade/dev.jsonl", "grade/evaluate.py"]
    assert {"grade/ltg/stages.py", "grade/ltg/models.py", "grade/ltg/prompts.py"} <= set(files)
    readme = (out / "README.md").read_text()
    assert "Org/Base-1B" in readme and "harveyai/harvey-labs" in readme and "{" not in readme

    train = [json.loads(l) for l in (out / "data/train.jsonl").read_text().splitlines()]
    grade = [json.loads(l) for l in (out / "grade/dev.jsonl").read_text().splitlines()]
    assert train and grade
    assert all([m["role"] for m in r["messages"]] == ["system", "user", "assistant"] and r["eval"]["split"] == "train" for r in train)
    assert all("hints" not in c for r in train for c in r["eval"]["rubric"])
    assert all([m["role"] for m in r["messages"]] == ["system", "user"] for r in grade)
    assert all(c["hints"] for r in grade for c in r["rubric"] if c["kind"] in ("issue", "fact"))

    # the shipped grader, run as the agent runs it, with an OpenAI-compatible judge
    srv = HTTPServer(("127.0.0.1", 0), _Judge)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    matters = [r["task_id"] for r in grade]  # "<run folder>/<matter id>"
    results = {}
    try:
        for kind in ("gold", "flawed"):
            memos = tmp_path / f"{kind}.jsonl"
            memos.write_text("".join(json.dumps({"task_id": t, "response": json.loads((tmp_path / "run/accepted" / t.split("/")[1] / "answers.json").read_text())[kind]}) + "\n" for t in matters))
            res = tmp_path / f"{kind}.out.json"
            subprocess.run([sys.executable, str(out / "grade/evaluate.py"), "--responses", str(memos), "--judge", "openai",
                            "--judge-url", f"http://127.0.0.1:{srv.server_port}/v1", "--judge-model", "fake",
                            "--json-output-file", str(res)], check=True, capture_output=True, cwd=tmp_path)
            results[kind] = json.loads(res.read_text())
    finally:
        srv.shutdown()
    assert results["gold"]["accuracy"] == 1.0 and results["gold"]["n"] == len(grade)
    assert results["flawed"]["accuracy"] == 0.0 and results["flawed"]["criteria_pass_rate"] < 1.0
    for t in results["flawed"]["tasks"]:  # the flawed memo fails exactly the criteria of its omitted issue
        matter = tmp_path / "run/accepted" / t["task_id"].split("/")[1]
        omitted = json.loads((matter / "answers.json").read_text())["flawed_omits"]
        want = {c["id"] for c in json.loads((matter / "rubric.json").read_text())["criteria"] if c.get("source") in omitted}
        assert set(t["failed"]) == want
