#!/usr/bin/env python3
"""Build a task folder for the lab's post-training agent (aibuildai-inc/aibuildai-llm-posttrain-agent).

    python scripts/build_handoff.py --out handoff/<name> --runs runs/pilot2*_nrp [export options]

Runs `ltg export` with the same filters, then writes the folder in the shape of the agent's GSM8K example:

    README.md          the task statement (the agent freezes it as the run's README)
    data/train.jsonl   the train split: chat messages ending in the gold memo, plus rubric and difficulty labels
    grade/evaluate.py  the frozen grader (scripts/handoff_evaluate.py)
    grade/dev.jsonl    the grader's tasks: the dev split, prompt and rubric with the judge's hints, no gold memo
    grade/ltg/         a frozen copy of this repo's ltg/*.py, which the grader imports its judge from

The test split is not shipped: it stays with us for a final check. No model calls; no base weights are copied.
"""

from __future__ import annotations

import argparse
import json
import shutil
import statistics
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from ltg.export import export, parse_ratios, task_id  # noqa: E402

STATEMENT = """# Post-train `{base_model}` to review contracts like a law-firm associate

Post-train the base language model in `base_model/` so that, given a partner's instruction and a folder of
contract documents, it writes the review memo the partner asked for, measured by the frozen grader in `grade/`.

## Objective

Maximize the `accuracy` the grader reports on `grade/dev.jsonl`. Store the model you want measured in a directory
named `final_model` inside your working directory. It must be a fine-tune of `base_model/`.

## What the tasks are

Each task is an invented commercial or M&A matter (Delaware or New York law): a partner-style instruction, 3 to 5
matter documents (agreements, schedules, side letters, emails) given in full in the user turn, and an all-pass
rubric. The generator first wrote an answer key with 3 to 5 planted issues tied to a document and section, then
drafted the documents, instruction and rubric from it, and kept a task only if a reference memo passes every
criterion and a memo that misses one issue fails. Rubric criteria are of four kinds: `issue` (finds a planted
problem, says where it is, why it matters and recommends a fix), `fact` (states a deal fact correctly), `format`
and `negative` (a wrong claim or bad act the memo must not make).

## What is in this folder

    base_model/         the frozen base weights, {base_model}. Read-only. Placed here when the run is set up.
    data/train.jsonl    {n_train} tasks. Training data.
    grade/evaluate.py   THE grader. Frozen: never modify it, never re-implement it, never substitute your own metric.
    grade/dev.jsonl     {n_dev} tasks, the grader's input: prompt and rubric, no reference memo.
    grade/ltg/          code the grader imports its judge from. Frozen.

Each line of `data/train.jsonl` holds `messages` (system prompt, user turn = instruction plus every document,
assistant turn = the reference memo) for supervised fine-tuning, and `eval`: `task_id`, `practice_area`,
`agreement_type`, `jurisdiction`, `rubric` (`id`, `kind`, `text` per criterion) and `difficulty` (per solver model:
`attempts`, `passes`, `pass_rate`; 0.0 means that model never passed it). User turns run {words_min} to {words_max}
words (median {words_median}), about 1.4 tokens per word; reference memos {memo_min} to {memo_max} words.
Pass rates in the train split: {labels}.

## How the model is scored

    python grade/evaluate.py --model-path <dir> --json-output-file out.json

`--limit N` grades the first N tasks, for smoke tests. The JSON holds `accuracy` (higher is better), `n`, `stderr`,
`criteria_pass_rate` and per-task results with the judge's reason for every failed criterion. The contract:

- **Prompt.** The task's system and user messages through the model's own chat template, nothing else.
- **Decoding.** Greedy, at most 12000 new tokens. A `<think>` block is removed before judging.
- **Judge.** An LLM grades the memo against each criterion, strictly and from the memo text alone. An issue
  criterion passes on any sound route to its conclusion. A negative criterion passes when the memo does not make
  the claim; quoting, rejecting or warning against it is not making it.
- **Metric.** `accuracy` is the fraction of tasks whose memo passes every criterion. With {n_dev} tasks it is
  coarse: `criteria_pass_rate` moves first, and a new candidate should beat the incumbent by more than `stderr`.

The judge is chosen with `--judge`: `sdk` (Claude through the Claude Agent SDK on this machine's Claude Code login,
the generator's own judge, the default) or `openai` with `--judge-url`, `--judge-model` and `--judge-key-env`.

## Rules

1. **Only this base model.** Fine-tune only the weights in `base_model/`.
2. **No external-model distillation.** Do not call a hosted LLM API during this run except through
   `grade/evaluate.py`, and do not author training examples yourself. Published public datasets are allowed.
3. **Contamination boundary.** Do not train on `grade/dev.jsonl` or derive training data from its tasks.
4. **LAB is the held-out exam.** Harvey's Legal Agent Benchmark (`harveyai/harvey-labs`, "LAB") is how the
   trained model will be evaluated. Never download, read, train on or derive data from it, or from any copy of it.
5. **The deliverable loads plainly.** `final_model/` loads with `transformers.AutoModelForCausalLM.from_pretrained`:
   real files, no symlinks, no hard links, no unmerged adapter.

## Environment

The grader needs `torch` and `transformers` in the run's Program environment, and for `--judge sdk` the
`claude-agent-sdk` package and a Claude Code login.
"""


