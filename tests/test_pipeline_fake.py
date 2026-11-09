"""End-to-end runs with the fake model, including deliberate faults each gate must catch."""

import json
from pathlib import Path

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
    assert report["accepted"] == 6  # the fake model drafts sound tasks; difficulty is a label, not a filter

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
    v = report["variety"]
    assert sum(v["industries"].values()) == 6 and len(v["industries"]) == 6  # one industry per matter
    assert v["repeated_names"] == {}  # every party starts with its own stem
    assert "## Variety" in (Path(out) / "report.md").read_text()

    calls = report["model_calls"]
    for role in ("ledger_writer", "drafter", "fact_extractor", "issue_verifier", "instruction_writer", "rubric_writer", "answer_writer", "judge", "solver"):
        assert calls[role]["calls"] > 0, role


@pytest.mark.parametrize(
    "fault, gate",
    [
        ("wrong_fact", "consistency"),
        ("conflicting_restatement", "consistency"),
        ("leaky_filename", "leak_check"),
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


def test_pass_rate_is_a_label_not_a_filter(tmp_path, read_json):
    easy = load_config(None, {"run": {"out_dir": str(tmp_path / "easy"), "n_matters": 3}, "fake": {"solver_skill": 1.0}})
    hard = load_config(None, {"run": {"out_dir": str(tmp_path / "hard"), "n_matters": 3}, "fake": {"solver_skill": 0.0}})
    for c, rate, unsolved in ((easy, 1.0, False), (hard, 0.0, True)):
        rep = Pipeline(c).run()
        assert rep["accepted"] == 3  # a 3-of-3 task is kept with its label; a 0-of-3 task is kept and flagged
        assert all(m["solver_pass_rate"] == rate and m["unsolved"] is unsolved for m in rep["matters"])
        task = read_json(Path(c.run.out_dir) / "accepted" / rep["matters"][0]["matter_id"] / "task.json")
        assert task["solver_pass_rate"] == rate and task["unsolved"] is unsolved
    assert "accepted (unsolved)" in (Path(hard.run.out_dir) / "report.md").read_text()


def test_isolation_solver_and_instruction_writer_never_see_the_answer_key(cfg):
    fake = RecordingFake(seed=cfg.run.seed)
    Pipeline(cfg, client=fake).run(n=3)
    drafted: dict[str, list[str]] = {}
    for d in Path(cfg.run.out_dir).glob("*/*/docs/*"):
        drafted.setdefault(d.name, []).append(d.read_text())
    reads = 0
    for p in fake.payloads["solver"]:
        assert set(p) in ({"instruction", "files", "steps", "steps_left"}, {"instruction", "files", "steps"})
        for st in p["steps"]:  # every tool result is text taken from a drafted document, nothing else
            if st["action"]["tool"] == "read_file":
                reads += 1
                assert any(st["result"].split("\n", 1)[1] in text for text in drafted[st["action"]["filename"]])
    assert reads > 0
    for p in fake.payloads["instruction_writer"]:
        assert set(p) == {"matter", "files"}
        assert "issue_types" not in p["matter"] and "jurisdiction" not in p["matter"]
    for p in fake.payloads["ledger_writer"]:  # the sampler, not the model, picks industry and name stems
        assert p["spec"]["industry"] and len(p["spec"]["name_stems"]) == 2 and "Halvorsen" in p["avoid_names"]
    for p in fake.payloads["judge"]:
        assert set(p) == {"response", "criteria"}
    for p in fake.payloads["fact_extractor"]:  # gets the fact keys, never the expected values
        assert all(set(q) == {"id", "key", "of", "filename"} for q in p["queries"])
    for p in fake.payloads["issue_verifier"]:  # judges blind; detect terms are checked in code
        assert "detect_terms" not in p["issue"]
        assert set(p["client"]) == {"name", "role"}  # whom an issue hurts depends on the client's side
    for p in fake.payloads["drafter"]:  # later drafts see earlier ones, never anything beyond the ledger
        assert set(p) == {"ledger", "document", "precedent", "drafted"}
        assert p["document"]["filename"] not in {d["filename"] for d in p["drafted"]}


def test_leak_check_flags_an_instruction_that_names_an_issue():
    fake = FakeModel(seed=1)
    spec = {"matter_id": "m", "practice_area": "commercial_contracts", "agreement_type": "supply agreement", "jurisdiction": "Delaware",
            "n_documents": 3, "issue_types": ["auto_renewal", "uncapped_indemnity"]}
    ledger = Ledger.from_dict(fake._ledger_writer({"spec": spec, "precedents": []}))
    clean = "Please review the supply agreement and send a memo."
    assert gates.leak_check(clean, ledger, {}).passed
    leaky = gates.leak_check("Please check whether the automatic-renewal clause hurts the client.", ledger, {})
    assert not leaky.passed and leaky.details["hits"][0]["issue"] == "I1"

    ledger.documents[1].filename = "automatic_renewal_letter.md"  # the solver sees filenames too
    assert not gates.leak_check(clean, ledger, {}).passed
    ledger.documents[1].filename = "side_letter.md"
    assert not gates.leak_check(clean, ledger, {"side_letter.md": "Text <!-- planted: I1 --> more"}).passed


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
                            "gates": {"reference_dirs": [str(matter / "docs")], "decontam_bloom_bits": 2**20,
                                      "decontam_cache_dir": str(tmp_path / "cache")}})
    rep = Pipeline(c2).run()
    assert rep["matters"][0]["failed_gate"] == "decontamination"
    assert rep["gates"]["decontamination"]["skipped"] == 0


