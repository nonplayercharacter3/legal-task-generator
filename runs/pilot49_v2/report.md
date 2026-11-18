# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.
2 matters were reloaded from an earlier run; model calls below cover this run only.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 1 | 1 | 0 |
| leak_check | 1 | 1 | 0 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 0 | 0 | 1 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**1 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s49-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F10", "key": "APA representation survival period", "filename": "asset_purchase_agreement.md", "ledger": "earlier of 12 months after Closi |
| s49-m0002 | accepted (label pending) | train |  |  |
| s49-m0003 | rejected at issue_check |  |  | missing: ["I2"] |

## Variety

- Industries: craft brewing (1), seed genetics (1), boutique hotels (1)
- Agreement types: asset purchase agreement (2), master services agreement (1)
- Issue types: missing_assignment_restriction (3), uncapped_indemnity (2), change_of_control_consent (2), survival_gap (2), expired_notice_window (2), liability_cap_carveout (2), governing_law_mismatch (1), defined_term_inconsistency (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| drafter | 6 | 136336 | 35790 | 0 |
| fact_extractor | 1 | 40166 | 3345 | 0 |
| issue_solo_verifier | 8 | 67047 | 4265 | 0 |
| issue_verifier | 5 | 170837 | 4439 | 0 |
