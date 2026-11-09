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

    # the same matter id in two runs (one seed run twice): both exported, keyed by run folder, same split
    twin = tmp_path / "twin"
    shutil.copytree(run / "accepted", twin / "accepted")
    assert main(["export", "--runs", str(run), str(twin), "--out", str(out)]) == 0
    assert capsys.readouterr().err == ""
    rows = [json.loads(l)["eval"] for s in want for l in (out / f"{s}.jsonl").read_text().splitlines()]
    assert len(rows) == 2 * sum(want.values())
    assert {r["task_id"] for r in rows} == {f"{f}/{m}" for f in (run.name, "twin") for m in {r["matter_id"] for r in rows}}
    by_matter = {}
    for r in rows:
        by_matter.setdefault(r["matter_id"], set()).add(r["split"])
    assert all(len(splits) == 1 for splits in by_matter.values())

    # the same run folder passed twice is a duplicate task id: reported, kept in neither
    assert main(["export", "--runs", str(run), str(run), "--out", str(out)]) == 0
    assert "duplicate task id" in capsys.readouterr().err
    assert all((out / f"{s}.jsonl").read_text() == "" for s in want)


def test_export_filters_by_difficulty_band_and_unsolved(cfg, tmp_path):
    from ltg.config import load_config

    rep = Pipeline(cfg).run()
    rates = {m["matter_id"]: m["solver_pass_rate"] for m in rep["matters"]}
    assert len(set(rates.values())) > 1  # the fake spreads the labels
    low = min(rates.values())
    out = tmp_path / "band"

    def exported(*flags):
        assert main(["export", "--runs", cfg.run.out_dir, "--out", str(out), *flags]) == 0
        return {json.loads(l)["eval"]["matter_id"] for s in ("train", "dev", "test") for l in (out / f"{s}.jsonl").read_text().splitlines()}

    assert exported() == set(rates)
    assert exported("--model", "solver", "--min-pass", str(low), "--max-pass", str(low)) == {m for m, r in rates.items() if r == low}
    assert exported("--model", "solver", "--min-pass", str(low + 0.01)) == {m for m, r in rates.items() if r > low}
    assert exported("--model", "nobody") == set()
    assert main(["export", "--runs", cfg.run.out_dir, "--out", str(out)]) == 0
    ex = json.loads((out / "train.jsonl").read_text().splitlines()[0])
    assert ex["eval"]["difficulty"][0]["model"] == "solver" and "solver_pass_rate" not in ex["eval"]
    assert main(["export", "--runs", cfg.run.out_dir, "--out", str(out), "--min-pass", "0.5"]) == 2  # a band needs a model

    hard = load_config(None, {"run": {"out_dir": str(tmp_path / "hard"), "n_matters": 3}, "fake": {"solver_skill": 0.0}})
    assert Pipeline(hard).run()["unsolved"] == 3
    assert main(["export", "--runs", hard.run.out_dir, "--out", str(out)]) == 0
    assert all((out / f"{s}.jsonl").read_text() == "" for s in ("train", "dev", "test"))
    assert main(["export", "--runs", hard.run.out_dir, "--out", str(out), "--include-unsolved"]) == 0
    assert sum(len((out / f"{s}.jsonl").read_text().splitlines()) for s in ("train", "dev", "test")) == 3


def test_relabel_script_recovers_only_old_too_easy_rejections(cfg, tmp_path, capsys):
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("relabel", Path(__file__).resolve().parent.parent / "scripts" / "relabel_past_runs.py")
    relabel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(relabel)

    Pipeline(cfg).run()
    run = Path(cfg.run.out_dir)
    old = {}  # make every matter look like an old run: rejected at solver_check, with its true pass rate
    for m in sorted((run / "accepted").iterdir()):
        g = json.loads((m / "gates.json").read_text())
        g.update({"accepted": False, "failed_gate": "solver_check", "split": None})
        (m / "task.json").unlink()
        (m / "gates.json").write_text(json.dumps(g))
        old[m.name] = g["solver_pass_rate"]
    (run / "accepted").rename(run / "rejected")
    leaky = next(iter(old))  # one that failed the probe: never recovered, whatever its rate
    g = json.loads((run / "rejected" / leaky / "gates.json").read_text())
    g["solver_pass_rate"] = 1.0
    next(x for x in g["gates"] if x["name"] == "solver_check")["details"]["probe_without_documents_passed"] = True
    (run / "rejected" / leaky / "gates.json").write_text(json.dumps(g))

    assert relabel.main([str(run)]) == 0
    want = {m for m, r in old.items() if r == 1.0 and m != leaky}
    assert {p.parent.name for p in run.glob("rejected/*/task.json")} == want
    assert f"recovered {len(want)}" in capsys.readouterr().out
    for m in want:
        t = json.loads((run / "rejected" / m / "task.json").read_text())
        assert t["difficulty"] == [{"model": "fake", "attempts": 3, "passes": 3, "pass_rate": 1.0}] and t["split"] in ("train", "dev", "test")
    assert main(["export", "--runs", str(run), "--out", str(tmp_path / "x"), "--model", "fake", "--min-pass", "1.0"]) == 0
    assert sum(len((tmp_path / "x" / f"{s}.jsonl").read_text().splitlines()) for s in ("train", "dev", "test")) == len(want)


