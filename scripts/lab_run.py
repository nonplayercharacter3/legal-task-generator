"""Run one task through LAB's own harness with Qwen on NRP, then grade it with our SDK judge in place of LAB's judges.

    runs/lab_venv/bin/python scripts/lab_run.py TASK [--tag r1] [--judge-only]

TASK is a LAB task id (`corporate-ma/analyze-cim-deal-teaser/scenario-01`) or `ours/<name>` from to_lab_format.py.
LAB root is runs/lab_root (LAB's tasks symlinked or copied in; results and scores land in runs/lab_root/results/), so
nothing under ../harvey-labs is written. Needs the venv with lab-core and claude-agent-sdk, pandoc 3.5+ on PATH
(LAB documents are .docx), podman running, and NRP_LLM_API_KEY.

Two glue pieces, nothing else changed:
- NRP serves /v1/chat/completions only (no Responses API), so the agent uses LAB's own Baseten adapter, which is a
  plain OpenAI-compatible chat adapter, with reasoning_effort "low" as in our solver config and replies without the
  model's reasoning text.
- LAB's judge reads one criterion per call through `Judge.evaluate`; SdkJudge answers that call with Opus through the
  Claude Agent SDK (the Max plan), with LAB's own prompt template. LAB's default is two judges; this is one.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
os.environ.setdefault("LAB_ROOT", str(Path(os.environ.get("LAB_ROOT_DIR", "/Users/shesirui/Projects/legal-task-generator/runs/lab_root"))))
os.environ["BASETEN_API_KEY"] = os.environ["NRP_LLM_API_KEY"]
os.environ["BASETEN_BASE_URL"] = "https://ellm.nrp-nautilus.io/v1"

import openai  # noqa: E402
from lab_core import paths  # noqa: E402
from lab_core.evaluation.judge import Judge  # noqa: E402
from lab_core.evaluation.run_eval import evaluate_run  # noqa: E402
from lab_core.harness import run as lab_run  # noqa: E402
from lab_core.harness.adapters.baseten import BasetenAdapter  # noqa: E402
from ltg.models import CallLog, ClaudeAgentClient  # noqa: E402

MODEL = "qwen3-small"
MAX_TOKENS = 32000  # one reply, thinking included; 16000 was cut off mid-thought on a long matter (s20-m0001)


class NRPAdapter(BasetenAdapter):
    def __init__(self, **kw):
        super().__init__(**{**kw, "reasoning_effort": None, "max_tokens": MAX_TOKENS})
        self.client = openai.OpenAI(api_key=os.environ["BASETEN_API_KEY"], base_url=os.environ["BASETEN_BASE_URL"],
                                    timeout=1200, max_retries=4)
        create = self.client.chat.completions.create
        self.client.chat.completions.create = lambda **k: create(**k, extra_body={"reasoning_effort": "low"})

    def chat(self, messages, tools):
        r = super().chat(messages, tools)
        for k in ("reasoning", "reasoning_content"):
            r.message.pop(k, None)
        return r


class SdkJudge(Judge):
    def __init__(self, calls: CallLog):
        self.model = "opus"
        self.calls = calls
        self.client = ClaudeAgentClient("opus", log=calls)

    def evaluate(self, prompt_template, variables, temperature=0.0, _retries=2):
        prompt = prompt_template.format(**variables)
        for _ in range(_retries):
            out = self.client.complete("judge", "You are a careful grader. Reply with the JSON object only.", prompt)
            try:
                return self._parse_json(out)
            except ValueError:
                pass
        raise ValueError("judge reply had no JSON")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("task")
    ap.add_argument("--tag", default="r1")
    ap.add_argument("--judge-only", action="store_true")
    a = ap.parse_args()
    run_id = f"{a.task}/{MODEL}-low/{a.tag}"
    run_dir = paths.results_dir() / run_id
    if not a.judge_only:
        lab_run.BasetenAdapter = NRPAdapter
        lab_run.main(lab_run.parser.parse_args(["--model", f"baseten/{MODEL}", "--task", a.task, "--run-id", run_id,
                                                 "--reasoning-effort", "low", "--max-turns", "60"]))
    calls = CallLog()
    t0 = time.time()
    scores = evaluate_run(run_id, a.task, SdkJudge(calls), parallel=4)
    (run_dir / "judge_calls.json").write_text(json.dumps({"calls": len(calls.records), "ok": sum(r.ok for r in calls.records),
                                                           "seconds": round(time.time() - t0)}))
    print(scores["summary"])
