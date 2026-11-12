# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.
2 matters were reloaded from an earlier run; model calls below cover this run only.

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
| solver_check | 1 | 1 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 0.00: 1 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s45-m0001 | rejected at issue_check |  |  | missing: ["I4"] |
| s45-m0002 | rejected at issue_check |  |  | missing: ["I2"] |
| s45-m0003 | accepted (unsolved) | dev | qwen3-small 0.00 |  |

## Variety

- Industries: school bus operations (1), marine shipping (1), used car auctions (1)
- Agreement types: asset purchase agreement (1), stock purchase agreement (1), master services agreement (1)
- Issue types: missing_assignment_restriction (2), liability_cap_carveout (2), expired_notice_window (2), defined_term_inconsistency (2), change_of_control_consent (2), governing_law_mismatch (2), uncapped_indemnity (2), survival_gap (1), auto_renewal (1), exclusivity_scope (1)
- Party names used in more than one matter: ostrander in s45-m0001, s45-m0003
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 77482 | 13842 | 0 |
| drafter | 8 | 182815 | 35031 | 0 |
| fact_extractor | 1 | 39389 | 3756 | 0 |
| fact_matcher | 1 | 1294 | 121 | 0 |
| instruction_writer | 1 | 1318 | 148 | 0 |
| issue_solo_verifier | 8 | 52199 | 4074 | 0 |
| issue_verifier | 6 | 192819 | 4194 | 0 |
| judge | 7 | 54652 | 6730 | 0 |
| rubric_writer | 1 | 7696 | 2566 | 0 |
| solver | 83 | 703096 | 68235 | 0 |
