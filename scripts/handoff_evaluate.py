#!/usr/bin/env python3
"""The frozen grader: all-pass rubric accuracy on legal contract-review tasks.

Copied into a handoff package as `grade/evaluate.py` by `scripts/build_handoff.py`, beside `grade/ltg/` (a frozen copy
of the generator's code: the judge prompt and grading rule are imported from it, never restated) and `grade/dev.jsonl`
(one task per line: `task_id`, `messages` = system and user turn, `rubric` with the judge's hints).

  prompt     the task's system and user messages, through the model's own chat template
  decoding   greedy, at most --max-new-tokens new tokens; any <think> block is dropped before judging
  judge      an LLM grades the memo against each rubric criterion (ltg.stages.judge_with_reasons); a negative
             criterion passes when the judge says the claim is not made
  metric     accuracy = fraction of tasks whose memo passes every criterion (all-pass);
             criteria_pass_rate = fraction of all criteria passed, a smoother signal for small splits

    python evaluate.py --model-path <dir> --json-output-file out.json
    python evaluate.py --responses memos.jsonl ...      grade memos written elsewhere ({"task_id", "response"} per line)

Judge: `--judge sdk` (Claude through the Claude Agent SDK on this machine's Claude Code login, the generator's own
judge) or `--judge openai --judge-url <base>/v1 --judge-model <id> [--judge-key-env VAR]` (any OpenAI-compatible
endpoint). Only the judge calls a model API; the candidate runs locally.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from ltg.models import ClaudeAgentClient, OpenAICompatClient  # noqa: E402
from ltg.schema import Rubric  # noqa: E402
from ltg.stages import judge_with_reasons  # noqa: E402

_THINK = re.compile(r"<think>.*?</think>", re.S)


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="All-pass rubric grader for legal contract-review memos.")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--model-path", help="model directory or hub id; memos are generated with transformers")
    src.add_argument("--responses", help="JSONL of {task_id, response}: grade these memos instead of generating")
    p.add_argument("--data", default=str(HERE / "dev.jsonl"), help="the grader's tasks")
    p.add_argument("--limit", type=int, default=-1, help="tasks to grade from the front of the file; -1 grades all")
    p.add_argument("--json-output-file", default=None)
    p.add_argument("--max-new-tokens", type=int, default=12000)
    p.add_argument("--dtype", default="bfloat16", choices=("bfloat16", "float16", "float32"))
    p.add_argument("--judge", default="sdk", choices=("sdk", "openai"))
    p.add_argument("--judge-model", default="opus", help="sdk: a Claude model or alias; openai: the endpoint's model id")
    p.add_argument("--judge-url", default=None, help="openai: base URL ending in /v1")
    p.add_argument("--judge-key-env", default=None, help="openai: environment variable holding the API key")
    return p.parse_args(argv)


def judge_client(a: argparse.Namespace):
    if a.judge == "sdk":
        return ClaudeAgentClient(a.judge_model)
    if not a.judge_url:
        raise SystemExit("--judge openai needs --judge-url")
    return OpenAICompatClient(a.judge_url, a.judge_model, api_key_env=a.judge_key_env, temperature=0.0, max_tokens=16000)


def generate(model_path: str, tasks: list[dict], max_new_tokens: int, dtype: str) -> dict[str, str]:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, dtype=getattr(torch, dtype),
                                                 device_map="cuda" if torch.cuda.is_available() else "cpu")
    model.eval()
    out = {}
    for n, t in enumerate(tasks, 1):  # one at a time: prompts run to ~30k tokens, so batching buys little
        ids = tok.apply_chat_template(t["messages"], add_generation_prompt=True, return_tensors="pt").to(model.device)
        with torch.inference_mode():
            gen = model.generate(ids, max_new_tokens=max_new_tokens, do_sample=False, temperature=None, top_p=None,
                                 top_k=None, pad_token_id=tok.pad_token_id or tok.eos_token_id)
        out[t["task_id"]] = tok.decode(gen[0, ids.shape[1]:], skip_special_tokens=True)
        print(f"  generated {n}/{len(tasks)}", flush=True)
    return out


def grade(tasks: list[dict], responses: dict[str, str], judge) -> dict:
    rows = []
    for t in tasks:
        memo = _THINK.sub("", responses.get(t["task_id"], "")).strip()
        grades, reasons = judge_with_reasons(judge, memo, Rubric.from_dict({"criteria": t["rubric"]}))
        rows.append({"task_id": t["task_id"], "all_pass": all(grades.values()), "passed": sum(grades.values()),
                     "criteria": len(grades), "failed": {k: reasons[k] for k, ok in grades.items() if not ok}})
    n = len(rows)
    acc = sum(r["all_pass"] for r in rows) / n
    return {"accuracy": acc, "n": n, "stderr": (acc * (1 - acc) / n) ** 0.5,
            "criteria_pass_rate": sum(r["passed"] for r in rows) / max(1, sum(r["criteria"] for r in rows)), "tasks": rows}


def main(argv=None) -> int:
    a = parse_args(argv)
    tasks = [json.loads(l) for l in Path(a.data).read_text(encoding="utf-8").splitlines() if l.strip()]
    tasks = tasks[: a.limit] if a.limit >= 0 else tasks
    if not tasks:
        raise SystemExit(f"no tasks in {a.data}")
    judge = judge_client(a)
    t0 = time.time()
    if a.responses:
        lines = Path(a.responses).read_text(encoding="utf-8").splitlines()
        responses = {r["task_id"]: r["response"] for r in map(json.loads, filter(str.strip, lines))}
    else:
        responses = generate(a.model_path, tasks, a.max_new_tokens, a.dtype)
    metrics = grade(tasks, responses, judge)
    metrics["seconds"] = round(time.time() - t0)
    print(json.dumps({k: v for k, v in metrics.items() if k != "tasks"}, indent=2))
    if a.json_output_file:
        Path(a.json_output_file).parent.mkdir(parents=True, exist_ok=True)
        Path(a.json_output_file).write_text(json.dumps(metrics, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
