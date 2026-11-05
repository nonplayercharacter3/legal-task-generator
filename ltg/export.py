"""Export accepted tasks as JSONL training data, one file per split.

Each line: `messages` (system, user = instruction plus every document, assistant = gold memo) for supervised
fine-tuning, and `eval` (task metadata and rubric) so reward-based training can grade a response. The ledger, the
planted issues, judge hints and the flawed answer are never written: they would leak the answers.
"""

from __future__ import annotations

import json
from pathlib import Path

from . import prompts

SPLITS = ("train", "dev", "test")


def _solver_model(run_dir: Path) -> str:
    try:
        b = json.loads((run_dir / "settings.json").read_text())["backend"]
    except (OSError, KeyError, ValueError):
        return ""
    return b.get("roles", {}).get("solver", {}).get("model") or b.get("models", {}).get("solver") or b.get("default_model") or b.get("kind", "")


def example(matter: Path, solver_model: str) -> dict:
    task = json.loads((matter / "task.json").read_text())
    split = json.loads((matter / "gates.json").read_text())["split"]
    docs = "\n\n".join(f"### {name}\n\n{(matter / 'docs' / name).read_text()}" for name in sorted(task["documents"]))
    criteria = json.loads((matter / "rubric.json").read_text())["criteria"]
    return {
        "messages": [
            {"role": "system", "content": prompts.SOLVER_WRITE},
            {"role": "user", "content": f"{task['instruction']}\n\n## Documents\n\n{docs}"},
            {"role": "assistant", "content": json.loads((matter / "answers.json").read_text())["gold"]},
        ],
        "eval": {
            "task_id": task["task_id"],
            "split": split,
            "practice_area": task["practice_area"],
            "agreement_type": task["agreement_type"],
            "jurisdiction": task["jurisdiction"],
            "rubric": [{"id": c["id"], "kind": c["kind"], "text": c["text"]} for c in criteria],
            "solver_pass_rate": task["solver_pass_rate"],
            "solver_model": solver_model,
        },
    }


def export(runs: list[str], out: str) -> dict:
    """Write <out>/{train,dev,test}.jsonl. Returns counts per split and the matter ids dropped as duplicates."""
    found: dict[str, list[Path]] = {}
    for r in runs:
        for m in sorted((Path(r) / "accepted").glob("*/task.json")):
            found.setdefault(m.parent.name, []).append(m.parent)
    dupes = sorted(k for k, v in found.items() if len(v) > 1)
    lines: dict[str, list[str]] = {s: [] for s in SPLITS}
    for mid, (matter, *rest) in sorted(found.items()):
        if rest:
            continue
        ex = example(matter, _solver_model(matter.parent.parent))
        lines[ex["eval"]["split"]].append(json.dumps(ex, ensure_ascii=False))
    Path(out).mkdir(parents=True, exist_ok=True)
    for s, ls in lines.items():
        (Path(out) / f"{s}.jsonl").write_text("".join(l + "\n" for l in ls), encoding="utf-8")
    return {"counts": {s: len(ls) for s, ls in lines.items()}, "duplicates": {k: [str(p) for p in found[k]] for k in dupes}}
