"""Export tasks as JSONL training data, one file per split, optionally one difficulty band of one model.

Each line: `messages` (system, user = instruction plus every document, assistant = gold memo) for supervised
fine-tuning, and `eval` (task metadata, rubric and difficulty labels) so reward-based training can grade a response.
The ledger, the planted issues, judge hints and the flawed answer are never written: they would leak the answers.
"""

from __future__ import annotations

import json
from pathlib import Path

from . import prompts
from .splits import assign_split

SPLITS = ("train", "dev", "test")


def _settings(run_dir: Path) -> dict:
    try:
        return json.loads((run_dir / "settings.json").read_text())
    except (OSError, ValueError):
        return {}


def _solver_model(settings: dict) -> str:
    b = settings.get("backend", {})
    return b.get("roles", {}).get("solver", {}).get("model") or b.get("models", {}).get("solver") or b.get("default_model") or b.get("kind", "")


def difficulty(task: dict, settings: dict) -> list[dict]:
    """The task's labels; a task.json written before labels existed gets one from its pass rate and run settings."""
    if task.get("difficulty"):
        return task["difficulty"]
    rate, attempts = task.get("solver_pass_rate"), settings.get("gates", {}).get("solver_attempts", 3)
    if rate is None:
        return []
    return [{"model": _solver_model(settings), "attempts": attempts, "passes": round(rate * attempts), "pass_rate": rate}]


def task_id(matter: Path) -> str:
    """`<run folder name>/<matter id>`: matter ids come from the seed, so two runs with one seed share them (s9-m0003
    was drafted by both pilot9_haiku and pilot9_nrp). The split stays per matter id, so such drafts never straddle splits."""
    return f"{matter.parent.parent.resolve().name}/{matter.name}"


def parse_ratios(text: str) -> dict[str, float]:
    """`"0.7,0.15,0.15"` -> {"train": 0.7, "dev": 0.15, "test": 0.15}; three non-negative numbers summing to 1."""
    try:
        vals = [float(v) for v in text.split(",")]
    except ValueError:
        raise ValueError(f"--ratios takes three numbers TRAIN,DEV,TEST, not {text!r}") from None
    if len(vals) != 3 or min(vals) < 0 or abs(sum(vals) - 1) > 1e-6:
        raise ValueError(f"--ratios takes three non-negative numbers TRAIN,DEV,TEST summing to 1, not {text!r}")
    return dict(zip(SPLITS, vals))


def example(matter: Path, labels: list[dict], split: str | None = None) -> dict:
    task = json.loads((matter / "task.json").read_text())
    docs = "\n\n".join(f"### {name}\n\n{(matter / 'docs' / name).read_text()}" for name in sorted(task["documents"]))
    criteria = json.loads((matter / "rubric.json").read_text())["criteria"]
    return {
        "messages": [
            {"role": "system", "content": prompts.SOLVER_WRITE},
            {"role": "user", "content": f"{task['instruction']}\n\n## Documents\n\n{docs}"},
            {"role": "assistant", "content": json.loads((matter / "answers.json").read_text())["gold"]},
        ],
        "eval": {
            "task_id": task_id(matter),
            "matter_id": task["task_id"],
            "split": split or task["split"],
            "practice_area": task["practice_area"],
            "agreement_type": task["agreement_type"],
            "jurisdiction": task["jurisdiction"],
            "rubric": [{"id": c["id"], "kind": c["kind"], "text": c["text"]} for c in criteria],
            "difficulty": labels,
        },
    }


def export(runs: list[str], out: str, model: str | None = None, min_pass: float = 0.0, max_pass: float = 1.0,
           include_unsolved: bool = False, include_held: bool = False, include_pending: bool = False,
           ratios: dict[str, float] | None = None) -> dict:
    """Write <out>/{train,dev,test}.jsonl from every matter folder holding a task.json (accepted, or relabelled
    under rejected/). A task held by a person (`hold: {"reason", "by"}` in task.json) is left out unless
    `include_held`, and one still waiting for `ltg label` (`label_pending`: no label, no leak probe) unless
    `include_pending`. With `model`, keep only tasks that model labelled with min_pass <= pass_rate <= max_pass.
    With `ratios` ({"train", "dev", "test"}), each task's split is assigned again from its matter id and its run's
    salt, ignoring the stored one: hashing keeps it deterministic, stable when tasks join, and twin drafts of one matter
    id in the same split. Returns counts per split, the task ids dropped as duplicates (two run folders with one name),
    how many the filters left out, and how many tasks `moved` split under `ratios`."""
    found: dict[str, list[Path]] = {}
    for r in runs:
        for m in sorted(Path(r).glob("*/*/task.json")):
            found.setdefault(task_id(m.parent), []).append(m.parent)
    dupes = sorted(k for k, v in found.items() if len(v) > 1)
    lines: dict[str, list[str]] = {s: [] for s in SPLITS}
    skipped = {"held": 0, "pending": 0, "unsolved": 0, "outside_band": 0}
    moved = 0
    for tid, (matter, *rest) in sorted(found.items()):
        if rest:
            continue
        task = json.loads((matter / "task.json").read_text())
        settings = _settings(matter.parent.parent)
        labels = difficulty(task, settings)
        if task.get("hold") and not include_held:
            skipped["held"] += 1
            continue
        if task.get("label_pending") and not include_pending:
            skipped["pending"] += 1
            continue
        if task.get("unsolved") and not include_unsolved:
            skipped["unsolved"] += 1
            continue
        if model is not None:
            mine = [d for d in labels if d["model"] == model]
            if not mine or not min_pass <= mine[0]["pass_rate"] <= max_pass:
                skipped["outside_band"] += 1
                continue
        split = None
        if ratios is not None:
            split = assign_split(task["task_id"], ratios, settings.get("splits", {}).get("salt", "ltg-v0"))
            moved += split != task["split"]
        ex = example(matter, labels, split)
        lines[ex["eval"]["split"]].append(json.dumps(ex, ensure_ascii=False))
    Path(out).mkdir(parents=True, exist_ok=True)
    for s, ls in lines.items():
        (Path(out) / f"{s}.jsonl").write_text("".join(l + "\n" for l in ls), encoding="utf-8")
    return {"counts": {s: len(ls) for s, ls in lines.items()}, "duplicates": {k: [str(p) for p in found[k]] for k in dupes}, "skipped": skipped, "moved": moved}
