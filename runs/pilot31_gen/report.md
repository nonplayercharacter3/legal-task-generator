# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 2 | 1 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 2 | 0 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 2 | 2 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 2 | 0.67: 2 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s31-m0001 | accepted | train | qwen3-small 0.67 |  |
| s31-m0002 | accepted | train | qwen3-small 0.67 |  |
| s31-m0003 | rejected at issue_check |  |  | missing: ["I2"] |

## Variety

- Industries: craft brewing (1), seed genetics (1), solar panel installation (1)
- Agreement types: supply agreement (2), asset purchase agreement (1)
- Issue types: auto_renewal (2), expired_notice_window (2), uncapped_indemnity (2), missing_assignment_restriction (1), liability_cap_carveout (1), exclusivity_scope (1), governing_law_mismatch (1), change_of_control_consent (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 106292 | 30260 | 0 |
| drafter | 14 | 228146 | 66848 | 0 |
| fact_extractor | 3 | 77886 | 7573 | 0 |
| fact_matcher | 3 | 4906 | 509 | 0 |
| instruction_writer | 2 | 2827 | 719 | 0 |
| issue_verifier | 12 | 254955 | 8858 | 0 |
| judge | 14 | 122073 | 17224 | 0 |
| ledger_writer | 3 | 12381 | 25038 | 0 |
| rubric_writer | 2 | 13202 | 5272 | 0 |
| solver | 98 | 618860 | 89457 | 0 |
