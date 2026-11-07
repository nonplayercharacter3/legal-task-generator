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
| qwen3-small | 3 | 0.00: 2, 1.00: 1 |

**2 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s24-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s24-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s24-m0003 | accepted | train | qwen3-small 1.00 |  |

## Variety

- Industries: elevator maintenance (1), precision agriculture drones (1), water treatment chemicals (1)
- Agreement types: asset purchase agreement (3)
- Issue types: survival_gap (2), change_of_control_consent (2), defined_term_inconsistency (2), expired_notice_window (1), uncapped_indemnity (1), liability_cap_carveout (1), governing_law_mismatch (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 199402 | 46008 | 0 |
| drafter | 14 | 273902 | 86304 | 0 |
| fact_extractor | 3 | 96812 | 8643 | 0 |
| fact_matcher | 3 | 5327 | 1130 | 0 |
| instruction_writer | 3 | 4233 | 1106 | 0 |
| issue_verifier | 11 | 297029 | 8311 | 0 |
| judge | 21 | 173961 | 19488 | 0 |
| ledger_writer | 3 | 12277 | 31315 | 0 |
| rubric_writer | 3 | 18497 | 4714 | 0 |
| solver | 176 | 1564382 | 197366 | 0 |
