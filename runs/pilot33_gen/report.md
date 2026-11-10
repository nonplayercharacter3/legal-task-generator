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
| s33-m0001 | accepted (label pending) | train |  |  |
| s33-m0002 | accepted (label pending) | train |  |  |
| s33-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: veterinary diagnostics (1), pet food manufacturing (1), organic dairy (1)
- Agreement types: distribution agreement (2), asset purchase agreement (1)
- Issue types: change_of_control_consent (3), governing_law_mismatch (2), missing_assignment_restriction (1), defined_term_inconsistency (1), auto_renewal (1), liability_cap_carveout (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 178156 | 39187 | 0 |
| drafter | 13 | 203605 | 74770 | 0 |
| fact_extractor | 3 | 83008 | 5943 | 0 |
| fact_matcher | 2 | 3072 | 390 | 0 |
| instruction_writer | 3 | 4179 | 951 | 0 |
| issue_verifier | 10 | 243080 | 6646 | 0 |
| judge | 9 | 58725 | 6894 | 0 |
| ledger_writer | 3 | 12227 | 20894 | 0 |
| rubric_writer | 3 | 18454 | 6514 | 0 |
