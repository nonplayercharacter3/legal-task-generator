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
| s65-m0001 | accepted (label pending) | test |  |  |
| s65-m0002 | rejected at issue_check |  |  | missing: ["I1"] |
| s65-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: independent film distribution (1), cold chain logistics (1), specialty pharmaceuticals (1)
- Agreement types: stock purchase agreement (1), distribution agreement (1), software license agreement (1)
- Issue types: uncapped_indemnity (3), defined_term_inconsistency (3), missing_assignment_restriction (2), expired_notice_window (2), exclusivity_scope (2), governing_law_mismatch (1), survival_gap (1), liability_cap_carveout (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 361000 | 35455 | 0 |
| drafter | 25 | 1246495 | 279547 | 0 |
| fact_extractor | 3 | 290417 | 12427 | 0 |
| fact_matcher | 3 | 5075 | 740 | 0 |
| instruction_writer | 2 | 2611 | 292 | 0 |
| issue_solo_verifier | 18 | 278957 | 8843 | 0 |
| issue_verifier | 15 | 1318380 | 12513 | 0 |
| judge | 6 | 46860 | 4557 | 0 |
| ledger_writer | 5 | 23962 | 81075 | 0 |
| rubric_writer | 2 | 15524 | 4569 | 0 |
