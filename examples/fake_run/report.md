# Run report

Backend: `fake`. Accepted **7 of 20** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 20 | 20 | 0 | 0 |
| consistency | 20 | 17 | 3 | 0 |
| issue_check | 17 | 16 | 1 | 0 |
| leak_check | 16 | 14 | 2 | 0 |
| rubric_trace | 14 | 13 | 1 | 0 |
| rubric_tests | 13 | 12 | 1 | 0 |
| decontamination | 12 | 0 | 0 | 12 |
| solver_check | 12 | 7 | 5 | 0 |

**Decontamination was skipped (no `reference_dirs`): these tasks were NOT screened against LAB.**

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s7-m0001 | rejected at rubric_tests |  |  | gold_fails: ["C1"] |
| s7-m0002 | accepted | train | 0.67 |  |
| s7-m0003 | rejected at leak_check |  |  | hits: [{"issue": "I1", "phrase": "change of control consent", "in": "instruction"}, {"issue": "I1", "phrase": "change of control", "in": "instruction"}, {"issue |
| s7-m0004 | rejected at consistency |  |  | mismatches: [{"fact": "F1", "key": "Effective Date", "filename": "master_services_agreement.md", "ledger": "2026-02-12", "document": "to be confirmed"}] |
| s7-m0005 | accepted | train | 0.67 |  |
| s7-m0006 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0007 | rejected at consistency |  |  | mismatches: [{"fact": "F1", "key": "Effective Date", "filename": "amendment_1.md", "ledger": "2026-08-10", "document": "2026-08-10 (as revised)"}] |
| s7-m0008 | rejected at consistency |  |  | mismatches: [{"fact": "F1", "key": "Effective Date", "filename": "stock_purchase_agreement.md", "ledger": "2026-03-13", "document": "to be confirmed"}] |
| s7-m0009 | rejected at issue_check |  |  | missing: ["I1"] |
| s7-m0010 | rejected at leak_check |  |  | hits: [{"issue": "I1", "phrase": "overbroad exclusivity", "in": "instruction"}, {"issue": "I1", "phrase": "overbroad exclusivity", "in": "overbroad_exclusivity_ |
| s7-m0011 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0012 | accepted | test | 0.67 |  |
| s7-m0013 | accepted | train | 0.67 |  |
| s7-m0014 | rejected at rubric_trace |  |  | errors: ["criterion C9 cites 'I99', which is not a ledger issue"] |
| s7-m0015 | accepted | train | 0.67 |  |
| s7-m0016 | accepted | dev | 0.33 |  |
| s7-m0017 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s7-m0018 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s7-m0019 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0020 | accepted | train | 0.33 |  |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 28 | 73298 | 8523 | 0 |
| drafter | 80 | 119192 | 13082 | 0 |
| fact_extractor | 20 | 31329 | 6285 | 0 |
| instruction_writer | 16 | 5566 | 2308 | 0 |
| issue_verifier | 71 | 28608 | 3340 | 0 |
| judge | 87 | 67251 | 9272 | 0 |
| ledger_writer | 20 | 23517 | 16184 | 0 |
| rubric_writer | 14 | 21266 | 5233 | 0 |
| solver | 231 | 202382 | 10648 | 0 |
