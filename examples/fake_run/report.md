# Run report

Backend: `fake`. Accepted **8 of 20** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed |
| --- | ---: | ---: | ---: |
| ledger_schema | 20 | 20 | 0 |
| consistency | 20 | 18 | 2 |
| issue_check | 18 | 17 | 1 |
| leak_check | 17 | 17 | 0 |
| rubric_trace | 17 | 16 | 1 |
| rubric_tests | 16 | 13 | 3 |
| decontamination | 13 | 13 | 0 |
| solver_check | 13 | 8 | 5 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s7-m0001 | accepted | train | 0.67 |  |
| s7-m0002 | accepted | train | 0.67 |  |
| s7-m0003 | rejected at rubric_tests |  |  | gold_fails: ["C1"] |
| s7-m0004 | rejected at consistency |  |  | mismatches: [{"fact": "F1", "key": "Effective Date", "ledger": "2026-02-12", "document": "to be confirmed"}] |
| s7-m0005 | accepted | train | 0.67 |  |
| s7-m0006 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0007 | rejected at rubric_trace |  |  | errors: ["criterion C10 cites 'I99', which is not a ledger issue"] |
| s7-m0008 | rejected at consistency |  |  | mismatches: [{"fact": "F1", "key": "Effective Date", "ledger": "2026-03-13", "document": "to be confirmed"}] |
| s7-m0009 | rejected at issue_check |  |  | missing: ["I1"] |
| s7-m0010 | rejected at rubric_tests |  |  | gold_fails: ["C1"] |
| s7-m0011 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0012 | accepted | test | 0.67 |  |
| s7-m0013 | accepted | train | 0.67 |  |
| s7-m0014 | rejected at rubric_tests |  |  | gold_fails: ["C1"] |
| s7-m0015 | accepted | train | 0.67 |  |
| s7-m0016 | accepted | dev | 0.33 |  |
| s7-m0017 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s7-m0018 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s7-m0019 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0020 | accepted | train | 0.33 |  |

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 17 | 45061 | 11025 | 0 |
| drafter | 80 | 114028 | 14926 | 0 |
| fact_extractor | 20 | 15953 | 1180 | 0 |
| instruction_writer | 17 | 5904 | 2441 | 0 |
| issue_verifier | 77 | 33239 | 3588 | 0 |
| judge | 100 | 78534 | 10719 | 0 |
| ledger_writer | 20 | 22287 | 15722 | 0 |
| rubric_writer | 17 | 25726 | 6490 | 0 |
| solver | 52 | 40339 | 9346 | 0 |
