"""Write accepted matter folders as LAB task folders (task.json + documents/), as LAB's harness and grader read them.

    python scripts/to_lab_format.py OUT_TASKS_DIR runs/pilot20_nrp/accepted/s20-m0001 [more matter folders]

Each matter becomes OUT_TASKS_DIR/ours/<run folder>__<matter id>/. Documents are copied as they are (Markdown). The
deliverable is `memo.md`, which LAB accepts as a deliverable like any file (its own prompt tells agents to write
plain Markdown with `write`), so the instruction says so and no .docx or pandoc is needed to read it. Each rubric
criterion becomes a LAB `match_criteria` in LAB's own "PASS if ... FAIL if ..." form; a negative criterion passes when
the claim is absent. Judge hints and the ledger are not written.
"""

import json
import shutil
import sys
from pathlib import Path

DELIVERABLE = "memo.md"


def match_criteria(c: dict) -> str:
    if c["kind"] == "negative":
        return (f"PASS if the memo does not make the following claim. FAIL if the memo makes it, even with a "
                f"qualification: {c['text']}")
    return f"PASS if the memo satisfies this: {c['text']} FAIL if it does not."


def convert(matter: Path, out_tasks: Path) -> str:
    task = json.loads((matter / "task.json").read_text())
    name = f"ours/{matter.parent.parent.name}__{matter.name}"
    dest = out_tasks / name
    shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(matter / "docs", dest / "documents")
    rubric = json.loads((matter / "rubric.json").read_text())["criteria"]
    cfg = {
        "title": f"Contract review: {task['agreement_type']} ({matter.parent.parent.name} {matter.name})",
        "work_type": "review",
        "tags": ["ltg", task["practice_area"], task["agreement_type"]],
        "instructions": f"{task['instruction'].rstrip()}\n\nOutput: `{DELIVERABLE}` (write the memo there as plain Markdown).",
        "deliverables": {DELIVERABLE: DELIVERABLE},
        "criteria": [{"id": c["id"], "title": f"{c['id']} ({c['kind']})", "match_criteria": match_criteria(c),
                      "deliverables": [DELIVERABLE]} for c in rubric],
    }
    (dest / "task.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False))
    return name


if __name__ == "__main__":
    out = Path(sys.argv[1])
    for m in sys.argv[2:]:
        print(convert(Path(m), out))
