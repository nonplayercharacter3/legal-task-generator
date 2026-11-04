# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 3 | 0 | 0 |
| rubric_tests | 3 | 3 | 0 | 0 |
| decontamination | 3 | 3 | 0 | 0 |
| solver_check | 3 | 0 | 3 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s9-m0001 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s9-m0002 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s9-m0003 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |

## Variety

- Industries: commercial laundry services (1), architectural glass (1), dental clinics (1)
- Agreement types: stock purchase agreement (1), supply agreement (1), master services agreement (1)
- Issue types: expired_notice_window (3), change_of_control_consent (2), survival_gap (1), governing_law_mismatch (1), liability_cap_carveout (1), exclusivity_scope (1), auto_renewal (1), defined_term_inconsistency (1), missing_assignment_restriction (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 168342 | 50081 | 0 |
| drafter | 13 | 199763 | 69654 | 0 |
| fact_extractor | 3 | 78550 | 7333 | 0 |
| fact_matcher | 3 | 3864 | 1117 | 0 |
| instruction_writer | 3 | 4129 | 1144 | 0 |
| issue_verifier | 13 | 285848 | 8811 | 0 |
| judge | 21 | 230433 | 26794 | 0 |
| ledger_writer | 3 | 10943 | 25196 | 0 |
| rubric_writer | 3 | 16456 | 6291 | 0 |
| solver | 163 | 1676301 | 531858 | 0 |
