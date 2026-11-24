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
| s62-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F5", "key": "SPA exclusive forum", "filename": "stock_purchase_agreement.md", "ledger": "Court of Chancery of the State of Delaware, for  |
| s62-m0002 | rejected at issue_check |  |  | missing: ["I5"] |
| s62-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: medical imaging equipment (1), data center cooling (1), boutique hotels (1)
- Agreement types: stock purchase agreement (2), supply agreement (1)
- Issue types: missing_assignment_restriction (3), defined_term_inconsistency (3), uncapped_indemnity (2), liability_cap_carveout (2), expired_notice_window (1), governing_law_mismatch (1), exclusivity_scope (1), auto_renewal (1), survival_gap (1), change_of_control_consent (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 161904 | 11878 | 0 |
| drafter | 6 | 267404 | 79445 | 0 |
| fact_extractor | 1 | 80474 | 3559 | 0 |
| fact_matcher | 1 | 2804 | 683 | 0 |
| instruction_writer | 1 | 1331 | 257 | 0 |
| issue_solo_verifier | 6 | 113663 | 3896 | 0 |
| issue_verifier | 5 | 373273 | 3842 | 0 |
| judge | 3 | 18750 | 2304 | 0 |
| rubric_writer | 1 | 7674 | 1961 | 0 |
