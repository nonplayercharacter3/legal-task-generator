# Our dataset against LAB (2026-11-11)

Made by `scripts/dataset_stats.py` (PR #32), no model calls. Our side: the 73 accepted `task.json` committed at
ed0cfb8 (the 68 the reviewer counted plus later rounds), 12 of them `unsolved`, 1 held. LAB side: `harveyai/harvey-labs`
as cloned on the laptop, 2,010 tasks. Counts only; no LAB text is copied here. The reviewer's note is in
`.inbox/2026-11-11-lab-gap/review.md` (not in the repo).

## How a LAB task is laid out

A task is any folder holding a `task.json`, 2 to 4 levels under `tasks/`: `<area>/<task>`,
`<area>/<task>/scenario-NN`, or `contracts/<sub-area>/<task>/scenario-NN`. The first folder name is the practice area.
`task.json` holds the instruction (`instructions`), the rubric (`criteria`: `id`, `title`, `match_criteria`) and, in
most, `work_type` and `deliverables` ({file name: file name}). The matter documents are the files under the task's
`documents/` folder (.docx, .xlsx, .eml, .pptx, .txt, .json). No Git LFS pointer files were found in this clone (the
script counts one as a file with no words). Three groups, which behave differently:

- **practice-area**, 1,262 tasks: `work_type` and `deliverables` present.
- **contracts**, 498 tasks: neither; the reply is the deliverable, so these are the closest to ours.
- **firm-knowledge**, 250 tasks: `docs_dir` points at one shared DMS folder, no per-task documents, answer in
  `response.md`. Left out of the folder rows.

## The table

Spreads are min / p10 / median / p90 / max. LAB maxima come from a few outlier tasks (one folder holds 4,061 files and
61.8M words), so read the medians.

| Measure | Ours (73) | LAB practice-area (1,262) | LAB contracts (498) |
|---|---|---|---|
| Documents per task | 4 / 4 / 4 / 5 / 5 | 2 / 5 / 7 / 10 / 4061 | 5 / 8 / 10 / 13 / 20 |
| Words per folder | 6058 / 6567 / 9419 / 12682 / 14695 | 3941 / 16528 / 32951 / 56763 / 61.8M | 25435 / 46000 / 74281 / 122271 / 250848 |
| File formats | .md 327 | .docx 30849, .xlsx 9717, .eml 4059, .pptx 1052, .txt 873, .json 5 | .docx 3105, .eml 1110, .xlsx 858, .pptx 39, .txt 16 |
| Rubric criteria per task | 8 / 9 / 10 / 20 / 25 | 23 / 38 / 57 / 83 / 1114 | 25 / 36 / 58 / 91 / 142 |
| Instruction words (mean, median) | 159.6, 160 | 25.1, 25 | 76.1, 74 |
| Instructions naming every file | 96% | 0.2% | 0% |
| Deliverable | reply (memo) 73 | file 1262 (.docx 1247, .xlsx 39, .md 11) | reply (not stated) 498 |
| Work types | issue-spotting memo 73 | analyze 488, draft 444, review 306, research 24 | not stated |
| Practice areas | commercial contracts 41, M&A 32 | 24 areas, largest corporate-ma 161, intellectual-property 147, corporate-governance 97 | contracts 498 |
| Issues per task | 3 / 4 / 5 (min / median / max), 293 in all | n/a | n/a |
| Issue types | 10 distinct; top: change_of_control_consent 36, defined_term_inconsistency 34, expired_notice_window 34 | n/a | n/a |

LAB overall (all 2,010 tasks): median 8 documents, median 54 criteria, instructions 42.5 words on average. Our
`unsolved` subset (12 tasks) and the held one (1) look like the rest; see `dataset_stats.md` from the script for the
split columns.

## Qwen's per-check pass rate on our tasks

From the label grades stored in each `gates.json` (qwen3-small, 3 attempts each; 52 of the 73 tasks have grades, 156
attempts, 1,770 criterion grades; the rest are label-pending or older runs without per-model grades).

| Group | Criteria graded | Pass rate |
|---|---|---|
| All criteria | 1,770 | 0.9254 |
| Issue | 888 | 0.8975 |
| Fact | 318 | 0.8962 |
| Negative | 306 | 0.9869 |
| Format | 258 | 0.9845 |
| Rubric 8 to 9 criteria (20 tasks) | 528 | 0.928 |
| Rubric 10 (15 tasks) | 450 | 0.929 |
| Rubric 11 to 12 (8 tasks) | 270 | 0.926 |
| Rubric 13 or more (9 tasks) | 522 | 0.920 |

The all-pass rate over the same attempts is 0.5128. The reviewer's figures for Qwen 3.8 27B on the Vals held-out set
are all-pass 11.25% and criteria 88.78%. They come from the reviewer and use another harness and judge (one call per
criterion, two judges), so this is not a strict comparison.

## What it says

Our tasks are small beside LAB: 4 to 5 markdown documents (about 9,400 words) against a median of 7 documents and
about 33,000 words in LAB's practice-area tasks, and 10 criteria against about 57. Every task is the same shape, an
issue-spotting memo returned in the reply, over Delaware and New York contracts and M&A, with 10 issue types; LAB mixes
four work types, file deliverables and 24 practice areas. Our instructions are about six times longer than LAB's
practice-area ones and name every file, where LAB's almost never do. On a per-check basis Qwen passes about 93% of our
criteria against 89% of LAB's on the Vals set, close enough that the large all-pass gap (51% against 11%) mostly
reflects LAB having five times as many criteria that must all pass (0.93 to the 10th is 0.48, 0.89 to the 57th is near
0), not that single checks are much harder. Different harness and judge, so the per-check match is only suggestive;
T46 runs Qwen through LAB's own tool to measure the gap properly.
