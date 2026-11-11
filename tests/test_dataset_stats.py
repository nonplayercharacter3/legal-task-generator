"""`scripts/dataset_stats.py` on the fake demo output and on a tiny made-up LAB-shaped folder."""

import json
import sys
import zipfile
from pathlib import Path

from ltg.orchestrator import Pipeline

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from dataset_stats import main as stats_main  # noqa: E402


def _docx(path: Path, text: str) -> None:
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("word/document.xml", f"<w:document><w:t>{text}</w:t></w:document>")


def _lab(root: Path) -> Path:
    """tasks/<area>/<task> (practice-area), tasks/contracts/<sub>/<task>/scenario-01, tasks/firm-knowledge/tasks/1."""
    t = root / "tasks"
    a = t / "tax" / "t1"
    (a / "documents").mkdir(parents=True)
    _docx(a / "documents" / "one.docx", "alpha beta gamma")
    (a / "documents" / "two.txt").write_text("delta epsilon")
    (a / "documents" / "lfs.docx").write_bytes(b"version https://git-lfs.github.com/spec/v1\n")
    crit = [{"id": f"C-{i}", "title": "x", "match_criteria": "y"} for i in range(4)]
    (a / "task.json").write_text(json.dumps({"title": "T", "work_type": "draft", "tags": [], "criteria": crit,
                                             "instructions": "Review one.docx and two.txt, then draft.",
                                             "deliverables": {"memo.docx": "memo.docx"}}))
    c = t / "contracts" / "sub" / "t2" / "scenario-01"
    (c / "documents").mkdir(parents=True)
    (c / "documents" / "x.eml").write_text("one two three four")
    (c / "task.json").write_text(json.dumps({"title": "T", "criteria": crit[:2], "instructions": "Do it."}))
    f = t / "firm-knowledge" / "tasks" / "1"
    f.mkdir(parents=True)
    (f / "task.json").write_text(json.dumps({"id": 1, "docs_dir": "../../dms", "criteria": crit[:1],
                                             "instructions": "Find.", "deliverables": {"response.md": "response.md"}}))
    return root


def test_stats_on_fake_run_and_lab_shaped_folder(cfg, tmp_path):
    Pipeline(cfg).run()
    out = tmp_path / "out"
    assert stats_main(["--runs", cfg.run.out_dir, "--lab", str(_lab(tmp_path / "lab")), "--out", str(out),
                       "--model", "solver"]) == 0
    d = json.loads((out / "dataset_stats.json").read_text())
    ours, lab = d["stats"]["ours"], d["stats"]["LAB, all"]
    assert ours["tasks"] > 0 and ours["issues_per_task"]["total"] > 0
    assert ours["instruction_words"]["mean"] > 0
    assert lab["tasks"] == 3 and lab["practice_areas"] == {"tax": 1, "contracts": 1, "firm-knowledge": 1}
    pa = d["stats"]["LAB practice-area"]
    assert pa["documents_per_task"]["median"] == 3 and pa["words_per_folder"]["median"] == 5  # pointer adds 0
    assert pa["instructions_naming_every_file"] == 0  # lfs.docx is not named
    assert pa["deliverable_formats"] == {".docx": 1}
    assert d["stats"]["LAB contracts"]["deliverable"] == {"not stated (reply)": 1}
    assert d["stats"]["LAB firm-knowledge"]["documents_per_task"]["median"] == 0
    pc = d["per_check"]
    assert pc["attempts"] > 0 and 0 <= pc["all_pass_rate"] <= pc["criteria"]["pass_rate"] <= 1
    assert (out / "dataset_stats.md").read_text().startswith("# Dataset statistics")