def _words(s: str) -> int:
    return len(s.split())


def build(out: Path, runs: list[str], base_model: str, **filters) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        res = export(runs, tmp, **filters)
        rows = {s: [json.loads(l) for l in (Path(tmp) / f"{s}.jsonl").read_text(encoding="utf-8").splitlines()] for s in ("train", "dev")}
    if not rows["train"] or not rows["dev"]:
        raise SystemExit(f"need train and dev tasks, got {res['counts']}")
    rubrics = {task_id(m.parent): json.loads((m.parent / "rubric.json").read_text())["criteria"] for r in runs for m in Path(r).glob("*/*/task.json")}

    if out.exists():
        shutil.rmtree(out)
    (out / "data").mkdir(parents=True)
    (out / "grade" / "ltg").mkdir(parents=True)
    (out / "data" / "train.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows["train"]), encoding="utf-8")
    grade_rows = [{"task_id": r["eval"]["task_id"], "messages": r["messages"][:2],
                   "rubric": [{k: c.get(k) for k in ("id", "kind", "text", "hints")} for c in rubrics[r["eval"]["task_id"]]]}
                  for r in rows["dev"]]
    (out / "grade" / "dev.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in grade_rows), encoding="utf-8")
    shutil.copyfile(ROOT / "scripts" / "handoff_evaluate.py", out / "grade" / "evaluate.py")
    for f in (ROOT / "ltg").glob("*.py"):
        shutil.copyfile(f, out / "grade" / "ltg" / f.name)

    users = [_words(r["messages"][1]["content"]) for s in rows.values() for r in s]
    memos = [_words(r["messages"][2]["content"]) for r in rows["train"]]
    bands: dict[str, list[float]] = {}
    for r in rows["train"]:
        for d in r["eval"]["difficulty"]:
            bands.setdefault(d["model"], []).append(d["pass_rate"])
    labels = "; ".join(f"{m}: " + ", ".join(f"{v:.2f} x{vs.count(v)}" for v in sorted(set(vs))) for m, vs in bands.items()) or "none"
    (out / "README.md").write_text(STATEMENT.format(
        base_model=base_model, n_train=len(rows["train"]), n_dev=len(rows["dev"]), labels=labels,
        words_min=min(users), words_max=max(users), words_median=int(statistics.median(users)),
        memo_min=min(memos), memo_max=max(memos)), encoding="utf-8")
    return {**res, "out": str(out)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="the task folder to write, e.g. handoff/v0")
    ap.add_argument("--runs", nargs="+", required=True, help="run folders to export from")
    ap.add_argument("--base-model", default="<base model chosen by the lab>", help="named in the statement")
    ap.add_argument("--model", default=None, help="keep only tasks this solver model labelled within the band")
    ap.add_argument("--min-pass", type=float, default=0.0)
    ap.add_argument("--max-pass", type=float, default=1.0)
    ap.add_argument("--include-unsolved", action="store_true")
    ap.add_argument("--include-held", action="store_true")
    ap.add_argument("--include-pending", action="store_true")
    ap.add_argument("--ratios", metavar="TRAIN,DEV,TEST", help="re-assign splits as `ltg export --ratios` does")
    a = ap.parse_args(argv)
    try:
        ratios = parse_ratios(a.ratios) if a.ratios else None
    except ValueError as e:
        ap.error(str(e))
    res = build(Path(a.out), a.runs, a.base_model, model=a.model, min_pass=a.min_pass, max_pass=a.max_pass,
                include_unsolved=a.include_unsolved, include_held=a.include_held, include_pending=a.include_pending, ratios=ratios)
    print(f"handoff -> {res['out']}: train {res['counts']['train']}, dev {res['counts']['dev']} (test {res['counts']['test']} kept back); "
          f"left out {res['skipped']}" + (f"; duplicates dropped: {', '.join(res['duplicates'])}" if res["duplicates"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
