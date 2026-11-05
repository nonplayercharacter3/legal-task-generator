"""`ltg export`: accepted fake-demo tasks to JSONL, one file per split, with nothing from the answer key."""

import json
import shutil
from pathlib import Path

from ltg.cli import main
from ltg.orchestrator import Pipeline


def test_export_splits_and_no_answer_key(cfg, tmp_path, capsys):
    report = Pipeline(cfg).run()
    run = Path(cfg.run.out_dir)
    want = {s: sum(m["split"] == s for m in report["matters"] if m["accepted"]) for s in ("train", "dev", "test")}
    assert sum(want.values()) == report["accepted"] > 0

    out = tmp_path / "export"
    assert main(["export", "--runs", str(run), "--out", str(out)]) == 0
    raw = {s: (out / f"{s}.jsonl").read_text().splitlines() for s in want}
    assert {s: len(ls) for s, ls in raw.items()} == want

    # Ledger-only text must never appear. Detect terms are not checked: issue_check requires them verbatim in the
    # documents, which the export includes in full.
    secrets = []
    for m in (run / "accepted").iterdir():
        led = json.loads((m / "ledger.json").read_text())
        secrets += [led["summary"], json.loads((m / "answers.json").read_text())["flawed"]]
        secrets += [i["description"] for i in led["issues"]]
    for s, ls in raw.items():
        for line in ls:
            ex = json.loads(line)
            assert ex["eval"]["split"] == s
            assert [m["role"] for m in ex["messages"]] == ["system", "user", "assistant"]
            assert all(set(c) == {"id", "kind", "text"} for c in ex["eval"]["rubric"])
            for key in ('"detect_terms"', '"expected_finding"', '"hints"', '"issues"'):
                assert key not in line
            for secret in secrets:
                assert json.dumps(secret)[1:-1] not in line

    # the same matter id in two runs: reported, kept in neither
    twin = tmp_path / "twin"
    shutil.copytree(run / "accepted", twin / "accepted")
    assert main(["export", "--runs", str(run), str(twin), "--out", str(out)]) == 0
    assert "duplicate matter id" in capsys.readouterr().err
    assert all((out / f"{s}.jsonl").read_text() == "" for s in want)
