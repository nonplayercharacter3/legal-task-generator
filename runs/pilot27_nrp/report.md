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
| s27-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s27-m0002 | accepted | train | qwen3-small 1.00 |  |
| s27-m0003 | accepted (unsolved) | train | qwen3-small 0.00 |  |

## Variety

- Industries: organic dairy (1), battery recycling (1), elevator maintenance (1)
- Agreement types: stock purchase agreement (2), asset purchase agreement (1)
- Issue types: uncapped_indemnity (2), change_of_control_consent (2), missing_assignment_restriction (2), governing_law_mismatch (2), survival_gap (2), liability_cap_carveout (1), defined_term_inconsistency (1), expired_notice_window (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 217244 | 53045 | 0 |
| drafter | 15 | 316962 | 94868 | 0 |
| fact_extractor | 3 | 103894 | 7764 | 0 |
| fact_matcher | 3 | 4457 | 416 | 0 |
| instruction_writer | 3 | 4255 | 1170 | 0 |
| issue_verifier | 13 | 396484 | 11949 | 0 |
| judge | 21 | 209826 | 20708 | 0 |
| ledger_writer | 3 | 12438 | 24725 | 0 |
| rubric_writer | 3 | 19043 | 4888 | 0 |
| solver | 182 | 1707859 | 179899 | 0 |
