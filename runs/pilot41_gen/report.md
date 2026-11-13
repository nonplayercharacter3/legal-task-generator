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
| qwen3-small | 3 | 0.67: 1, 1.00: 2 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s41-m0001 | accepted | train | qwen3-small 0.67 |  |
| s41-m0002 | accepted | train | qwen3-small 1.00 |  |
| s41-m0003 | accepted | train | qwen3-small 1.00 |  |

## Variety

- Industries: medical imaging equipment (1), pet food manufacturing (1), event furniture rental (1)
- Agreement types: stock purchase agreement (1), distribution agreement (1), master services agreement (1)
- Issue types: missing_assignment_restriction (2), defined_term_inconsistency (2), change_of_control_consent (1), survival_gap (1), expired_notice_window (1), liability_cap_carveout (1), uncapped_indemnity (1), governing_law_mismatch (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 169076 | 39721 | 0 |
| drafter | 13 | 218513 | 68108 | 0 |
| fact_extractor | 3 | 80912 | 7047 | 0 |
| fact_matcher | 2 | 2927 | 284 | 0 |
| instruction_writer | 3 | 4251 | 1047 | 0 |
| issue_verifier | 10 | 224292 | 6290 | 0 |
| judge | 21 | 177202 | 21585 | 0 |
| ledger_writer | 3 | 12166 | 22296 | 0 |
| rubric_writer | 3 | 18304 | 6590 | 0 |
| solver | 148 | 1120793 | 148166 | 1 |
