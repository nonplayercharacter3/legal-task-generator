# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 3 | 0 | 0 |
| rubric_tests | 3 | 3 | 0 | 0 |
| decontamination | 3 | 0 | 0 | 3 |
| solver_check | 3 | 2 | 1 | 0 |

**Decontamination was skipped (no `reference_dirs`): these tasks were NOT screened against LAB.**

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s5-m0001 | accepted | train | 0.67 |  |
| s5-m0002 | accepted | train | 0.33 |  |
| s5-m0003 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 167098 | 49488 | 0 |
| drafter | 12 | 184654 | 70767 | 0 |
| fact_extractor | 3 | 79344 | 6949 | 0 |
| fact_matcher | 3 | 4530 | 872 | 0 |
| instruction_writer | 3 | 4697 | 1150 | 0 |
| issue_verifier | 13 | 303297 | 8213 | 0 |
| judge | 21 | 255559 | 19551 | 0 |
| ledger_writer | 3 | 9981 | 19476 | 0 |
| rubric_writer | 3 | 16366 | 4217 | 0 |
| solver | 167 | 1844605 | 560007 | 0 |
