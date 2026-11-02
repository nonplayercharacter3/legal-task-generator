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
| s8-m0001 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s8-m0002 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s8-m0003 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |

## Variety

- Industries: medical imaging equipment (1), dental clinics (1), precision agriculture drones (1)
- Agreement types: stock purchase agreement (1), asset purchase agreement (1), supply agreement (1)
- Issue types: change_of_control_consent (2), defined_term_inconsistency (2), governing_law_mismatch (2), liability_cap_carveout (2), uncapped_indemnity (2), missing_assignment_restriction (1), survival_gap (1), expired_notice_window (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 205136 | 53903 | 0 |
| drafter | 15 | 265066 | 86873 | 0 |
| fact_extractor | 3 | 98388 | 8520 | 0 |
| fact_matcher | 2 | 2632 | 552 | 0 |
| instruction_writer | 3 | 4229 | 1194 | 0 |
| issue_verifier | 14 | 389653 | 8555 | 0 |
| judge | 21 | 207009 | 29563 | 0 |
| ledger_writer | 3 | 10920 | 21367 | 0 |
| rubric_writer | 3 | 16638 | 6683 | 0 |
| solver | 171 | 1517045 | 153448 | 0 |
