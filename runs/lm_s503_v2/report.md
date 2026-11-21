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
| solver_check | 2 | 0 | 0 | 2 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**2 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s503-m0001 | rejected at issue_check |  |  | missing: ["I4"] |
| s503-m0002 | accepted (label pending) | train |  |  |
| s503-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: pet food manufacturing (1), solar panel installation (1), dental clinics (1)
- Agreement types: asset purchase agreement (1), master services agreement (1), distribution agreement (1)
- Issue types: defined_term_inconsistency (3), missing_assignment_restriction (2), change_of_control_consent (2), governing_law_mismatch (2), expired_notice_window (1), exclusivity_scope (1), uncapped_indemnity (1), liability_cap_carveout (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 183880 | 32652 | 0 |
| drafter | 23 | 616295 | 137886 | 0 |
| fact_extractor | 3 | 148977 | 10510 | 0 |
| fact_matcher | 3 | 5358 | 1388 | 0 |
| instruction_writer | 2 | 2656 | 309 | 0 |
| issue_solo_verifier | 18 | 162267 | 9885 | 0 |
| issue_verifier | 14 | 593876 | 10728 | 0 |
| judge | 6 | 44269 | 4417 | 0 |
| ledger_writer | 3 | 14291 | 38787 | 0 |
| rubric_writer | 2 | 15326 | 5062 | 0 |
