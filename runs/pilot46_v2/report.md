# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

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
| s46-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F4", "key": "Distribution Agreement forum", "filename": "brugev_tesaisk_distribution_agreement.md", "ledger": "State or federal courts lo |
| s46-m0002 | rejected at issue_check |  |  | missing: ["I6"] |
| s46-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: orthopedic implants (1), specialty pharmaceuticals (1), veterinary diagnostics (1)
- Agreement types: supply agreement (2), distribution agreement (1)
- Issue types: uncapped_indemnity (3), expired_notice_window (3), governing_law_mismatch (2), change_of_control_consent (2), defined_term_inconsistency (2), exclusivity_scope (1), liability_cap_carveout (1), auto_renewal (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 63310 | 13088 | 0 |
| drafter | 20 | 453414 | 91410 | 0 |
| fact_extractor | 3 | 103769 | 9792 | 0 |
| fact_matcher | 2 | 3566 | 830 | 0 |
| instruction_writer | 1 | 1313 | 157 | 0 |
| issue_solo_verifier | 20 | 141045 | 9523 | 0 |
| issue_verifier | 11 | 305101 | 9113 | 0 |
| judge | 3 | 19604 | 2527 | 0 |
| ledger_writer | 5 | 23312 | 59919 | 0 |
| rubric_writer | 1 | 7101 | 2008 | 0 |
