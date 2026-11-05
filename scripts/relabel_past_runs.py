"""Recover tasks that older runs rejected only for being solved 3 of 3.

Until 2026-11-04 solver_check threw away a sound task that the solver passed every time. Difficulty is now a label,
so those tasks are training data too. For each run folder given, this finds rejected matters that failed only at
solver_check with a pass rate of 1.0, every earlier gate passed and the no-documents probe failed, and writes a
task.json beside their other files (nothing else is moved or rewritten), so `ltg export` picks them up.

    python3 scripts/relabel_past_runs.py runs/cloud_pilot_r2 runs/pilot6_haiku ...
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ltg.export import _settings, _solver_model  # noqa: E402
from ltg.splits import assign_split  # noqa: E402


def recoverable(gates: dict) -> bool:
    if gates.get("accepted") or gates.get("failed_gate") != "solver_check" or gates.get("solver_pass_rate") != 1.0:
        return False
    results = gates.get("gates", [])
    sc = next((g for g in results if g["name"] == "solver_check"), None)
    if sc is None or sc["details"].get("probe_without_documents_passed") is not False:
        return False
    return all(g["passed"] for g in results if g["name"] != "solver_check")


NEEDED = ("instruction.md", "rubric.json", "answers.json", "docs")  # a slimmed folder (spec, ledger, gates only) cannot be exported


def relabel(matter: Path, settings: dict) -> dict:
    spec = json.loads((matter / "spec.json").read_text())
    gates = json.loads((matter / "gates.json").read_text())
    rubric = json.loads((matter / "rubric.json").read_text())["criteria"]
    hints = settings.get("gates", {}).get("judge_hints", True)
    splits = settings.get("splits", {})
    attempts = settings.get("gates", {}).get("solver_attempts", 3)
    return {
        "task_id": spec["matter_id"],
        "split": assign_split(spec["matter_id"], splits.get("ratios", {"train": 0.8, "dev": 0.1, "test": 0.1}), splits.get("salt", "ltg-v0")),
        "practice_area": spec["practice_area"],
        "agreement_type": spec["agreement_type"],
        "work_type": spec["work_type"],
        "jurisdiction": spec["jurisdiction"],
        "instruction": (matter / "instruction.md").read_text(),
        "documents": sorted(p.name for p in (matter / "docs").iterdir()),
        "rubric": [{"id": c["id"], "text": c["text"], "kind": c["kind"], "hints": c.get("hints", []) if hints else []} for c in rubric],
        "solver_pass_rate": gates["solver_pass_rate"],
        "unsolved": False,
        "difficulty": [{"model": _solver_model(settings), "attempts": attempts, "passes": attempts, "pass_rate": 1.0}],
        "relabelled": "rejected at solver_check for a pass rate of 1.0 before difficulty became a label (2026-11-04)",
    }


def main(runs: list[str]) -> int:
    total = 0
    for r in runs:
        run = Path(r)
        settings = _settings(run)
        done, missing = [], []
        for g in sorted(run.glob("rejected/*/gates.json")):
            if not recoverable(json.loads(g.read_text())):
                continue
            if not all((g.parent / f).exists() for f in NEEDED):
                missing.append(g.parent.name)
                continue
            (g.parent / "task.json").write_text(json.dumps(relabel(g.parent, settings), indent=2, ensure_ascii=False), encoding="utf-8")
            done.append(g.parent.name)
        total += len(done)
        print(f"{run}: recovered {len(done)}" + (f" ({', '.join(done)})" if done else "")
              + (f"; {len(missing)} qualify but lack {'/'.join(NEEDED)} on disk ({', '.join(missing)})" if missing else ""))
    print(f"total recovered: {total}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1:]))
