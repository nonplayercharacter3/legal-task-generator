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
| qwen3-small | 3 | 0.00: 2, 0.33: 1 |

**2 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s25-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s25-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s25-m0003 | accepted | train | qwen3-small 0.33 |  |

## Variety

- Industries: precision agriculture drones (1), seed genetics (1), water treatment chemicals (1)
- Agreement types: distribution agreement (2), supply agreement (1)
- Issue types: liability_cap_carveout (2), uncapped_indemnity (2), exclusivity_scope (2), expired_notice_window (1), change_of_control_consent (1), governing_law_mismatch (1), missing_assignment_restriction (1), defined_term_inconsistency (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 186704 | 48462 | 0 |
| drafter | 13 | 213417 | 79121 | 0 |
| fact_extractor | 3 | 87932 | 6589 | 0 |
| fact_matcher | 3 | 4193 | 738 | 0 |
| instruction_writer | 3 | 4090 | 1127 | 0 |
| issue_verifier | 11 | 281536 | 7146 | 0 |
| judge | 21 | 217180 | 18951 | 0 |
| ledger_writer | 3 | 12377 | 29309 | 0 |
| rubric_writer | 3 | 18067 | 5109 | 0 |
| solver | 146 | 1141185 | 159452 | 0 |
