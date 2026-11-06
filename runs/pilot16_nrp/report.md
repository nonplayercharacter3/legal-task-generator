# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 2 | 1 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 1 | 1 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 1 | 0 | 0 |

Bundled issue criteria (`gates.check_bundling`): 1 matter(s) flagged in the final rubric; 0 repair(s) ran, 0 cleared.

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 0.33: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s16-m0001 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C4"] |
| s16-m0002 | accepted | train | qwen3-small 0.33 |  |
| s16-m0003 | rejected at leak_check |  |  | hits: [{"issue": "I3", "phrase": "Lumora Biomechanics", "in": "instruction"}] |

## Variety

- Industries: dental clinics (1), battery recycling (1), orthopedic implants (1)
- Agreement types: stock purchase agreement (2), asset purchase agreement (1)
- Issue types: expired_notice_window (2), governing_law_mismatch (2), change_of_control_consent (2), liability_cap_carveout (2), survival_gap (1), missing_assignment_restriction (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 136930 | 31702 | 0 |
| drafter | 13 | 250780 | 87137 | 0 |
| fact_extractor | 3 | 94288 | 6954 | 0 |
| fact_matcher | 3 | 4527 | 641 | 0 |
| instruction_writer | 3 | 4175 | 1107 | 0 |
| issue_verifier | 11 | 302554 | 9269 | 0 |
| judge | 10 | 82860 | 7545 | 0 |
| ledger_writer | 3 | 12262 | 25340 | 0 |
| rubric_writer | 2 | 11862 | 3196 | 0 |
| solver | 57 | 480065 | 58993 | 0 |
