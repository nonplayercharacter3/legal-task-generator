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
| qwen3-small | 3 | 0.33: 2, 1.00: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s39-m0001 | accepted | train | qwen3-small 0.33 |  |
| s39-m0002 | accepted | train | qwen3-small 1.00 |  |
| s39-m0003 | accepted | train | qwen3-small 0.33 |  |

## Variety

- Industries: regional airline catering (1), industrial textiles (1), commercial bakery (1)
- Agreement types: stock purchase agreement (2), master services agreement (1)
- Issue types: missing_assignment_restriction (3), defined_term_inconsistency (2), survival_gap (2), expired_notice_window (2), change_of_control_consent (2), uncapped_indemnity (1), governing_law_mismatch (1), liability_cap_carveout (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 221614 | 59574 | 0 |
| drafter | 14 | 295569 | 95628 | 0 |
| fact_extractor | 3 | 104041 | 7223 | 0 |
| fact_matcher | 3 | 4651 | 485 | 0 |
| instruction_writer | 3 | 4341 | 1084 | 0 |
| issue_verifier | 14 | 429475 | 10564 | 0 |
| judge | 30 | 209200 | 27418 | 9 |
| ledger_writer | 3 | 12471 | 35268 | 0 |
| rubric_writer | 3 | 21040 | 8232 | 0 |
| solver | 283 | 1760009 | 224847 | 0 |
