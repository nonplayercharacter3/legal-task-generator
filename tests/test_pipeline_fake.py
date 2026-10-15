"""End-to-end runs with the fake model, including deliberate faults each gate must catch."""

import json

import pytest

from ltg import gates
from ltg.config import load_config
from ltg.fake import FakeModel
from ltg.orchestrator import Pipeline
from ltg.schema import Ledger

from .conftest import RecordingFake


def test_end_to_end_writes_tasks_and_report(cfg, read_json):
    report = Pipeline(cfg).run()
    out = cfg.run.out_dir
    assert report["candidates"] == 6
    assert report["errors"] == 0
    assert 0 < report["accepted"] < 6  # solver_skill 0.85 gives a mix of too easy, too hard and kept

    from pathlib import Path

    acc = sorted((Path(out) / "accepted").iterdir())
    assert len(acc) == report["accepted"]
    task = read_json(acc[0] / "task.json")
    assert task["split"] in ("train", "dev", "test")
    assert set(task["documents"]) == {p.name for p in (acc[0] / "docs").iterdir()}
    for f in ("spec.json", "ledger.json", "instruction.md", "rubric.json", "answers.json", "gates.json"):
        assert (acc[0] / f).exists(), f
    assert (Path(out) / "report.md").read_text().startswith("# Run report")
    assert not (Path(out) / "work").exists()

    calls = report["model_calls"]
    for role in ("ledger_writer", "drafter", "fact_extractor", "issue_verifier", "instruction_writer", "rubric_writer", "answer_writer", "judge", "solver"):
        assert calls[role]["calls"] > 0, role


@pytest.mark.parametrize(
    "fault, gate",
    [
        ("wrong_fact", "consistency"),
        ("conflicting_restatement", "consistency"),
        ("drop_issue", "issue_check"),
        ("untraceable_criterion", "rubric_trace"),
        ("weak_gold", "rubric_tests"),
    ],
)
def test_each_fault_is_caught_by_its_gate(tmp_path, fault, gate):
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 3, "seed": 11}, "fake": {"fault": fault}})
    report = Pipeline(cfg).run()
    assert report["accepted"] == 0
    assert {m["failed_gate"] for m in report["matters"]} == {gate}


def test_solver_band_rejects_too_easy_and_too_hard(tmp_path):
    easy = load_config(None, {"run": {"out_dir": str(tmp_path / "easy"), "n_matters": 3}, "fake": {"solver_skill": 1.0}})
    hard = load_config(None, {"run": {"out_dir": str(tmp_path / "hard"), "n_matters": 3}, "fake": {"solver_skill": 0.0}})
    for c, reason in ((easy, "too easy"), (hard, "too hard")):
        rep = Pipeline(c).run()
        assert rep["accepted"] == 0
        assert all(m["failed_gate"] == "solver_check" and reason in m["reason"] for m in rep["matters"])


def test_isolation_solver_and_instruction_writer_never_see_the_answer_key(cfg):
    fake = RecordingFake(seed=cfg.run.seed)
    Pipeline(cfg, client=fake).run(n=3)
    for p in fake.payloads["solver"]:
        assert set(p) == {"instruction", "documents"}
    for p in fake.payloads["instruction_writer"]:
        assert set(p) == {"matter", "files"}
        assert "issue_types" not in p["matter"]
    for p in fake.payloads["judge"]:
        assert set(p) == {"response", "criteria"}
    for p in fake.payloads["fact_extractor"]:  # gets the fact keys, never the expected values
        assert all(set(q) == {"id", "key", "filename"} for q in p["queries"])


def test_leak_check_flags_an_instruction_that_names_an_issue():
    fake = FakeModel(seed=1)
    spec = {"matter_id": "m", "practice_area": "commercial_contracts", "agreement_type": "supply agreement", "jurisdiction": "Delaware",
            "n_documents": 3, "issue_types": ["auto_renewal", "uncapped_indemnity"]}
    ledger = Ledger.from_dict(fake._ledger_writer({"spec": spec, "precedents": []}))
    assert gates.leak_check("Please review the supply agreement and send a memo.", ledger).passed
    leaky = gates.leak_check("Please check whether the automatic renewal clause hurts the client.", ledger)
    assert not leaky.passed and leaky.details["hits"][0]["issue"] == "I1"


