# The 13 unsolved tasks of rounds 20 to 27: hard, or too strict?

Reviewed 2026-11-08 (inbox T25). Rounds 20 to 27 (seeds 20 to 27, main 81173a2) kept 23 tasks. In 13 of them
qwen3-small passed none of its three attempts, so they are marked `unsolved`. This note asks whether each one is
fair but hard, would be solvable with a looser criterion, or is broken.

## Method

- **Which criteria.** For each unsolved task, the criteria Qwen failed in all three attempts. Where no criterion
  failed in all three (s21-m0002, s24-m0001), the criteria it failed at least twice. That gives 16 criteria.
- **Referee.** One Opus call through the Claude Agent SDK per criterion, built the same way `scripts/judge_leniency.py`
  builds its referee (`configs/pilot_nrp_solver.toml`, role `referee`, default model). The referee saw the
  instruction, every document, the full ledger, the ledger entry the criterion traces to, the criterion, and all three
  memos. It answered `genuine_miss`, `too_strict` (and why) or `broken`, and for each memo whether it satisfies the
  criterion in substance, with a quote. The prompt is in the appendix.
- **Cost.** 16 calls, about 986k input and 12k output tokens, 0 errors. The script ran from the session scratchpad and
  is not in the repo; the replies are not committed.
- **Hand checks.** I checked four tasks by hand against the memos: s20-m0002, s23-m0002, s25-m0001 and s26-m0001,
  where a fact criterion asks for a whole precedence clause or the governing law. I agree with the referee on all four.
- **Limits.**
  - The referee is Opus, the same model family that wrote the rubrics, so this is not calibration against a lawyer.
  - For the two tasks picked by the "failed at least twice" rule, the prompt still said that all three memos failed
    the criterion. In s21-m0002 the referee therefore thought attempt 3 was failed "in error" on C3. In fact attempt 3
    passed C3 and failed only C2, which was not reviewed.

"Fails" below lists the failed criteria for attempts 1, 2 and 3.

## Per task

**s20-m0002** (MSA, outdoor apparel, run pilot20_nrp). Fails: C6 / C6 / C6.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C6 | fact | too_strict | Two facts in one: "amendments take precedence" and "the Service Level Schedule controls on service levels". Every memo states the second. The first does no work, because the amendment deletes and replaces MSA 2.4 outright. |

Checked by hand: each memo quotes MSA 17.3 on the Schedule and says nothing about amendments.

**s21-m0002** (supply agreement, independent film distribution, pilot21_nrp). Fails: C1, C3 / C3 / C2.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C3 | issue | genuine_miss | Supply Agreement 14.3 makes the Order Form control the Minimum Annual Commitment, so the narrow 1.1 definition governs the US$850,000 calculation. Attempts 1 and 2 misread 14.3 and conclude the opposite. |

**s21-m0003** (MSA, elevator maintenance, pilot21_nrp). Fails: C1, C2, C5, C7, C8 / C2, C5, C8, C12 / C2, C5.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C2 | issue | genuine_miss | MSA 1.14 defines Service Call as a call received during Business Hours, so after-hours entrapments fall outside the SOW's 30-minute commitment. No memo finds the definition. |
| C5 | issue | genuine_miss | Amendment 3.1 makes the anti-assignment clause one-sided. One memo half-notices it, one calls it favourable, one omits it. |

**s22-m0003** (SPA, medical imaging equipment, pilot22_nrp). Fails: C2 / C2 / C2, C6.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C2 | issue | too_strict | All three memos find Escrow Agreement 8.3, its conflict with SPA 9.5(e), the 11.9 precedence clause and a fix. The criterion also demands the Deferred Payment carve-out. That point is contestable: SPA 9.8 keeps direct claims for the Deferred Payment, and the ledger itself says it only "may" be capped. |

**s23-m0001** (distribution agreement, event furniture rental, pilot23_nrp). Fails: C5 / C5, C6, C7 / C5.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C5 | fact | too_strict | The cap's measure (amounts paid in the prior 12 months) is background. The finding is that 12.2 takes the defect indemnity out of the cap, and every memo makes that point without restating the formula. |

**s23-m0002** (MSA, seed genetics, pilot23_nrp). Fails: C5 / C5 / C5.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C5 | fact | too_strict | It asks for the full four-tier ranking. What matters here is that the MSA prevails over Order Form No. 4 unless the Order Form names the MSA section it overrides. All three memos apply that rule correctly. |

Checked by hand: each memo quotes the MSA 1.3 express-override sentence. None lists the four tiers.

**s24-m0001** (APA, elevator maintenance, pilot24_nrp). Fails: C6 / C1, C4 / C1.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C1 | issue | too_strict | It requires one route: the 90-day survival bar beats the 15-month escrow through APA 11.9 precedence. The memos reach the same conclusion through 9.1, since the escrow is only a source of recovery, and they recommend the right fix. |

**s24-m0002** (APA, precision agriculture drones, pilot24_nrp). Fails: C1 / C1, C6 / C1.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C1 | issue | genuine_miss | APA 2.3(b) makes pre- and post-Closing Assigned Contract liabilities Assumed Liabilities, and 9.5(c) exempts Buyer's 9.3 indemnity from the cap. No memo finds the resulting uncapped exposure. |

**s25-m0001** (distribution agreement, precision agriculture drones, pilot25_nrp). Fails: C3, C7 / C3, C7 / C3, C7.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C3 | issue | genuine_miss | The 11.2 breach indemnity, including lost profits, sits outside both the cap and the consequential-damages bar under 12.3(a). No memo treats it as the client's exposure. |
| C7 | fact | too_strict | New York governing law. None of the four issues turns on it, and nothing in the memos' advice needs it. |

