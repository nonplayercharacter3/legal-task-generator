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

Bundled issue criteria (`gates.check_bundling`): 1 matter(s) flagged in the final rubric; 0 repair(s) ran, 0 cleared.

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 3 | 0.00: 2, 0.33: 1 |

**2 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s21-m0001 | accepted | train | qwen3-small 0.33 |  |
| s21-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s21-m0003 | accepted (unsolved) | train | qwen3-small 0.00 |  |

## Variety

- Industries: pet food manufacturing (1), independent film distribution (1), elevator maintenance (1)
- Agreement types: stock purchase agreement (1), supply agreement (1), master services agreement (1)
- Issue types: missing_assignment_restriction (2), uncapped_indemnity (2), expired_notice_window (2), defined_term_inconsistency (2), exclusivity_scope (2), survival_gap (1), change_of_control_consent (1), liability_cap_carveout (1), auto_renewal (1), governing_law_mismatch (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 163950 | 43568 | 0 |
| drafter | 13 | 215564 | 66680 | 0 |
| fact_extractor | 3 | 73897 | 6828 | 0 |
| fact_matcher | 3 | 4418 | 459 | 0 |
| instruction_writer | 3 | 4067 | 1079 | 0 |
| issue_verifier | 15 | 316397 | 9843 | 0 |
| judge | 21 | 172068 | 22358 | 0 |
| ledger_writer | 3 | 12554 | 34828 | 0 |
| rubric_writer | 3 | 19959 | 6581 | 0 |
| solver | 132 | 869915 | 146875 | 0 |
