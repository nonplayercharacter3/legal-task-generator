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
| s57-m0001 | accepted (label pending) | train |  |  |
| s57-m0002 | accepted (label pending) | train |  |  |
| s57-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: specialty pharmaceuticals (1), dental clinics (1), veterinary diagnostics (1)
- Agreement types: stock purchase agreement (2), distribution agreement (1)
- Issue types: uncapped_indemnity (2), liability_cap_carveout (2), governing_law_mismatch (2), survival_gap (2), change_of_control_consent (2), expired_notice_window (2), missing_assignment_restriction (2), defined_term_inconsistency (1), auto_renewal (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 330150 | 47380 | 0 |
| drafter | 27 | 821541 | 151942 | 0 |
| fact_extractor | 3 | 169336 | 11340 | 0 |
| fact_matcher | 3 | 4269 | 501 | 0 |
| instruction_writer | 3 | 3963 | 429 | 0 |
| issue_solo_verifier | 18 | 158501 | 8421 | 0 |
| issue_verifier | 17 | 818724 | 13455 | 0 |
| judge | 9 | 68639 | 6691 | 0 |
| ledger_writer | 3 | 14511 | 46463 | 0 |
| rubric_writer | 3 | 23718 | 6966 | 0 |
