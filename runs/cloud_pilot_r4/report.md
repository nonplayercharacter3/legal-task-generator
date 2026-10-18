# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 1 | 2 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 0 | 0 | 1 |
| solver_check | 1 | 0 | 1 | 0 |

**Decontamination was skipped (no `reference_dirs`): these tasks were NOT screened against LAB.**

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s4-m0001 | rejected at leak_check |  |  | hits: [{"issue": "I3", "phrase": "Schedule 3.4", "in": "instruction"}, {"issue": "I3", "phrase": "Schedule 3.4", "in": "stock_purchase_agreement_excerpt_and_sch |
| s4-m0002 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s4-m0003 | rejected at leak_check |  |  | hits: [{"issue": "I1", "phrase": "Notice of Disagreement", "in": "instruction"}, {"issue": "I1", "phrase": "Notice of Disagreement", "in": "closing_statement_co |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 93300 | 17310 | 0 |
| drafter | 13 | 251763 | 92471 | 0 |
| fact_extractor | 3 | 102894 | 6425 | 0 |
| fact_matcher | 3 | 3907 | 698 | 0 |
| instruction_writer | 3 | 4802 | 1172 | 0 |
| issue_verifier | 9 | 269496 | 6872 | 0 |
| judge | 7 | 63916 | 5944 | 0 |
| ledger_writer | 3 | 9369 | 23863 | 0 |
| rubric_writer | 1 | 5466 | 1263 | 0 |
| solver | 82 | 1670933 | 76232 | 0 |
