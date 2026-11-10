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
        ok = {c["id"]: self.grade(p["response"], c["id"]) for c in p["criteria"]}
        return json.dumps({"results": [{"id": c["id"], **({"claim_made": not ok[c["id"]]} if c["kind"] == "negative" else {"pass": ok[c["id"]]})} for c in p["criteria"]]})


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
    for answer, ids in (("gold", g.details["gold_fails"]), ("flawed", g.details["flawed_wrongly_passes"] + g.details["flawed_wrongly_fails"])):
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


def test_consistency_tells_the_matcher_which_instrument_numbers_each_value():
    """Round 14, s14-m0002: the term sheet names the agreement's cap carve-outs by its own section numbers."""
    from ltg import prompts

    ledger = _ledger()
    ledger.facts[0].key = "Distribution Agreement liability cap carve-outs"
    ledger.facts[0].value = "Supplier indemnity under Section 11.1, recall costs under Section 10.4, and fraud"
    ledger.documents[1].kind = "term sheet"
    term_sheet = "Supplier's third-party indemnity in Section 10.1; Supplier's recall cost obligations in Section 9.2; and fraud"
    seen = Facts({"F1@a.md": ledger.facts[0].value, "F1@b.md": term_sheet}, same=True)
    assert gates.consistency(seen, ledger, {"a.md": "...", "b.md": "..."}).passed
    assert seen.matched == [{"id": "0", "fact": ledger.facts[0].key, "ledger": ledger.facts[0].value, "ledger_in": "agreement (a.md)",
                             "document": term_sheet, "document_in": "term sheet (b.md)"}]
    assert "own numbering" in prompts.FACT_MATCHER and "not whether the numbers match" in prompts.FACT_MATCHER

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
    assert "rejecting it or warning against it is not making it" in prompts.JUDGE
    fake = FakeModel()
    claim = "SPA Section 11.5 restricts assignment of the TSA"
    rubric = Rubric([Criterion("N1", f"The response claims that {claim}.", "negative", "I1")])
    rejects = "SPA Section 11.5 covers only the SPA. It would be wrong to say that SPA Section 11.5 restricts assignment of the TSA."
    asserts = "Good news: SPA Section 11.5 restricts assignment of the TSA, so no change is needed."
    assert judge(fake, rejects, rubric) == {"N1": True}
    assert judge(fake, asserts, rubric) == {"N1": False}


def test_code_not_the_judge_grades_a_negative_criterion():
    """Round 15 (s15-m0003): the judge returned `pass: false` on negative criteria C8 and C9 while its reason said the
    flawed answer does not make the claim. The judge now reports `claim_made` and code derives the grade."""
    from ltg.stages import judge_with_reasons

    c8 = "The response claims that Wexcombe Dune Holdings LLC is a seller or co-seller of the hotel assets under the APA."
    c9 = (
        "The response claims that the APA's New York governing-law and forum clauses override the IP Assignment "
        "Agreement's Delaware clause for disputes under the IP Assignment."
    )
    rubric = Rubric([Criterion("C1", "finds I1", "issue", "I1"), Criterion("C8", c8, "negative", "F9"), Criterion("C9", c9, "negative", "I2")])
    flawed = (  # excerpts of the flawed answer in runs/pilot15_nrp/rejected/s15-m0003/answers.json
        "**Wexcombe Dune Holdings LLC** is not a seller or a party to the APA.\n"
        "On the text, Delaware law and the Chancery forum govern IP Assignment disputes, and the APA does not override them."
    )
    why = "The response does not make this claim; it says the opposite."

    class Judge:
        def __init__(self, reply):
            self.reply = reply

        def complete(self, role, system, user):
            assert "claim_made" in system and [c["kind"] for c in extract_input(user)["criteria"]] == ["issue", "negative", "negative"]
            return json.dumps({"results": self.reply})

    # Round 15's judge, as it answers now: the claims are not made, so C8 and C9 pass, whatever else it adds.
    grades, reasons = judge_with_reasons(Judge([{"id": "C1", "pass": True}, {"id": "C8", "claim_made": False, "pass": False, "reason": why}, {"id": "C9", "claim_made": False, "reason": why}]), flawed, rubric)
    assert grades == {"C1": True, "C8": True, "C9": True} and reasons["C8"] == why
    grades, _ = judge_with_reasons(Judge([{"id": "C1", "pass": True}, {"id": "C8", "claim_made": True}, {"id": "C9", "claim_made": True}]), flawed, rubric)
    assert grades == {"C1": True, "C8": False, "C9": False}
    # A bare `pass` on a negative criterion is the round 15 failure mode: it no longer counts, and the reason says so.
    grades, reasons = judge_with_reasons(Judge([{"id": "C1", "pass": True}, {"id": "C8", "pass": True, "reason": why}, {"id": "C9", "pass": False}]), flawed, rubric)
    assert grades == {"C1": True, "C8": False, "C9": False} and "no claim_made" in reasons["C8"]


