"""Gate logic tested directly, with a stub model, for branches the fake pipeline never reaches."""

import json

import pytest

from ltg import gates, prompts
from ltg.models import extract_input
from ltg.schema import Answers, Criterion, Rubric

RUBRIC = Rubric([Criterion("C1", "finds I1", "issue", "I1"), Criterion("C2", "finds I2", "issue", "I2"), Criterion("C3", "no fake law", "negative")])
ANSWERS = Answers(gold="GOLD", flawed="FLAWED", flawed_omits=["I2"])


class Stub:
    """Answers judge calls with grade(response, criterion_id) -> bool, and solver calls with a fixed answer."""

    def __init__(self, grade, answer="ANSWER"):
        self.grade, self.answer = grade, answer

    def complete(self, role, system, user):
        p = extract_input(user)
        if role == "solver":
            return '{"tool": "finish"}' if system == prompts.SOLVER_STEP else self.answer
        return json.dumps({"results": [{"id": c["id"], "pass": self.grade(p["response"], c["id"])} for c in p["criteria"]]})


def correct(response, cid):
    return {"GOLD": True, "": cid == "C3", "FLAWED": cid != "C2"}[response]


@pytest.mark.parametrize(
    "grade, failure",
    [
        (correct, None),
        (lambda r, c: False if (r, c) == ("GOLD", "C1") else correct(r, c), "gold_fails"),
        (lambda r, c: True if r == "" else correct(r, c), "blank_passes"),
        (lambda r, c: True if r == "FLAWED" else correct(r, c), "flawed_wrongly_passes"),
        (lambda r, c: False if (r, c) == ("FLAWED", "C1") else correct(r, c), "flawed_wrongly_fails"),
    ],
)
def test_rubric_tests_catches_each_kind_of_bad_rubric(grade, failure):
    g = gates.rubric_tests(Stub(grade), RUBRIC, ANSWERS)
    assert g.passed is (failure is None)
    flagged = {k for k in ("gold_fails", "blank_passes", "flawed_wrongly_passes", "flawed_wrongly_fails") if g.details[k]}
    assert flagged == ({failure} if failure else set())


def test_solver_check_rejects_a_task_solvable_without_documents():
    always = Stub(lambda r, c: True)
    g, _ = gates.solver_check(always, "instr", {"a.md": "text"}, RUBRIC, attempts=3, min_rate=0.01, max_rate=0.99, probe_without_documents=True)
    assert not g.passed and "without opening any document" in g.details["reason"]
    g, _ = gates.solver_check(always, "instr", {"a.md": "text"}, RUBRIC, attempts=3, min_rate=0.01, max_rate=0.99, probe_without_documents=False)
    assert not g.passed and "too easy" in g.details["reason"]


class Facts:
    """Extractor that returns fixed document values, and a matcher with fixed verdicts; records matcher calls."""

    def __init__(self, values, same):
        self.values, self.same, self.matched = values, same, []

    def complete(self, role, system, user):
        p = extract_input(user)
        if role == "fact_extractor":
            return json.dumps({"facts": [{"id": q["id"], "value": self.values.get(q["id"])} for q in p["queries"]]})
        self.matched += p["pairs"]
        return json.dumps({"results": [{"id": x["id"], "same": self.same} for x in p["pairs"]]})


def _ledger():
    from ltg.schema import DocumentPlan, Fact, Ledger, Party

    return Ledger("m", "", [Party("P1", "A", "Buyer"), Party("P2", "B", "Seller")],
                  [Fact("F1", "Governing Law", "State of New York", "D1", "12")],
                  [DocumentPlan("D1", "a.md", "agreement"), DocumentPlan("D2", "b.md", "amendment")], [])


def test_consistency_asks_the_matcher_only_about_reworded_values():
    docs = {"a.md": "...", "b.md": "..."}
    exact = Facts({"F1@a.md": "state of new york."}, same=False)
    assert gates.consistency(exact, _ledger(), docs).passed and exact.matched == []  # normalisation suffices

    reworded = {"F1@a.md": "the laws of the State of New York", "F1@b.md": "the laws of the State of New York"}
    ok = gates.consistency(Facts(reworded, same=True), _ledger(), docs)
    assert ok.passed and ok.details["reworded"] == 2
    bad = gates.consistency(Facts(reworded, same=False), _ledger(), docs)
    assert not bad.passed and len(bad.details["mismatches"]) == 2

    missing = Facts({}, same=True)  # silent in its own document: rejected without asking the matcher
    g = gates.consistency(missing, _ledger(), docs)
    assert not g.passed and missing.matched == [] and g.details["mismatches"][0]["filename"] == "a.md"
