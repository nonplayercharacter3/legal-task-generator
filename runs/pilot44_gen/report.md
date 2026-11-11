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
| s44-m0001 | accepted (label pending) | train |  |  |
| s44-m0002 | accepted (label pending) | train |  |  |
| s44-m0003 | accepted (label pending) | dev |  |  |

## Variety

- Industries: school bus operations (1), concert promotion (1), used car auctions (1)
- Agreement types: supply agreement (1), stock purchase agreement (1), master services agreement (1)
- Issue types: missing_assignment_restriction (2), liability_cap_carveout (2), change_of_control_consent (1), exclusivity_scope (1), uncapped_indemnity (1), defined_term_inconsistency (1), survival_gap (1), governing_law_mismatch (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 175672 | 54278 | 0 |
| drafter | 14 | 226137 | 71257 | 0 |
| fact_extractor | 3 | 83551 | 7784 | 0 |
| fact_matcher | 2 | 3382 | 784 | 0 |
| instruction_writer | 3 | 4235 | 1091 | 0 |
| issue_verifier | 11 | 254903 | 6968 | 0 |
| judge | 9 | 73351 | 7925 | 0 |
| ledger_writer | 3 | 12253 | 21686 | 0 |
| rubric_writer | 3 | 18417 | 7019 | 0 |
