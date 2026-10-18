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
| s3-m0001 | accepted | dev | 0.67 |  |
| s3-m0002 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s3-m0003 | rejected at consistency |  |  | mismatches: [{"fact": "F5", "key": "SPA exclusive forum", "filename": "stock_purchase_agreement.md", "ledger": "Court of Chancery of the State of Delaware", "do |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 130724 | 30881 | 0 |
| drafter | 14 | 265658 | 98621 | 0 |
| fact_extractor | 3 | 109288 | 7660 | 0 |
| fact_matcher | 3 | 4991 | 1280 | 0 |
| instruction_writer | 2 | 3312 | 835 | 0 |
| issue_verifier | 9 | 234566 | 5674 | 0 |
| judge | 14 | 126327 | 14075 | 0 |
| ledger_writer | 3 | 9520 | 23278 | 0 |
| rubric_writer | 2 | 11528 | 4043 | 0 |
| solver | 117 | 1568329 | 146774 | 0 |
