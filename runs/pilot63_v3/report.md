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

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**3 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s63-m0001 | accepted (label pending) | train |  |  |
| s63-m0002 | accepted (label pending) | test |  |  |
| s63-m0003 | accepted (label pending) | dev |  |  |

## Variety

- Industries: precision agriculture drones (1), outdoor apparel (1), regional airline catering (1)
- Agreement types: stock purchase agreement (1), master services agreement (1), distribution agreement (1)
- Issue types: change_of_control_consent (2), liability_cap_carveout (2), missing_assignment_restriction (2), exclusivity_scope (2), auto_renewal (2), governing_law_mismatch (2), expired_notice_window (2), survival_gap (1), defined_term_inconsistency (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 626092 | 47839 | 0 |
| drafter | 26 | 1445851 | 313406 | 0 |
| fact_extractor | 3 | 317945 | 12350 | 0 |
| fact_matcher | 3 | 4678 | 622 | 0 |
| instruction_writer | 3 | 3930 | 454 | 0 |
| issue_solo_verifier | 22 | 361351 | 10021 | 0 |
| issue_verifier | 17 | 1644801 | 13929 | 0 |
| judge | 9 | 64917 | 6772 | 0 |
| ledger_writer | 3 | 14443 | 44705 | 0 |
| rubric_writer | 3 | 23878 | 6582 | 0 |