def test_run_refuses_a_seed_another_run_folder_used(tmp_path, capsys):
    a, b = str(tmp_path / "a"), str(tmp_path / "b")
    assert main(["run", "--out", a, "--seed", "5", "--matters", "1"]) == 0
    assert main(["run", "--out", b, "--seed", "5", "--matters", "1"]) == 2
    assert "seed 5 was already used by" in capsys.readouterr().err
    assert not (tmp_path / "b").exists()
    assert main(["run", "--out", a, "--seed", "5", "--matters", "1", "--resume"]) == 0  # the same folder is not another run
    assert main(["run", "--out", b, "--seed", "5", "--matters", "1", "--allow-seed-reuse"]) == 0
    assert main(["run", "--out", str(tmp_path / "c"), "--seed", "6", "--matters", "1"]) == 0
    assert main(["run", "--out", str(tmp_path / "d"), "--matters", "1"]) == 0  # the config's own seed is not checked


def test_drop_criteria_relabels_a_task_from_its_stored_grades(cfg, tmp_path):
    """T25 found criteria too strict in 7 unsolved tasks; dropping them relabels each task from the grades already
    stored in gates.json, with no model call."""
    import importlib.util

    import pytest

    spec = importlib.util.spec_from_file_location("drop", Path(__file__).resolve().parent.parent / "scripts" / "drop_criteria.py")
    drop = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(drop)

    Pipeline(cfg).run()
    run = Path(cfg.run.out_dir)
    m = sorted((run / "accepted").iterdir())[0]
    g = json.loads((m / "gates.json").read_text())  # make it unsolved: C2 failed every attempt, C3 one of them
    sc = next(x for x in g["gates"] if x["name"] == "solver_check")["details"]
    model = sc["difficulty"][0]["model"]
    for r, failed in zip(sc["runs"][model], (["C2"], ["C2", "C3"], ["C2"])):
        r.update({"passed": False, "failed_criteria": failed})
    unsolved = [{**sc["difficulty"][0], "passes": 0, "pass_rate": 0.0}]
    sc.update({"difficulty": unsolved, "pass_rate": 0.0, "unsolved": True})
    g.update({"difficulty": unsolved, "solver_pass_rate": 0.0, "unsolved": True})
    (m / "gates.json").write_text(json.dumps(g))
    task = json.loads((m / "task.json").read_text())
    task.update({"difficulty": unsolved, "solver_pass_rate": 0.0, "unsolved": True})
    (m / "task.json").write_text(json.dumps(task))
    before = (m / "rubric.json").read_text()

    old, new = drop.relabel(m, ["C2"], "test review")
    assert old[0]["passes"] == 0 and new[0]["passes"] == 2 and new[0]["pass_rate"] == 0.667
    assert (m / "rubric.original.json").read_text() == before
    assert "C2" not in {c["id"] for c in json.loads((m / "rubric.json").read_text())["criteria"]}
    t = json.loads((m / "task.json").read_text())
    assert "C2" not in {c["id"] for c in t["rubric"]} and t["relabelled"] == {"dropped": ["C2"], "by": "test review"}
    assert t["difficulty"] == new and t["unsolved"] is False and t["solver_pass_rate"] == 0.667
    g = json.loads((m / "gates.json").read_text())
    assert g["unsolved"] is False and next(x for x in g["gates"] if x["name"] == "solver_check")["details"]["runs"][model][1]["failed_criteria"] == ["C2", "C3"]
    with pytest.raises(SystemExit, match="already dropped"):
        drop.relabel(m, ["C2"], "test review")
    assert main(["export", "--runs", str(run), "--out", str(tmp_path / "x"), "--model", model, "--min-pass", "0.6", "--max-pass", "0.7"]) == 0
    assert any(json.loads(line)["eval"]["matter_id"] == m.name for line in (tmp_path / "x" / f"{t['split']}.jsonl").read_text().splitlines())
