# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.
1 matters were reloaded from an earlier run; model calls below cover this run only.

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
| solver_check | 2 | 2 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 2 | 1.00: 2 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s40-m0001 | accepted | train | qwen3-small 1.00 |  |
| s40-m0002 | accepted | train | qwen3-small 1.00 |  |
| s40-m0003 | rejected at consistency |  |  | mismatches: [{"fact": "F8", "key": "Order of precedence", "filename": "bill_of_sale.md", "ledger": "SPA prevails over Ancillary Documents, except Seller Note co |

## Variety

- Industries: commercial laundry services (1), veterinary diagnostics (1), boutique hotels (1)
- Agreement types: distribution agreement (1), asset purchase agreement (1), stock purchase agreement (1)
- Issue types: expired_notice_window (2), defined_term_inconsistency (2), governing_law_mismatch (2), exclusivity_scope (1), change_of_control_consent (1), missing_assignment_restriction (1), survival_gap (1), liability_cap_carveout (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 62548 | 13430 | 0 |
| drafter | 4 | 70245 | 28653 | 0 |
| fact_extractor | 2 | 60476 | 5118 | 0 |
| fact_matcher | 1 | 1482 | 277 | 0 |
| issue_verifier | 3 | 79927 | 2114 | 0 |
| judge | 11 | 100191 | 9718 | 0 |
| ledger_writer | 1 | 4181 | 9656 | 0 |
| solver | 98 | 735789 | 124839 | 0 |
