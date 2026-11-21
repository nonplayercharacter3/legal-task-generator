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
| s501-m0001 | accepted (label pending) | train |  |  |
| s501-m0002 | accepted (label pending) | train |  |  |
| s501-m0003 | rejected at consistency |  |  | mismatches: [{"fact": "F4", "key": "MSA liability cap", "filename": "traivaix_zegath_master_services_agreement.md", "ledger": "Fees paid or payable in the 12 mo |

## Variety

- Industries: used car auctions (1), water treatment chemicals (1), independent film distribution (1)
- Agreement types: stock purchase agreement (1), supply agreement (1), master services agreement (1)
- Issue types: liability_cap_carveout (2), defined_term_inconsistency (2), missing_assignment_restriction (2), survival_gap (1), change_of_control_consent (1), exclusivity_scope (1), auto_renewal (1), uncapped_indemnity (1), governing_law_mismatch (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 190810 | 30540 | 0 |
| drafter | 26 | 665354 | 127281 | 0 |
| fact_extractor | 3 | 143344 | 11858 | 0 |
| fact_matcher | 4 | 6206 | 979 | 0 |
| instruction_writer | 2 | 2669 | 294 | 0 |
| issue_solo_verifier | 8 | 70194 | 4039 | 0 |
| issue_verifier | 8 | 335965 | 6383 | 0 |
| judge | 6 | 42604 | 4441 | 0 |
| ledger_writer | 4 | 18968 | 47038 | 0 |
| rubric_writer | 2 | 14212 | 4290 | 0 |
