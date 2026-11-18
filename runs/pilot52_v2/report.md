# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 1 | 2 | 0 |
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
| s52-m0001 | rejected at issue_check |  |  | missing: ["I4"] |
| s52-m0002 | rejected at issue_check |  |  | missing: ["I3"] |
| s52-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: outdoor apparel (1), commercial bakery (1), concert promotion (1)
- Agreement types: master services agreement (2), supply agreement (1)
- Issue types: change_of_control_consent (3), defined_term_inconsistency (2), expired_notice_window (2), auto_renewal (2), missing_assignment_restriction (1), governing_law_mismatch (1), uncapped_indemnity (1), liability_cap_carveout (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 90900 | 16026 | 0 |
| drafter | 29 | 779530 | 136505 | 0 |
| fact_extractor | 3 | 151005 | 12177 | 0 |
| fact_matcher | 2 | 3259 | 536 | 0 |
| instruction_writer | 1 | 1300 | 142 | 0 |
| issue_solo_verifier | 18 | 129089 | 8999 | 0 |
| issue_verifier | 14 | 586074 | 10797 | 0 |
| judge | 3 | 20364 | 1829 | 0 |
| ledger_writer | 4 | 18120 | 45755 | 0 |
| rubric_writer | 1 | 6873 | 2563 | 0 |