Checked by hand: no memo states the governing law, and no ledger issue concerns it.

**s25-m0002** (supply agreement, seed genetics, pilot25_nrp). Fails: C1 / C1, C5 / C1, C5.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C1 | issue | genuine_miss | The 1.1 definitions stretch the 4.1 exclusivity and non-production covenant to every crop in the US and Canada, far beyond the hybrid-corn, Iowa and Illinois deal. Every memo treats exclusivity only as lock-in. |

**s26-m0001** (MSA, outdoor apparel, pilot26_nrp). Fails: C4, C6 / C4, C6, C9 / C4, C6.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C4 | issue | genuine_miss | 11.3 takes every Section 10 indemnity out of the cap, so the broad 10.2 product indemnity is unlimited. No memo connects the two, and one recommends keeping the carve-out. |
| C6 | fact | too_strict | It asks for the full three-tier ranking. All that matters is that the Order Form and the Service Level Schedule each outrank the MSA, and the memos state both. Nothing turns on Order Form against Schedule. |

Checked by hand: each memo states "the Order Form controls over the MSA", and two state "the SLS ranks above the MSA".

**s27-m0001** (SPA, organic dairy, pilot27_nrp). Fails: C3, C5 / C5 / C5.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C5 | issue | genuine_miss | TSA 12.3 incorporates SPA 12.4 mutatis mutandis, so Seller can assign the TSA, and the Company's data, to a competitor. No memo finds it. |

**s27-m0003** (SPA, elevator maintenance, pilot27_nrp). Fails: C1 / C1 / C1, C7.

| Criterion | Kind | Verdict | Reason |
| --- | --- | --- | --- |
| C1 | issue | genuine_miss | Buyer's 9.3(b) indemnity for post-Closing operations is uncapped under 9.5(c)(iii), while Seller is capped at $4.85M. No memo addresses Buyer's own indemnity. |

## Counts

Across the 16 criteria: 9 `genuine_miss`, 7 `too_strict`, 0 `broken`. Of the 11 issue criteria, 9 are genuine misses;
of the other two, one bundles a second point and one demands a route. All 5 fact criteria are too strict.

| Outcome | Tasks | Which |
| --- | ---: | --- |
| Fair but hard: every reviewed failure is `genuine_miss` | 6 | s21-m0002, s21-m0003, s24-m0002, s25-m0002, s27-m0001, s27-m0003 |
| Solvable with a looser criterion: at least one attempt would pass every criterion | 5 | s20-m0002 (3 of 3), s23-m0002 (3 of 3), s22-m0003 (2 of 3), s23-m0001 (2 of 3), s24-m0001 (1 of 3) |
| Hard, plus one too-strict fact criterion: still unsolved after loosening | 2 | s25-m0001, s26-m0001 |
| Broken | 0 | |

The second row's counts assume that the criterion, loosened or dropped as the referee's reason describes, passes every
memo, and that the other failures stay. So 8 of the 13 are genuinely unsolved by Qwen, and 5 are unsolved only
because of the rubric. Qwen's label on the kept tasks would move from 0.00: 13 to roughly 0.00: 8, 0.33: 7, 0.67: 2,
1.00: 6 (from 0.33: 6, 1.00: 4).

## Patterns for rubric-writer rules

1. **A fact criterion states one fact.** Never two in one criterion. Never a whole ranking, such as an order of
   precedence, when only one pair of it matters: ask for the pair the issues use, for example "the Order Form
   prevails over the MSA". Seen in s20-m0002 C6, s23-m0002 C5 and s26-m0001 C6.
2. **A fact criterion is a fact the memo's advice needs.** Background that no issue or recommendation turns on does
   not get a criterion, for example governing law when no issue concerns law or forum, or a cap's measure when the
   issue is a carve-out. Seen in s25-m0001 C7 and s23-m0001 C5. This complements T26 item 1: a fact only one issue
   uses is one problem; a fact no issue uses is the other.
3. **An issue criterion carries one finding.** A second, contestable point goes in its own issue or nowhere. Above
   all, nothing the ledger itself hedges ("may") belongs in the criterion. Seen in s22-m0003 C2.
4. **An issue criterion requires the conclusion, not one route.** That is already the rule (5c66350), and it still
   recurs: s24-m0001 C1 names the 11.9 precedence route. The judge prompt says any sound route passes, yet the
   judge failed the memos. The criterion text should name the conclusion only.

Also seen, outside this question: the s25-m0001 instruction lists Kestrova Agritech, the buyer in issue I4, among
"the other parties involved". Kestrova is not a detect term, so `leak_check` passed it, but it points a reader at the
issue. This is T22's class 4 (the instruction writer listing every ledger party).

## Appendix: referee prompt

```
You audit one rubric criterion of a legal-memo task. Three memos by the same model all failed it under the
grader. You see the partner's instruction, the matter documents, the answer key (the ledger) with the entry the
criterion traces to, the criterion, and the three memos. Decide which of these holds:
- "genuine_miss": a correct, thorough memo answering this instruction must say what the criterion asks, and these
  memos do not (they miss it, get it wrong, or say only part of what is needed).
- "too_strict": a sound memo could reasonably leave this out or say it differently and still be correct; name why
  (for example: the fact is incidental background, the criterion bundles two things, it demands one route or one
  wording, or the memos reach the same conclusion another way).
- "broken": the criterion or the documents are wrong (the criterion misstates the documents, the documents do not
  support it, or no memo could satisfy it).
For each memo also say whether it satisfies the criterion in substance, quoting the closest passage.

Reply with ONLY a JSON object: {"verdict": "genuine_miss"|"too_strict"|"broken", "reason": str (one or two sentences),
"memos": [{"attempt": int, "satisfies": bool, "quote": str}]}
```
