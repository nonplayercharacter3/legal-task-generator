import copy

from ltg.config import SpecCfg
from ltg.fake import FakeModel
from ltg.models import render_input
from ltg.schema import Ledger, Rubric, validate_ledger, validate_rubric
from ltg.stages import sample_specs


def _ledger_and_spec(n_docs=4, n_issues=3):
    cfg = SpecCfg(n_documents=[n_docs, n_docs], n_issues=[n_issues, n_issues])
    spec = sample_specs(cfg, 1, seed=3)[0]
    fake = FakeModel(seed=3)
    raw = fake._ledger_writer({"spec": spec.to_dict(), "precedents": []})
    return Ledger.from_dict(raw), spec


def test_fake_ledger_is_valid():
    ledger, spec = _ledger_and_spec()
    assert validate_ledger(ledger, spec) == []


def test_ledger_catches_structural_errors():
    ledger, spec = _ledger_and_spec()
    bad = copy.deepcopy(ledger)
    bad.issues[0].doc = "D99"
    distractor = next(d for d in bad.documents if d.distractor)
    bad.issues[1].doc = distractor.id
    bad.documents[0].filename = "../escape.md"
    bad.facts.append(copy.deepcopy(bad.facts[0]))  # duplicate id
    errs = "\n".join(validate_ledger(bad, spec))
    assert "unknown document D99" in errs
    assert "distractor document" in errs
    assert "unsafe filename" in errs
    assert "duplicate id F1" in errs


def test_ledger_counts_must_match_spec():
    ledger, spec = _ledger_and_spec()
    ledger.issues = ledger.issues[:1]
    assert any("expected 3 issues" in e for e in validate_ledger(ledger, spec))


def test_ledger_tolerates_extra_keys():
    ledger, _ = _ledger_and_spec()
    d = ledger.to_dict()
    d["parties"][0]["notes"] = "extra key a model might add"
    assert Ledger.from_dict(d).parties[0].name == ledger.parties[0].name


def test_rubric_must_trace_to_ledger_and_cover_every_issue():
    ledger, _ = _ledger_and_spec()
    fake = FakeModel(seed=3)
    rubric = Rubric.from_dict(fake._rubric_writer({"ledger": ledger.to_dict()}))
    assert validate_rubric(rubric, ledger) == []

    rubric.criteria = [c for c in rubric.criteria if c.source != "I2"]
    rubric.criteria[0].source = "I99"
    errs = "\n".join(validate_rubric(rubric, ledger))
    assert "I99" in errs and "issue I2 has no criterion" in errs


def test_render_input_round_trips():
    from ltg.models import extract_input

    payload = {"a": [1, "two"], "b": {"c": "ünïcode"}}
    assert extract_input("preamble\n" + render_input(payload) + "\ntrailer") == payload


def test_contradiction_must_target_a_fact_in_another_document():
    ledger, spec = _ledger_and_spec()
    issue, fact = ledger.issues[0], ledger.facts[0]
    issue.contradicts, issue.doc = fact.id, fact.doc
    assert any("contradicts F1 inside" in e for e in validate_ledger(ledger, spec))
    issue.doc = next(d.id for d in ledger.documents if d.id != fact.doc and not d.distractor)
    assert not any("contradicts" in e for e in validate_ledger(ledger, spec))


def test_fact_values_must_be_short_values_not_clauses():
    ledger, spec = _ledger_and_spec()
    ledger.facts[0].value = " ".join(["word"] * 21)
    assert any("fact F1 is 21 words" in e for e in validate_ledger(ledger, spec))
    ledger.facts[0].value = "30 days"
    assert validate_ledger(ledger, spec) == []


def test_negative_criteria_may_not_target_a_distractor():
    ledger, _ = _ledger_and_spec()
    distractor = next(d for d in ledger.documents if d.distractor)
    crits = [{"id": f"C{k + 1}", "text": f"finds {i.id}", "kind": "issue", "source": i.id} for k, i in enumerate(ledger.issues)]
    ok = Rubric.from_dict({"criteria": crits + [{"id": "N1", "text": "Does not cite case law absent from the documents.", "kind": "negative"}]})
    assert validate_rubric(ok, ledger) == []
    name = distractor.filename.rsplit(".", 1)[0].replace("_", " ")
    bad = Rubric.from_dict({"criteria": crits + [{"id": "N1", "text": f"Fails if it flags the {name} as a problem.", "kind": "negative"}]})
    assert any("distractor" in e for e in validate_rubric(bad, ledger))