def test_report_shows_decontamination_as_skipped_without_reference(cfg):
    rep = Pipeline(cfg).run()
    d = rep["gates"]["decontamination"]
    assert d["evaluated"] > 0 and d["skipped"] == d["evaluated"] and d["passed"] == 0
    from pathlib import Path

    assert "NOT screened against LAB" in (Path(cfg.run.out_dir) / "report.md").read_text()


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

    assert run(solver_skill=0.85)["accepted"] == 6
    assert run(fault="drop_issue")["accepted"] == 0  # every task now broken
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
    mismatch.contradicts = ["F1", "F3"]  # an issue may move several facts (governing law and forum)
    assert gates.consistency(fake, ledger, docs).passed
    mismatch.contradicts = None
    g = gates.consistency(fake, ledger, docs)
    assert not g.passed and g.details["mismatches"][0]["filename"] == other


def test_issue_check_needs_both_the_terms_and_the_verifier(tmp_path):
    class BlindVerifier(FakeModel):  # says every issue is present
        def _issue_verifier(self, p):
            return {"present": True, "evidence": "", "reason": ""}

    class SkepticalVerifier(FakeModel):  # says no issue is present
        def _issue_verifier(self, p):
            return {"present": False, "evidence": "", "reason": ""}

    dropped = load_config(None, {"run": {"out_dir": str(tmp_path / "a"), "n_matters": 2}, "fake": {"fault": "drop_issue"}})
    rep = Pipeline(dropped, client=BlindVerifier(fault="drop_issue")).run()
    assert {m["failed_gate"] for m in rep["matters"]} == {"issue_check"}  # detect terms missing from the document

    clean = load_config(None, {"run": {"out_dir": str(tmp_path / "b"), "n_matters": 2}})
    rep = Pipeline(clean, client=SkepticalVerifier()).run()
    assert {m["failed_gate"] for m in rep["matters"]} == {"issue_check"}  # terms present, verifier disagrees


def test_judge_without_hints_and_exported_rubric_matches_what_was_judged(tmp_path, read_json):
    for hints in (True, False):
        cfg = load_config(None, {"run": {"out_dir": str(tmp_path / str(hints)), "n_matters": 6, "seed": 7}, "gates": {"judge_hints": hints}})
        fake = RecordingFake(seed=7)
        rep = Pipeline(cfg, client=fake).run()
        assert rep["accepted"] > 0
        sent = any("grading_hints" in c for p in fake.payloads["judge"] for c in p["criteria"])
        assert sent is hints
        task = read_json(next((tmp_path / str(hints) / "accepted").iterdir()) / "task.json")
        assert all(bool(c["hints"]) is hints for c in task["rubric"] if c["kind"] != "negative")


