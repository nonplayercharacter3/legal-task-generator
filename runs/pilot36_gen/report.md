# Run report

Backend: `claude_sdk`. Accepted **3 of 3** candidate matters.

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
| solver_check | 3 | 3 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 3 | 0.33: 1, 0.67: 2 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s36-m0001 | accepted | dev | qwen3-small 0.33 |  |
| s36-m0002 | accepted | test | qwen3-small 0.67 |  |
| s36-m0003 | accepted | train | qwen3-small 0.67 |  |

## Variety

- Industries: used car auctions (1), cold chain logistics (1), specialty pharmaceuticals (1)
- Agreement types: distribution agreement (1), asset purchase agreement (1), supply agreement (1)
- Issue types: expired_notice_window (2), defined_term_inconsistency (2), exclusivity_scope (1), missing_assignment_restriction (1), liability_cap_carveout (1), uncapped_indemnity (1), change_of_control_consent (1), survival_gap (1), governing_law_mismatch (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 192656 | 45902 | 0 |
| drafter | 13 | 216974 | 79949 | 0 |
| fact_extractor | 3 | 90530 | 7273 | 0 |
| fact_matcher | 2 | 2787 | 436 | 0 |
| instruction_writer | 3 | 4191 | 1018 | 0 |
| issue_verifier | 11 | 299433 | 8841 | 0 |
| judge | 28 | 194523 | 29331 | 4 |
| ledger_writer | 3 | 12312 | 25579 | 0 |
| rubric_writer | 3 | 19391 | 7056 | 0 |
| solver | 243 | 1892370 | 244278 | 0 |
