# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 2 | 1 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 2 | 0 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 2 | 1 | 1 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s12-m0001 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s12-m0002 | rejected at issue_check |  |  | missing: ["I3"] |
| s12-m0003 | accepted | train | 0.33 |  |

## Variety

- Industries: battery recycling (1), industrial textiles (1), data center cooling (1)
- Agreement types: master services agreement (1), stock purchase agreement (1), distribution agreement (1)
- Issue types: change_of_control_consent (2), defined_term_inconsistency (2), expired_notice_window (2), missing_assignment_restriction (1), uncapped_indemnity (1), liability_cap_carveout (1), survival_gap (1), governing_law_mismatch (1), auto_renewal (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 109038 | 29452 | 0 |
| drafter | 13 | 204551 | 68896 | 0 |
| fact_extractor | 3 | 80996 | 7859 | 0 |
| fact_matcher | 2 | 2575 | 640 | 0 |
| instruction_writer | 2 | 2753 | 764 | 0 |
| issue_verifier | 13 | 289103 | 7269 | 0 |
| judge | 14 | 113200 | 12078 | 0 |
| ledger_writer | 3 | 11760 | 23844 | 0 |
| rubric_writer | 2 | 10716 | 2674 | 0 |
| solver | 98 | 665894 | 91274 | 0 |
