# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 2 | 0 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 2 | 0 | 0 |
| decontamination | 2 | 0 | 0 | 2 |
| solver_check | 2 | 0 | 2 | 0 |

**Decontamination was skipped (no `reference_dirs`): these tasks were NOT screened against LAB.**

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s1-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F1", "key": "Effective Date", "filename": "mutual_nda.md", "ledger": "March 1, 2027", "document": "October 5, 2026"}] |
| s1-m0002 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s1-m0003 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 108606 | 27457 | 0 |
| drafter | 12 | 161057 | 64362 | 0 |
| fact_extractor | 3 | 70080 | 6712 | 0 |
| fact_matcher | 3 | 4380 | 940 | 0 |
| instruction_writer | 2 | 2762 | 758 | 0 |
| issue_verifier | 7 | 153408 | 2773 | 0 |
| judge | 14 | 124137 | 13689 | 0 |
| ledger_writer | 3 | 8356 | 12146 | 0 |
| rubric_writer | 2 | 9040 | 3686 | 0 |
| solver | 101 | 1176399 | 148079 | 0 |
