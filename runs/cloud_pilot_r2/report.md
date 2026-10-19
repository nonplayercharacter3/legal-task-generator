# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

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
| solver_check | 2 | 1 | 1 | 0 |

**Decontamination was skipped (no `reference_dirs`): these tasks were NOT screened against LAB.**

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s2-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F2", "key": "Licensed Software", "filename": "software_license_agreement.md", "ledger": "Corvane Ledger Platform, version 7.x, in object  |
| s2-m0002 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s2-m0003 | accepted | train | 0.33 |  |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 116680 | 31978 | 0 |
| drafter | 14 | 219926 | 74179 | 0 |
| fact_extractor | 3 | 86028 | 7558 | 0 |
| fact_matcher | 3 | 5023 | 1220 | 0 |
| instruction_writer | 2 | 2939 | 736 | 0 |
| issue_verifier | 8 | 195910 | 4004 | 0 |
| judge | 14 | 170718 | 12668 | 0 |
| ledger_writer | 3 | 8571 | 13230 | 0 |
| rubric_writer | 2 | 9327 | 2645 | 0 |
| solver | 112 | 1506200 | 360189 | 0 |