def _fact_ledger():
    from ltg.schema import Ledger

    return Ledger.from_dict({
        "matter_id": "m", "summary": "s", "parties": [{"id": "P1", "name": "A", "role": "client"}],
        "documents": [{"id": "D1", "filename": "a.md", "kind": "main agreement"}],
        "facts": [
            # s16-m0001 F6: I1 restates it as "30 days after Seller delivers", so only its number matches
            {"id": "F6", "key": "Closing Statement dispute period", "value": "30 days after Seller's delivery of the Closing Statement", "doc": "D1", "section": "2.4(b)"},
            # s22-m0001 F10: I2 quotes the date
            {"id": "F10", "key": "Q3 2026 Quarterly Service Report delivery date", "value": "October 6, 2026", "doc": "D1", "section": "Annex B-1"},
            {"id": "F1", "key": "Purchase Price", "value": "$68,000,000", "doc": "D1", "section": "2.1"},
            {"id": "F2", "key": "Governing law", "value": "State of New York", "doc": "D1", "section": "20.1"},
        ],
        "issues": [
            {"id": "I1", "type": "t", "label": "late dispute notice", "doc": "D1", "section": "2.4(b)", "detect_terms": [],
             "description": "APA Section 2.4(b) gives Buyer 30 days after Seller delivers the Closing Statement. Price $68,000,000.",
             "expected_finding": "The Dispute Notice came after the window."},
            {"id": "I2", "type": "t", "label": "missed termination window", "doc": "D1", "section": "6.2", "detect_terms": [],
             "description": "The Q3 report was delivered on October 6, 2026; notice is due within fifteen days.",
             "expected_finding": "The termination right lapses unless exercised; see F1 for the price."},
        ],
    })


def test_rubric_trace_warns_about_a_fact_only_one_issue_uses():
    """s16-m0001 C4 and s22-m0001 C7: a fact criterion only the omitted issue's finding would state, so the flawed
    answer failed it and rubric_tests rejected the task. rubric_trace now records such criteria, without rejecting."""
    ledger = _fact_ledger()
    rubric = Rubric([Criterion("C1", "finds I1", "issue", "I1"), Criterion("C2", "finds I2", "issue", "I2"),
                     Criterion("C4", "states the 30-day period", "fact", "F6"), Criterion("C7", "states October 6, 2026", "fact", "F10"),
                     Criterion("C8", "states the price", "fact", "F1"), Criterion("C9", "states New York law", "fact", "F2")])
    g = gates.rubric_trace(rubric, ledger, Answers(gold="g", flawed="f", flawed_omits=["I2"]))
    assert g.passed
    flagged = g.details["single_issue_facts"]
    assert [w.split()[1] for w in flagged] == ["C4", "C7"]  # F1 is used by both issues (value, id), F2 by none
    assert "only issue I1" in flagged[0] and "only issue I2" in flagged[1]
    assert "Never a fact only one issue's finding would state" in prompts.RUBRIC_WRITER
    assert "Never two facts in one criterion" in prompts.RUBRIC_WRITER


