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
| qwen3-small | 3 | 0.00: 2, 1.00: 1 |

**2 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s23-m0001 | accepted (unsolved) | test | qwen3-small 0.00 |  |
| s23-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s23-m0003 | accepted | train | qwen3-small 1.00 |  |

## Variety

- Industries: event furniture rental (1), seed genetics (1), video game publishing (1)
- Agreement types: distribution agreement (1), master services agreement (1), stock purchase agreement (1)
- Issue types: uncapped_indemnity (2), missing_assignment_restriction (2), change_of_control_consent (2), governing_law_mismatch (1), expired_notice_window (1), exclusivity_scope (1), liability_cap_carveout (1), defined_term_inconsistency (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 187000 | 46348 | 0 |
| drafter | 14 | 249839 | 81260 | 0 |
| fact_extractor | 3 | 90994 | 6927 | 0 |
| fact_matcher | 2 | 2509 | 179 | 0 |
| instruction_writer | 3 | 4212 | 1096 | 0 |
| issue_verifier | 11 | 282628 | 7544 | 0 |
| judge | 21 | 196641 | 20150 | 0 |
| ledger_writer | 3 | 12265 | 24707 | 0 |
| rubric_writer | 3 | 18124 | 5241 | 0 |
| solver | 157 | 1286958 | 157724 | 0 |
