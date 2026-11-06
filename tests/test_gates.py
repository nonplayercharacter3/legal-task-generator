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
    for answer, ids in (("gold", g.details["gold_fails"]), ("flawed", g.details["flawed_wrongly_passes"])):
        assert set(g.details["judge_reasons"][answer]) == set(ids)  # a reason (here "": the stub gives none) for each


def test_solver_check_rejects_only_a_task_solvable_without_documents():
    always = Stub(lambda r, c: True)
    g, _ = gates.solver_check(always, "instr", {"a.md": "text"}, RUBRIC, attempts=3, probe_without_documents=True)
    assert not g.passed and "without opening any document" in g.details["reason"]
    g, _ = gates.solver_check(always, "instr", {"a.md": "text"}, RUBRIC, attempts=3, probe_without_documents=False)
    assert g.passed and g.details["pass_rate"] == 1.0 and not g.details["unsolved"]  # 3 of 3 is a label, not a defect
    never = Stub(lambda r, c: False)
    g, _ = gates.solver_check(never, "instr", {"a.md": "text"}, RUBRIC, attempts=3, probe_without_documents=True)
    assert g.passed and g.details["pass_rate"] == 0.0 and g.details["unsolved"]


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

    reworded = {"F1@a.md": "New York law", "F1@b.md": "New York law"}
    ok = gates.consistency(Facts(reworded, same=True), _ledger(), docs)
    assert ok.passed and ok.details["reworded"] == 2
    bad = gates.consistency(Facts(reworded, same=False), _ledger(), docs)
    assert not bad.passed and len(bad.details["mismatches"]) == 2

    missing = Facts({}, same=True)  # silent in its own document: rejected without asking the matcher
    g = gates.consistency(missing, _ledger(), docs)
    assert not g.passed and missing.matched == [] and g.details["mismatches"][0]["filename"] == "a.md"


def test_detect_terms_ignore_markdown_emphasis_and_curly_quotes():
    assert gates._plain('"Territory" means') in gates._plain('> "**Territory**" means the United States')
    assert gates._plain('"Territory" means') in gates._plain("“Territory” means the United States")
    assert gates._plain('"Territory" means') not in gates._plain("the Territory is")


def test_issue_check_finds_terms_through_markdown_bold():
    from ltg.schema import DocumentPlan, Issue, Ledger, Party

    class Yes:
        def complete(self, role, system, user):
            return json.dumps({"present": True, "evidence": "", "reason": "still actionable"})

    issue = Issue("I1", "defined_term_inconsistency", "x", "x", "D1", "2.1", ['"Territory" means'], "x")
    ledger = Ledger("m", "", [Party("P1", "A", "Buyer"), Party("P2", "B", "Seller")], [], [DocumentPlan("D1", "a.md", "amendment")], [issue])
    g = gates.issue_check(Yes(), ledger, {"a.md": '> "**Territory**" means the United States'})
    assert g.passed
    assert g.details["results"][0]["reason"] == "still actionable"  # the verifier's grounds are kept in gates.json


def test_consistency_asks_again_for_a_value_missed_in_its_own_document():
    class MissesFirst(Facts):  # the long first extraction misses F1; a focused second call finds it
        calls = 0

        def complete(self, role, system, user):
            if role == "fact_extractor":
                MissesFirst.calls += 1
                if MissesFirst.calls == 1:
                    return json.dumps({"facts": []})
                p = extract_input(user)
                assert [q["id"] for q in p["queries"]] == ["F1@a.md"] and [d["filename"] for d in p["documents"]] == ["a.md"]
            return super().complete(role, system, user)

    g = gates.consistency(MissesFirst({"F1@a.md": "State of New York"}, same=False), _ledger(), {"a.md": "...", "b.md": "..."})
    assert g.passed and MissesFirst.calls == 2
    still_missing = Facts({}, same=True)  # both calls come back empty: rejected
    assert not gates.consistency(still_missing, _ledger(), {"a.md": "...", "b.md": "..."}).passed


def test_consistency_tells_the_extractor_which_instrument_a_fact_belongs_to():
    seen = []

    class Spy(Facts):
        def complete(self, role, system, user):
            if role == "fact_extractor":
                seen.extend(extract_input(user)["queries"])
            return super().complete(role, system, user)

    gates.consistency(Spy({"F1@a.md": "State of New York"}, same=True), _ledger(), {"a.md": "...", "b.md": "..."})
    assert {q["filename"]: q["of"] for q in seen} == {"a.md": "agreement (a.md)", "b.md": "agreement (a.md)"}


def test_consistency_accepts_the_ledger_value_word_for_word_inside_its_own_document():
    fallback = "the Court of Chancery (or, if it lacks jurisdiction, the Superior Court)"
    ledger = _ledger()
    ledger.facts[0].value = "Court of Chancery"
    own = Facts({"F1@a.md": fallback}, same=False)
    assert gates.consistency(own, ledger, {"a.md": "...", "b.md": "..."}).passed and own.matched == []
    elsewhere = Facts({"F1@a.md": "Court of Chancery", "F1@b.md": fallback}, same=False)  # other documents still go to the matcher
    assert not gates.consistency(elsewhere, ledger, {"a.md": "...", "b.md": "..."}).passed
    digits = Facts({"F1@a.md": "130 days"}, same=False)
    ledger.facts[0].value = "30 days"
    assert not gates.consistency(digits, ledger, {"a.md": "...", "b.md": "..."}).passed  # whole words only