def test_matters_run_concurrently_with_the_same_results(tmp_path):
    import threading
    import time

    class Slow(FakeModel):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            self.lock, self.active, self.peak = threading.Lock(), 0, 0

        def complete(self, role, system, user):
            with self.lock:
                self.active += 1
                self.peak = max(self.peak, self.active)
            time.sleep(0.002)
            try:
                return super().complete(role, system, user)
            finally:
                with self.lock:
                    self.active -= 1

    reps = {}
    for k in (1, 4):
        cfg = load_config(None, {"run": {"out_dir": str(tmp_path / str(k)), "n_matters": 6, "seed": 7, "concurrency": k}})
        slow = Slow(seed=7)
        reps[k] = Pipeline(cfg, client=slow).run()
        assert (slow.peak > 1) is (k > 1)
    assert reps[1]["matters"] == reps[4]["matters"]


class Crash(BaseException):
    """Stands in for the process dying: not an Exception, so no matter catches it."""


def _cfg(out, **gates):
    return load_config(None, {"run": {"out_dir": str(out), "n_matters": 6, "seed": 7, "concurrency": 1}, "gates": gates})


def test_resume_after_a_crash_skips_finished_matters(tmp_path):
    class CrashesOnFourth(FakeModel):
        def _ledger_writer(self, p):
            if p["spec"]["matter_id"].endswith("0004"):
                raise Crash()
            return super()._ledger_writer(p)

    with pytest.raises(Crash):
        Pipeline(_cfg(tmp_path / "a"), client=CrashesOnFourth(seed=7)).run()
    finished = {p.parent.name for p in (tmp_path / "a").glob("*/*/gates.json")}
    assert {"s7-m0001", "s7-m0002", "s7-m0003"} <= finished and "s7-m0004" not in finished
    fake = RecordingFake(seed=7)
    rep = Pipeline(_cfg(tmp_path / "a"), client=fake).run(resume=True)
    rerun = {p["spec"]["matter_id"] for p in fake.payloads["ledger_writer"]}
    assert rep["resumed"] == len(finished) and rerun == {f"s7-m000{k}" for k in range(1, 7)} - finished
    assert rep["matters"] == Pipeline(_cfg(tmp_path / "b")).run()["matters"]  # same as a run that never crashed


def test_resume_retries_matters_that_errored(tmp_path):
    class Down(FakeModel):
        def _judge(self, p):
            raise RuntimeError("endpoint down")

    assert Pipeline(_cfg(tmp_path), client=Down(seed=7)).run()["errors"] > 0
    rep = Pipeline(_cfg(tmp_path)).run(resume=True)
    assert rep["errors"] == 0 and rep["resumed"] < 6  # matters rejected before the judge was needed are kept
    # Seed 27 (2026-11-07): the resume overwrote the failed try's report and calls, so its errors were lost.
    first = tmp_path / "tries" / "1"
    before = json.loads((first / "report.json").read_text())
    assert before["errors"] > 0 and any("endpoint down" in (m["reason"] or "") for m in before["matters"])
    assert (first / "calls.jsonl").exists()
    Pipeline(_cfg(tmp_path)).run(resume=True)
    assert json.loads((tmp_path / "tries" / "2" / "report.json").read_text())["errors"] == 0


def test_resume_refuses_changed_settings(tmp_path):
    Pipeline(_cfg(tmp_path)).run()
    with pytest.raises(ValueError, match="settings changed"):
        Pipeline(_cfg(tmp_path, solver_attempts=5)).run(resume=True)
    rep = Pipeline(load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 8, "seed": 7, "concurrency": 2}})).run(resume=True)
    assert rep["resumed"] == 6 and rep["candidates"] == 8  # more matters and other concurrency are fine


