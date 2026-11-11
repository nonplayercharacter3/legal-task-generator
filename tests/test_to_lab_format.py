import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import to_lab_format  # noqa: E402


def test_convert_writes_lab_task(tmp_path):
    m = tmp_path / "runs/r1/accepted/s1-m0001"
    (m / "docs").mkdir(parents=True)
    (m / "docs/a.md").write_text("doc")
    (m / "task.json").write_text(json.dumps({"practice_area": "ma", "agreement_type": "spa", "instruction": "Review."}))
    crit = [{"id": "C1", "kind": "issue", "text": "The response finds X."}, {"id": "C2", "kind": "negative", "text": "The response claims Y."}]
    (m / "rubric.json").write_text(json.dumps({"criteria": crit}))
    name = to_lab_format.convert(m, tmp_path / "tasks")
    cfg = json.loads((tmp_path / "tasks" / name / "task.json").read_text())
    assert name == "ours/r1__s1-m0001" and (tmp_path / "tasks" / name / "documents/a.md").read_text() == "doc"
    assert cfg["deliverables"] == {"memo.md": "memo.md"} and "memo.md" in cfg["instructions"]
    assert cfg["criteria"][0]["match_criteria"].startswith("PASS if the memo satisfies")
    assert "does not make the following claim" in cfg["criteria"][1]["match_criteria"]
