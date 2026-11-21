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
| qwen3-small | 2 | 0.00: 1, 1.00: 1 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s51-m0001 | accepted | train | qwen3-small 1.00 |  |
| s51-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s51-m0003 | rejected at issue_check |  |  | missing: ["I3"] |

## Variety

- Industries: medical imaging equipment (1), water treatment chemicals (1), pet food manufacturing (1)
- Agreement types: stock purchase agreement (1), asset purchase agreement (1), supply agreement (1)
- Issue types: missing_assignment_restriction (3), defined_term_inconsistency (2), governing_law_mismatch (2), change_of_control_consent (1), liability_cap_carveout (1), expired_notice_window (1), survival_gap (1), uncapped_indemnity (1), exclusivity_scope (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 208182 | 28591 | 0 |
| drafter | 25 | 708812 | 131700 | 0 |
| fact_extractor | 3 | 147635 | 12033 | 0 |
| fact_matcher | 3 | 5094 | 609 | 0 |
| instruction_writer | 2 | 2624 | 286 | 0 |
| issue_solo_verifier | 22 | 185072 | 10737 | 0 |
| issue_verifier | 14 | 577521 | 11415 | 0 |
| judge | 19 | 149179 | 19538 | 0 |
| ledger_writer | 4 | 18323 | 57132 | 0 |
| rubric_writer | 2 | 14260 | 4002 | 0 |
| solver | 381 | 4462898 | 260540 | 7 |
