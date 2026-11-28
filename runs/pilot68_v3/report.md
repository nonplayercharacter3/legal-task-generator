# Run report

Backend: `claude_sdk`. Accepted **3 of 3** candidate matters.
2 matters were reloaded from an earlier run; model calls below cover this run only.

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

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**3 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s68-m0001 | accepted (label pending) | train |  |  |
| s68-m0002 | accepted (label pending) | train |  |  |
| s68-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: outdoor apparel (1), commercial laundry services (1), elevator maintenance (1)
- Agreement types: master services agreement (1), software license agreement (1), supply agreement (1)
- Issue types: auto_renewal (2), change_of_control_consent (2), defined_term_inconsistency (2), uncapped_indemnity (2), expired_notice_window (2), missing_assignment_restriction (2), governing_law_mismatch (1), liability_cap_carveout (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 183436 | 15883 | 0 |
| drafter | 8 | 362740 | 88881 | 0 |
| fact_extractor | 1 | 91752 | 3444 | 0 |
| fact_matcher | 1 | 1514 | 351 | 0 |
| instruction_writer | 1 | 1302 | 155 | 0 |
| issue_solo_verifier | 8 | 112093 | 3373 | 0 |
| issue_verifier | 5 | 426103 | 4356 | 0 |
| judge | 3 | 22474 | 2041 | 0 |
| rubric_writer | 1 | 7626 | 2027 | 0 |