def test_several_models_label_each_task(tmp_path, read_json):
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2, "seed": 7}, "gates": {"solver_models": ["solver", "solver_b"]}})
    rep = Pipeline(cfg).run()
    assert rep["accepted"] == 2 and set(rep["difficulty"]) == {"solver", "solver_b"}  # the fake has no model id: the role names it
    for m in rep["matters"]:
        folder = tmp_path / "accepted" / m["matter_id"]
        task = read_json(folder / "task.json")
        assert [d["model"] for d in task["difficulty"]] == ["solver", "solver_b"]
        assert all(set(d) == {"model", "attempts", "passes", "pass_rate"} and d["attempts"] == 3 for d in task["difficulty"])
        assert task["solver_pass_rate"] == task["difficulty"][0]["pass_rate"]
        assert (folder / "solver" / "attempt_3.md").exists() and (folder / "solver" / "solver_b" / "attempt_3.md").exists()
    assert "| solver_b |" in (tmp_path / "report.md").read_text()


def test_role_router_names_the_model_behind_a_labelling_role():
    from ltg.models import OpenAICompatClient, RoleRouter

    qwen = OpenAICompatClient(base_url="http://x/v1", default_model="qwen3-small", api_key_env="NONE")
    router = RoleRouter(FakeModel(), {"solver": qwen}, qwen.log)
    assert router.model_for("solver") == "qwen3-small" and router.model_for("solver_b") == ""


def test_bundled_issue_criterion_is_repaired_once_not_rejected(tmp_path, read_json):
    """T11b: a rubric whose only fault is a bundled harm or remedy clause goes back to its writer once."""
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2}, "fake": {"fault": "bundled_criterion"},
                             "gates": {"check_bundling": "repair"}})
    rep = Pipeline(cfg).run()
    assert rep["accepted"] == 2
    assert rep["model_calls"]["rubric_writer"]["calls"] == 4  # first draft + one repair, per matter
    assert rep["rubric_repairs"] == {"ran": 2, "cleared": 2, "bundled_after": 0}
    assert "2 repair(s) ran, 2 cleared" in (Path(tmp_path) / "report.md").read_text()
    trace = next(g for g in read_json(Path(tmp_path) / "accepted" / rep["matters"][0]["matter_id"] / "gates.json")["gates"] if g["name"] == "rubric_trace")
    assert trace["details"]["repair"]["ran"] and trace["details"]["repair"]["cleared"]
    assert len(trace["details"]["repair"]["flagged"]) == 1 and "yield data" in trace["details"]["repair"]["flagged"][0]
    assert trace["details"]["bundled"] == [] and trace["details"]["errors"] == []
    clean = Pipeline(load_config(None, {"run": {"out_dir": str(tmp_path / "clean"), "n_matters": 2}, "gates": {"check_bundling": "repair"}})).run()
    assert clean["model_calls"]["rubric_writer"]["calls"] == 2 and clean["rubric_repairs"]["ran"] == 0


class _StubbornWriter(FakeModel):
    """Keeps the bundled clause even when sent the rubric back."""

    def _rubric_writer(self, p):
        return super()._rubric_writer({**p, "previous_rubric": None})


def test_bundling_the_writer_cannot_correct_rejects_at_rubric_trace(tmp_path, read_json):
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2}, "fake": {"fault": "bundled_criterion"},
                             "gates": {"check_bundling": "repair"}})
    rep = Pipeline(cfg, client=_StubbornWriter(fault="bundled_criterion")).run()
    assert {m["failed_gate"] for m in rep["matters"]} == {"rubric_trace"}
    assert rep["model_calls"]["rubric_writer"]["calls"] == 4
    assert rep["rubric_repairs"] == {"ran": 2, "cleared": 0, "bundled_after": 2}
    trace = read_json(Path(tmp_path) / "rejected" / rep["matters"][0]["matter_id"] / "gates.json")["gates"][-1]
    assert trace["name"] == "rubric_trace" and trace["details"]["repair"]["ran"] and not trace["details"]["repair"]["cleared"]
    assert trace["details"]["bundled"] and trace["details"]["errors"] == trace["details"]["bundled"]