def test_consistency_accepts_a_trimmed_extraction_when_its_own_document_states_the_full_value():
    ledger = _ledger()
    ledger.facts[0].value = "exclusive jurisdiction of the courts in New York County"
    clause = "Each party submits to the exclusive jurisdiction of the courts in New York County."
    trimmed = Facts({"F1@a.md": "the courts in New York County"}, same=False)
    assert gates.consistency(trimmed, ledger, {"a.md": clause, "b.md": "..."}).passed and trimmed.matched == []
    nonexclusive = Facts({"F1@a.md": "the courts in New York County"}, same=False)  # the text really lacks "exclusive"
    assert not gates.consistency(nonexclusive, ledger, {"a.md": "Each party submits to the courts in New York County.", "b.md": "..."}).passed


def test_consistency_treats_a_fact_quoted_in_an_issue_description_as_planted_in_its_document():
    from ltg.schema import Issue

    ledger = _ledger()
    ledger.facts[0].value = "Fraud, breaches of Fundamental Representations, and Excluded Taxes"
    ledger.issues = [Issue("I1", "liability_cap_carveout", "x", "Section 8.5(b) carves out Fraud, breaches of Fundamental "
                           "Representations and Excluded Taxes; the escrow agreement keeps only Fraud.", "D2", "5.4", ["x"], "x")]
    narrowed = {"F1@a.md": ledger.facts[0].value, "F1@b.md": "claims for Fraud"}
    assert gates.consistency(Facts(narrowed, same=False), ledger, {"a.md": "...", "b.md": "..."}).passed
    ledger.issues[0].doc = "D1"  # the issue lives elsewhere: the conflict in b.md is not planted
    assert not gates.consistency(Facts(narrowed, same=False), ledger, {"a.md": "...", "b.md": "..."}).passed
    ledger.issues[0].doc, ledger.facts[0].value = "D2", "Fraud"  # too short to count as quoted
    assert not gates.consistency(Facts({"F1@a.md": "Fraud", "F1@b.md": "claims for willful misconduct"}, same=False), ledger,
                                 {"a.md": "...", "b.md": "..."}).passed



def test_consistency_treats_a_value_an_issue_in_that_document_says_it_changes_as_planted():
    """Round 14, s14-m0001: the side letter resets F5 to 100,000 lbs and its issue says so, but `contradicts` lists only F7."""
    from ltg.schema import Issue

    ledger = _ledger()
    ledger.facts[0].key, ledger.facts[0].value = "Supply Agreement Minimum Annual Commitment", "120,000 pounds of Products per Contract Year"
    ledger.issues = [Issue("I3", "defined_term_inconsistency", "x", "D3 Section 2 resets the Minimum Annual Commitment to 100,000 "
                           "pounds from Contract Year 2027. It also states that 'Products' means T-90 pelletized hops only.", "D2", "2",
                           ["x"], "x", contradicts="F7")]
    reset = {"F1@a.md": "120,000 pounds of Products per Contract Year", "F1@b.md": "100,000 pounds of Products per Contract Year"}
    docs = {"a.md": "...", "b.md": "..."}
    assert gates.consistency(Facts(reset, same=False), ledger, docs).passed
    other = {**reset, "F1@b.md": "90,000 pounds of Products per Contract Year"}  # a number the issue never names
    assert not gates.consistency(Facts(other, same=False), ledger, docs).passed
    ledger.issues[0].doc = "D1"  # the issue lives in the other document: b.md's value is not planted
    assert not gates.consistency(Facts(reset, same=False), ledger, docs).passed

def test_consistency_trusts_the_document_text_over_an_extractor_that_drops_a_qualifier():
    ledger = _ledger()
    ledger.facts[0].value = "courts located in Wilmington, Delaware, exclusively"
    docs = {"a.md": "16.2 Each Party submits to the **courts located in Wilmington, Delaware, exclusively**.", "b.md": "..."}
    dropped = Facts({"F1@a.md": "the courts located in Wilmington, Delaware"}, same=False)
    assert gates.consistency(dropped, ledger, docs).passed
    ledger.facts[0].value = "45 days"  # too short to trust a bare text match
    docs["a.md"] = "Buyer may object within 45 days."
    assert not gates.consistency(Facts({"F1@a.md": "30 days"}, same=False), ledger, docs).passed


def test_negative_criterion_names_one_plain_claim_and_a_gold_that_rejects_it_passes():
    """Round 13: the judge failed a gold answer that explicitly rejected the claim a double-negative criterion named."""
    from ltg import prompts
    from ltg.fake import FakeModel
    from ltg.stages import judge

    assert "Never stack negations" in prompts.RUBRIC_WRITER
    assert "rejecting it or warning against it is a pass" in prompts.JUDGE
    fake = FakeModel()
    claim = "SPA Section 11.5 restricts assignment of the TSA"
    fake._claims["The response claims that SPA Section 11.5 restricts assignment of the TSA."] = claim
    rubric = Rubric([Criterion("N1", f"The response claims that {claim}.", "negative", "I1")])
    rejects = "SPA Section 11.5 covers only the SPA. It would be wrong to say that SPA Section 11.5 restricts assignment of the TSA."
    asserts = "Good news: SPA Section 11.5 restricts assignment of the TSA, so no change is needed."
    assert judge(fake, rejects, rubric) == {"N1": True}
    assert judge(fake, asserts, rubric) == {"N1": False}
