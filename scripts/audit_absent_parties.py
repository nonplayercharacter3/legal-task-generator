"""List tasks whose planted issue, or whose instruction, names a ledger party that no document mentions. No model calls.

    python3 scripts/audit_absent_parties.py                 # every task under runs/
    python3 scripts/audit_absent_parties.py runs/pilot9_nrp runs/pilot27_nrp

s9-m0002 (2026-11-09): issue I1 rested on a sale to Pellworth Capital Partners, which no document names; the solver
could only take the name from the instruction. This runs the same check as `issue_check`'s `absent_parties` over
every task already kept (accepted, or relabelled under rejected/), and the same check on each instruction.
Prints one line per hit: task, where (an issue id or "instruction"), party id and name.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ltg.gates import parties_absent  # noqa: E402
from ltg.schema import Ledger  # noqa: E402


def audit(matter: Path) -> list[tuple[str, str, str]]:
    ledger = Ledger.from_dict(json.loads((matter / "ledger.json").read_text()))
    docs = {f.name: f.read_text(encoding="utf-8") for f in sorted((matter / "docs").iterdir())}
    hits = [(i.id, p["party"], p["name"]) for i in ledger.issues
            for p in parties_absent(f"{i.description} {i.expected_finding}", ledger, docs)]
    instruction = (matter / "instruction.md").read_text(encoding="utf-8") if (matter / "instruction.md").exists() else ""
    return hits + [("instruction", p["party"], p["name"]) for p in parties_absent(instruction, ledger, docs)]


def main(argv: list[str]) -> int:
    runs = [Path(a) for a in argv] or sorted(p for p in Path("runs").iterdir() if p.is_dir())
    tasks = sorted(t.parent for r in runs for t in r.glob("*/*/task.json"))
    n = 0
    for m in tasks:
        for where, pid, name in audit(m):
            n += 1
            print(f"{m.parent.parent.name}/{m.name}  {where}  {pid}  {name}")
    print(f"{n} hit(s) in {len(tasks)} task(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