def test_other_rubric_faults_reject_at_once_without_a_repair_call(tmp_path):
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2}, "fake": {"fault": "untraceable_criterion"}})
    rep = Pipeline(cfg).run()
    assert {m["failed_gate"] for m in rep["matters"]} == {"rubric_trace"}
    assert rep["model_calls"]["rubric_writer"]["calls"] == 2 and rep["rubric_repairs"]["ran"] == 0


def test_check_bundling_warn_only_records_and_off_skips(tmp_path, read_json):
    assert load_config(None).gates.check_bundling == "warn"  # the default since round 13
    for mode in ("warn", "off"):
        cfg = load_config(None, {"run": {"out_dir": str(tmp_path / mode), "n_matters": 2}, "fake": {"fault": "bundled_criterion"},
                                 "gates": {"check_bundling": mode}})
        rep = Pipeline(cfg, client=_StubbornWriter(fault="bundled_criterion")).run()
        assert rep["accepted"] == 2, mode
        assert rep["model_calls"]["rubric_writer"]["calls"] == 2, mode  # no repair call in either mode
        trace = next(g for g in read_json(Path(tmp_path) / mode / "accepted" / rep["matters"][0]["matter_id"] / "gates.json")["gates"] if g["name"] == "rubric_trace")
        assert trace["details"]["repair"] == {"ran": False} and trace["details"]["errors"] == []
        assert (len(trace["details"]["bundled"]) == 1) is (mode == "warn")
        assert rep["rubric_repairs"]["bundled_after"] == (2 if mode == "warn" else 0)
        assert ("2 matter(s) flagged" in (tmp_path / mode / "report.md").read_text()) is (mode == "warn")
    with pytest.raises(ValueError, match="check_bundling"):
        load_config(None, {"gates": {"check_bundling": "maybe"}})


def test_rubric_tests_keeps_the_judges_reason_for_a_gold_failure(tmp_path, read_json):
    """Round 13: the judge failed s13-m0001's gold on C8 and nothing on disk said why."""
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2, "seed": 11}, "fake": {"fault": "weak_gold"}})
    rep = Pipeline(cfg).run()
    assert {m["failed_gate"] for m in rep["matters"]} == {"rubric_tests"}
    g = read_json(Path(tmp_path) / "rejected" / rep["matters"][0]["matter_id"] / "gates.json")["gates"][-1]
    d = g["details"]
    assert g["name"] == "rubric_tests" and d["gold_fails"]
    assert set(d["judge_reasons"]["gold"]) == set(d["gold_fails"]) and all(d["judge_reasons"]["gold"].values())
    assert d["judge_reasons"]["flawed"] == {}


def test_a_new_run_avoids_industries_earlier_runs_beside_it_used(tmp_path):
    """Rounds 20 to 27: elevator maintenance came up 3 times in one night, because each run reshuffled all 30
    industries on its own. A run now puts the industries its sibling run folders (same backend kind) used last."""
    from ltg.orchestrator import industries_used_beside

    first = Pipeline(_cfg(tmp_path / "r1")).run()
    used = set(first["variety"]["industries"])
    (tmp_path / "other").mkdir()  # another backend's run is ignored
    (tmp_path / "other" / "settings.json").write_text(json.dumps({"backend": {"kind": "claude_sdk"}}))
    assert industries_used_beside(tmp_path / "r2", "fake") == {i: 1 for i in used}
    cfg2 = load_config(None, {"run": {"out_dir": str(tmp_path / "r2"), "n_matters": 6, "seed": 7}})
    second = Pipeline(cfg2).run()
    assert not used & set(second["variety"]["industries"])  # same seed, but none of r1's industries
    saved = (tmp_path / "r2" / "industries_before.json").read_text()
    Pipeline(_cfg(tmp_path / "r3")).run()  # a later run changes the history beside r2 ...
    Pipeline(cfg2).run(resume=True)  # ... but a resume keeps the history r2 saved, so it samples the same specs
    assert (tmp_path / "r2" / "industries_before.json").read_text() == saved