def test_same_seed_same_result(tmp_path):
    reps = []
    for k in range(2):
        c = load_config(None, {"run": {"out_dir": str(tmp_path / str(k)), "n_matters": 4, "seed": 5}})
        reps.append(Pipeline(c).run()["matters"])
    assert reps[0] == reps[1]


def test_model_error_rejects_matter_without_crashing_run(tmp_path):
    class Broken(FakeModel):
        def _rubric_writer(self, p):
            raise RuntimeError("endpoint down")

    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2}})
    rep = Pipeline(cfg, client=Broken()).run()
    assert rep["errors"] == 2
    assert (tmp_path / "rejected" / rep["matters"][0]["matter_id"] / "error.txt").exists()


def test_decontamination_gate_rejects_copied_benchmark_text(tmp_path):
    # First run without a reference to get real generated documents...
    c1 = load_config(None, {"run": {"out_dir": str(tmp_path / "a"), "n_matters": 1, "seed": 9}, "fake": {"solver_skill": 0.5}})
    Pipeline(c1).run()
    matter = next((tmp_path / "a").glob("*/s9-m0001"))
    # ...then pretend those documents are a benchmark and rerun the same matter.
    c2 = load_config(None, {"run": {"out_dir": str(tmp_path / "b"), "n_matters": 1, "seed": 9},
                            "gates": {"reference_dirs": [str(matter / "docs")], "decontam_bloom_bits": 2**20}})
    rep = Pipeline(c2).run()
    assert rep["matters"][0]["failed_gate"] == "decontamination"


def test_invalid_ledger_is_rejected_after_one_repair_attempt(tmp_path):
    class BadLedger(FakeModel):
        def _ledger_writer(self, p):
            led = super()._ledger_writer(p)
            led["issues"] = led["issues"][:1]  # fewer issues than the spec asked for
            return led

    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2}})
    fake = BadLedger()
    rep = Pipeline(cfg, client=fake).run()
    assert {m["failed_gate"] for m in rep["matters"]} == {"ledger_schema"}
    assert rep["model_calls"]["ledger_writer"]["calls"] == 4  # first try + one repair, per matter


def test_rerun_into_same_folder_leaves_no_stale_verdicts(tmp_path):
    def run(**fake):
        return Pipeline(load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 6, "seed": 7}, "fake": fake})).run()

    assert run(solver_skill=0.85)["accepted"] > 0
    assert run(solver_skill=1.0)["accepted"] == 0  # every task now too easy
    assert not list((tmp_path / "accepted").iterdir())
    assert len(list((tmp_path / "rejected").iterdir())) == 6


def test_run_refuses_folder_with_matters_from_another_run(tmp_path):
    Pipeline(load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2, "seed": 7}})).run()
    with pytest.raises(FileExistsError, match="another run"):
        Pipeline(load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2, "seed": 8}})).run()


def test_consistency_allows_only_planted_contradictions():
    fake = FakeModel(seed=1)
    spec = {"matter_id": "m", "practice_area": "commercial_contracts", "agreement_type": "supply agreement", "jurisdiction": "Delaware",
            "n_documents": 3, "issue_types": ["auto_renewal", "governing_law_mismatch"]}
    ledger = Ledger.from_dict(fake._ledger_writer({"spec": spec, "precedents": []}))
    mismatch = next(i for i in ledger.issues if i.type == "governing_law_mismatch")
    docs = {d.filename: fake._drafter({"ledger": ledger.to_dict(), "document": d.__dict__}) for d in ledger.documents}
    other = next(d.filename for d in ledger.documents if d.id == mismatch.doc)
    docs[other] += "\nGoverning Law: State of California\n"

    assert gates.consistency(fake, ledger, docs).passed  # the planted issue contradicts F3 on purpose
    mismatch.contradicts = None
    g = gates.consistency(fake, ledger, docs)
    assert not g.passed and g.details["mismatches"][0]["filename"] == other
