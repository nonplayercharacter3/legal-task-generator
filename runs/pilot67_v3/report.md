# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 1 | 2 | 0 |
| leak_check | 1 | 1 | 0 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 1 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 0.00: 1 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s67-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s67-m0002 | rejected at issue_check |  |  | missing: ["I6"] |
| s67-m0003 | rejected at issue_check |  |  | missing: ["I1"] |

## Variety

- Industries: craft brewing (1), seed genetics (1), independent film distribution (1)
- Agreement types: stock purchase agreement (2), asset purchase agreement (1)
- Issue types: survival_gap (3), governing_law_mismatch (3), change_of_control_consent (3), defined_term_inconsistency (2), liability_cap_carveout (2), uncapped_indemnity (2), expired_notice_window (2), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 228832 | 18157 | 0 |
| drafter | 22 | 1166262 | 290354 | 0 |
| fact_extractor | 3 | 291694 | 10371 | 0 |
| fact_matcher | 3 | 5353 | 800 | 0 |
| instruction_writer | 1 | 1325 | 147 | 0 |
| issue_solo_verifier | 24 | 436771 | 12985 | 0 |
| issue_verifier | 18 | 1633272 | 16145 | 0 |
| judge | 7 | 69881 | 7141 | 0 |
| ledger_writer | 3 | 14526 | 58879 | 0 |
| rubric_writer | 1 | 8320 | 2086 | 0 |
| solver | 184 | 5121391 | 198917 | 0 |
