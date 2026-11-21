# Run report

Backend: `claude_sdk`. Accepted **3 of 3** candidate matters.
1 matters were reloaded from an earlier run; model calls below cover this run only.

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
| s504-m0001 | accepted (label pending) | train |  |  |
| s504-m0002 | accepted (label pending) | train |  |  |
| s504-m0003 | accepted (label pending) | dev |  |  |

## Variety

- Industries: commercial laundry services (1), water treatment chemicals (1), veterinary diagnostics (1)
- Agreement types: software license agreement (2), asset purchase agreement (1)
- Issue types: missing_assignment_restriction (2), change_of_control_consent (2), governing_law_mismatch (2), uncapped_indemnity (2), expired_notice_window (1), liability_cap_carveout (1), survival_gap (1), auto_renewal (1), defined_term_inconsistency (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 173824 | 32164 | 0 |
| drafter | 6 | 107285 | 28753 | 0 |
| fact_extractor | 2 | 85445 | 6700 | 0 |
| fact_matcher | 1 | 1363 | 106 | 0 |
| instruction_writer | 1 | 1345 | 136 | 0 |
| issue_solo_verifier | 10 | 86000 | 4901 | 0 |
| issue_verifier | 10 | 389246 | 8185 | 0 |
| judge | 6 | 46665 | 4589 | 0 |
| rubric_writer | 1 | 6849 | 2608 | 0 |
