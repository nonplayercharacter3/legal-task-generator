"""Drop rubric criteria a review judged too strict and relabel the task from its stored solver grades, without
model calls.

    python3 scripts/drop_criteria.py --by "T25 review 2026-11" runs/pilot20_nrp/accepted/s20-m0002:C6 ...

For each matter folder: rubric.json is first kept as rubric.original.json, then the criteria are removed from
rubric.json and task.json; task.json records `relabelled: {"dropped": [...], "by": ...}`. Each attempt's pass is
recomputed from its stored `failed_criteria` minus the dropped ones, and the difficulty label, pass rate and
`unsolved` are updated in task.json and gates.json. The stored per-attempt grades stay as they were judged.
Run reports (report.json, report.md) are not rewritten. Prints old and new labels.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _write(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def relabel(matter: Path, dropped: list[str], by: str) -> tuple[list[dict], list[dict]]:
    rubric = json.loads((matter / "rubric.json").read_text())
    ids = {c["id"] for c in rubric["criteria"]}
    if missing := [c for c in dropped if c not in ids]:
        raise SystemExit(f"{matter}: no criterion {', '.join(missing)} in rubric.json (already dropped?)")
    original = matter / "rubric.original.json"
    if not original.exists():
        original.write_text((matter / "rubric.json").read_text())
    rubric["criteria"] = [c for c in rubric["criteria"] if c["id"] not in dropped]
    _write(matter / "rubric.json", rubric)

    gates = json.loads((matter / "gates.json").read_text())
    sc = next(g for g in gates["gates"] if g["name"] == "solver_check")["details"]
    old = [dict(d) for d in sc["difficulty"]]
    new = []
    for d in sc["difficulty"]:
        runs = sc["runs"][d["model"]]
        passes = sum(not (set(r["failed_criteria"]) - set(dropped)) for r in runs)
        new.append({**d, "passes": passes, "pass_rate": round(passes / max(d["attempts"], 1), 3)})
    unsolved = not any(d["passes"] for d in new)
    sc.update({"difficulty": new, "pass_rate": new[0]["pass_rate"], "unsolved": unsolved})
    gates.update({"difficulty": new, "solver_pass_rate": new[0]["pass_rate"], "unsolved": unsolved})
    _write(matter / "gates.json", gates)

    task = json.loads((matter / "task.json").read_text())
    task["rubric"] = [c for c in task["rubric"] if c["id"] not in dropped]
    task.update({"difficulty": new, "solver_pass_rate": new[0]["pass_rate"], "unsolved": unsolved,
                 "relabelled": {"dropped": dropped, "by": by}})
    _write(matter / "task.json", task)
    return old, new


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--by", required=True, help="who judged the criteria too strict, recorded in task.json")
    ap.add_argument("matters", nargs="+", help="<matter folder>:<criterion id>[,<criterion id>...]")
    a = ap.parse_args()
    for arg in a.matters:
        folder, _, crits = arg.rpartition(":")
        old, new = relabel(Path(folder), crits.split(","), a.by)
        fmt = lambda ds: ", ".join(f"{d['model']} {d['passes']}/{d['attempts']}" for d in ds)
        print(f"{Path(folder).name}: dropped {crits}; {fmt(old)} -> {fmt(new)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
