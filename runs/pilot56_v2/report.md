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
| s56-m0001 | accepted (label pending) | train |  |  |
| s56-m0002 | accepted (label pending) | train |  |  |
| s56-m0003 | rejected at issue_check |  |  | missing: ["I3"] |

## Variety

- Industries: used car auctions (1), school bus operations (1), commercial bakery (1)
- Agreement types: software license agreement (1), asset purchase agreement (1), supply agreement (1)
- Issue types: auto_renewal (2), exclusivity_scope (2), change_of_control_consent (2), defined_term_inconsistency (2), expired_notice_window (2), governing_law_mismatch (2), uncapped_indemnity (2), liability_cap_carveout (1), survival_gap (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 180268 | 28907 | 0 |
| drafter | 23 | 575758 | 122585 | 0 |
| fact_extractor | 3 | 133341 | 9420 | 0 |
| fact_matcher | 3 | 4247 | 413 | 0 |
| instruction_writer | 2 | 2630 | 284 | 0 |
| issue_solo_verifier | 22 | 169387 | 11151 | 0 |
| issue_verifier | 17 | 638753 | 11434 | 0 |
| judge | 6 | 43951 | 4843 | 0 |
| ledger_writer | 4 | 19382 | 58161 | 0 |
| rubric_writer | 2 | 15870 | 5429 | 0 |