def test_calls_log_grows_as_calls_end_and_a_killed_try_keeps_it(tmp_path):
    # Seed 28 (2026-11-09): the run was killed after 110 minutes and its calls.jsonl, written only at the end, was lost.
    class CrashesOnFourth(FakeModel):
        def _ledger_writer(self, p):
            if p["spec"]["matter_id"].endswith("0004"):
                raise Crash()
            return super()._ledger_writer(p)

    killed = CrashesOnFourth(seed=7)
    with pytest.raises(Crash):
        Pipeline(_cfg(tmp_path), client=killed).run()
    lines = (tmp_path / "calls.jsonl").read_text().splitlines()
    assert len(lines) == len(killed.log.records) > 0 and not (tmp_path / "report.json").exists()
    Pipeline(_cfg(tmp_path)).run(resume=True)
    assert (tmp_path / "tries" / "1" / "calls.jsonl").read_text().splitlines() == lines
    assert not (tmp_path / "tries" / "1" / "report.json").exists()
    rep = json.loads((tmp_path / "report.json").read_text())
    assert len((tmp_path / "calls.jsonl").read_text().splitlines()) == sum(r["calls"] for r in rep["model_calls"].values())


def test_run_log_has_a_heartbeat_per_stage_and_solver_attempt(tmp_path, capsys):
    # Seed 28 (2026-11-09): nothing in the batch log showed which stage two matters were stuck in for 50 minutes.
    Pipeline(load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 1, "seed": 7}})).run()
    lines = [ln.split(" ", 3)[3] for ln in capsys.readouterr().err.splitlines() if " s7-m0001 " in ln]
    assert lines[:3] == ["ledger", "documents", "consistency"]
    assert {"rubric_tests", "solver_check solver probe without documents", "solver_check solver attempt 3 of 3"} <= set(lines)
    assert lines[-1] in ("accepted", "rejected at solver_check")


GENERATION_ROLES = ("ledger_writer", "drafter", "instruction_writer", "rubric_writer", "answer_writer")


def test_resume_reuses_the_generation_of_a_matter_that_errored_in_solver_check(tmp_path, read_json):
    # Seed 28 (2026-11-09): a solver call on NRP timed out, and the resume redid the matter's whole Opus generation.
    class SolverDown(FakeModel):
        def _solver(self, p):
            raise RuntimeError("NRP silent")

    first = Pipeline(_cfg(tmp_path / "a"), client=SolverDown(seed=7)).run()
    errored = {m["matter_id"] for m in first["matters"] if m["failed_gate"] == "error"}
    assert errored and all("NRP silent" in m["reason"] for m in first["matters"] if m["matter_id"] in errored)
    for m in errored:
        assert read_json(tmp_path / "a" / "rejected" / m / "stages_done.json")["stages"] == ["ledger", "documents", "instruction", "rubric", "answers"]
    fake = RecordingFake(seed=7)
    rep = Pipeline(_cfg(tmp_path / "a"), client=fake).run(resume=True)
    regenerated = {p.get("spec", p.get("ledger", {})).get("matter_id") for r in GENERATION_ROLES for p in fake.payloads.get(r, [])}
    assert not regenerated & errored and fake.payloads["solver"] and rep["errors"] == 0
    assert rep["matters"] == Pipeline(_cfg(tmp_path / "b")).run()["matters"]  # the verdict of a run that never failed
    assert not (tmp_path / "a" / "accepted" / sorted(errored)[0] / "error.txt").exists()


def test_resume_regenerates_a_matter_whose_stage_never_completed(tmp_path):
    class DraftsDown(FakeModel):
        def _drafter(self, p):
            raise RuntimeError("down")

    Pipeline(_cfg(tmp_path), client=DraftsDown(seed=7)).run()
    fake = RecordingFake(seed=7)
    Pipeline(_cfg(tmp_path), client=fake).run(resume=True)
    assert not fake.payloads.get("ledger_writer") and fake.payloads["drafter"]  # ledger reused, documents redone