def test_rubric_writer_carries_the_unsolved_review_rules_and_trace_warns_on_a_ranking():
    """docs/research/unsolved_review_2026-11.md: 5 of 13 unsolved tasks failed only on a criterion that was too strict.
    (a) a whole order of precedence as one fact (s23-m0002 C5, s26-m0001 C6, s20-m0002 C6); (b) background no issue
    turns on (s25-m0001 C7 governing law, s23-m0001 C5 a cap's measure); (c) a second, ledger-hedged point in an issue
    criterion (s22-m0003 C2); (d) a route instead of the conclusion (s24-m0001 C1). Only (a) can be checked in code."""
    rw = prompts.RUBRIC_WRITER
    assert "never a whole ranking or list when one pair of it" in rw  # (a)
    assert "never background no issue turns on" in rw and "governing law" in rw  # (b)
    assert "The finding is ONE finding" in rw and "the ledger\n  itself hedges" in rw  # (c)
    assert "Name the conclusion, never the route" in rw and "even when the expected finding gives that\n  route" in rw  # (d)

    from ltg.schema import Ledger

    def ledger(value):
        return Ledger.from_dict({"matter_id": "m", "summary": "s", "parties": [{"id": "P1", "name": "A", "role": "client"}],
                                 "documents": [{"id": "D1", "filename": "a.md", "kind": "main agreement"}],
                                 "facts": [{"id": "F2", "key": "Order of precedence", "value": value, "doc": "D1", "section": "1.3"}],
                                 "issues": [{"id": "I1", "type": "t", "label": "l", "description": "d", "doc": "D1", "section": "1",
                                             "detect_terms": [], "expected_finding": "e"}]})

    rubric = Rubric([Criterion("C1", "finds I1", "issue", "I1"), Criterion("C5", "states the order of precedence", "fact", "F2")])
    answers = Answers(gold="g", flawed="f", flawed_omits=["I1"])
    for value in ("MSA, then Quality Agreement, then Service Level Schedule, then Order Forms",  # s23-m0002 F2
                  "Amendments; then Service Level Schedule for service levels and service credits; then MSA body"):  # s20-m0002
        g = gates.rubric_trace(rubric, ledger(value), answers)
        assert g.passed and len(g.details["ranking_facts"]) == 1 and "C5" in g.details["ranking_facts"][0]
    pair = gates.rubric_trace(rubric, ledger("The Order Form prevails over the MSA"), answers)
    assert pair.details["ranking_facts"] == []


def test_issue_check_rejects_a_party_an_issue_needs_that_no_document_mentions():
    # s9-m0002: I1 rested on Besouth's sale to Pellworth Capital Partners, which no document named; the solver could
    # only take the name from the instruction. issue_check rejects it and names issue, party and name.
    from ltg.schema import DocumentPlan, Issue, Ledger, Party

    class Yes:
        def complete(self, role, system, user):
            return json.dumps({"present": True, "evidence": "", "reason": "ok"})

    issue = Issue("I1", "change_of_control", "x", "A sale of Besouth to Pellworth Capital Partners triggers 9.2.", "D1", "9.2",
                  ["change of control"], "Pellworth's purchase lets Lanmark terminate.")
    parties = [Party("P1", "Besouth Holdings LLC", "Seller"), Party("P2", "Lanmark Glass, Inc.", "Buyer"), Party("P3", "Pellworth Capital Partners", "Buyer")]
    ledger = Ledger("m", "", parties, [], [DocumentPlan("D1", "a.md", "supply agreement")], [issue])
    doc = "**BESOUTH** and Lanmark agree. 9.2 A change of control lets Lanmark terminate."
    g = gates.issue_check(Yes(), ledger, {"a.md": doc})
    assert not g.passed and g.details["absent_parties"] == [{"issue": "I1", "party": "P3", "name": "Pellworth Capital Partners"}]
    assert g.details["reason"] == "I1 needs party P3 (Pellworth Capital Partners), which no document mentions"
    g = gates.issue_check(Yes(), ledger, {"a.md": doc, "b.md": "Notice from Pellworth Capital, L.P."})
    assert g.passed and g.details["absent_parties"] == [] and "reason" not in g.details  # the stem in any document, case and punctuation ignored


def test_parties_absent_matches_a_common_word_stem_by_full_name():
    # T31's known false-hit risk: "The" or "First" as a stem would match almost any text.
    from ltg.schema import Ledger, Party

    ledger = Ledger("m", "", [Party("P1", "Besouth Holdings LLC", "Seller"), Party("P2", "First Harbor Bank, N.A.", "Lender")], [], [], [])
    docs = {"a.md": "Besouth Holdings LLC, the first party, shall notify the lender."}
    # "first" is in the folder, but the bank is not: still absent
    assert gates.parties_absent("Consent of First Harbor Bank, N.A. is needed.", ledger, docs) == [{"party": "P2", "name": "First Harbor Bank, N.A."}]
    # named by its full name in any document, case and punctuation ignored: mentioned
    assert gates.parties_absent("Consent of First Harbor Bank, N.A. is needed.", ledger, {**docs, "b.md": "FIRST HARBOR BANK N.A."}) == []
    # "first" alone in the text does not name the bank
    assert gates.parties_absent("The first notice was late.", ledger, {"a.md": "Besouth"}) == []
    # an ordinary stem still matches on the stem alone
    assert gates.parties_absent("Besouth must consent.", ledger, {"a.md": "First Harbor Bank, N.A."}) == [{"party": "P1", "name": "Besouth Holdings LLC"}]
