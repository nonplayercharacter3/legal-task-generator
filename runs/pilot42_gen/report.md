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
| solver_check | 3 | 0 | 0 | 3 |

Bundled issue criteria (`gates.check_bundling`): 1 matter(s) flagged in the final rubric; 0 repair(s) ran, 0 cleared.

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**3 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s42-m0001 | accepted (label pending) | train |  |  |
| s42-m0002 | accepted (label pending) | train |  |  |
| s42-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: craft brewing (1), outdoor apparel (1), solar panel installation (1)
- Agreement types: software license agreement (2), master services agreement (1)
- Issue types: auto_renewal (2), uncapped_indemnity (2), liability_cap_carveout (1), missing_assignment_restriction (1), governing_law_mismatch (1), change_of_control_consent (1), defined_term_inconsistency (1), exclusivity_scope (1), expired_notice_window (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 147070 | 36075 | 0 |
| drafter | 13 | 192617 | 59077 | 0 |
| fact_extractor | 3 | 69160 | 6271 | 0 |
| fact_matcher | 2 | 2866 | 564 | 0 |
| instruction_writer | 3 | 4209 | 1115 | 0 |
| issue_verifier | 11 | 215760 | 7362 | 0 |
| judge | 9 | 54706 | 6132 | 0 |
| ledger_writer | 3 | 12135 | 21156 | 0 |
| rubric_writer | 3 | 18595 | 5729 | 0 |
