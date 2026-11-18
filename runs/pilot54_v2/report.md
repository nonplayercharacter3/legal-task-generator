# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 2 | 0 | 0 |
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
| s54-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F8", "key": "Asset Purchase Agreement order of precedence", "filename": "asset_purchase_agreement.md", "ledger": "Section 11.8 written am |
| s54-m0002 | accepted (label pending) | train |  |  |
| s54-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: event furniture rental (1), solar panel installation (1), commercial laundry services (1)
- Agreement types: asset purchase agreement (2), stock purchase agreement (1)
- Issue types: missing_assignment_restriction (2), expired_notice_window (2), governing_law_mismatch (2), liability_cap_carveout (2), uncapped_indemnity (2), survival_gap (2), defined_term_inconsistency (2), change_of_control_consent (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 263180 | 32849 | 0 |
| drafter | 28 | 967672 | 177042 | 0 |
| fact_extractor | 3 | 194989 | 11875 | 0 |
| fact_matcher | 4 | 5471 | 1399 | 0 |
| instruction_writer | 2 | 2621 | 299 | 0 |
| issue_solo_verifier | 12 | 108892 | 5646 | 0 |
| issue_verifier | 10 | 590861 | 8658 | 0 |
| judge | 6 | 45982 | 4832 | 0 |
| ledger_writer | 3 | 14349 | 49243 | 0 |
| rubric_writer | 2 | 15676 | 4966 | 0 |
