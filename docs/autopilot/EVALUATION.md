# How we judge the tasks: valid, LAB-like, and useful for training

Written 2026-11-17. The autopilot applies this; M4 uses levels 1 to 3 to decide whether a generator version is good
enough to scale, and M6 runs level 4. Every number gets recorded in `docs/autopilot/LOG.md` and the latest ones in
`STATE.md`.

The idea in one line: a task is worth training on only if it is **correct** (level 1), **shaped like the exam**
(level 2), **about as hard as the exam** (level 3), and **training on it actually moves the exam score** (level 4).
The first three are cheap and come first; the fourth is the real test and comes once there is enough data.

## Level 1. Each task is sound (it has one right answer and the checklist grades it fairly)

Why: a wrong answer key teaches the model wrong law, and an unfair checklist teaches it to chase the checklist.

Automatic, every task (already in the pipeline; a task failing any of these is rejected):
- the facts agree across documents (`consistency`); each planted problem is really in the folder and still
  actionable (`issue_check`), and a two-document problem cannot be found from either document alone;
- no hint gives the answer away (`leak_check`), and Qwen without the documents cannot pass (leak probe);
- every checklist item traces to the answer key (`rubric_trace`); the gold memo passes every item and the flawed
  memo fails the right ones (`rubric_tests`);
- n-gram screen against LAB's text (no copying).

Audit, every batch: an independent referee (Opus, a fresh prompt like the one in
`docs/research/unsolved_review_2026-11.md`, seeing the folder, answer key and checklist) reads a random 10% of the new
accepted tasks (at least 3) and answers: is each planted problem a real legal problem under the stated law; would a
correct memo by a competent associate pass every item; does any item demand one particular route; is there an
unplanted problem a good memo would raise that the checklist would punish or ignore.
- Target: at least 90% of audited tasks clean. Each finding is a defect class: fix it in the generator, and drop or
  fix the affected tasks (`scripts/drop_criteria.py` for single items).

Strong-model check, on tasks Qwen never solves: let Opus solve the task once as the test-taker. If Opus also fails the
same item, suspect the item and send it to the referee. Tasks nobody can pass teach nothing.

Human check (once, not blocking scale-up): someone with legal training reads 10 tasks and grades 5 memos. The
autopilot asks for this through a `needs-sirui` issue; it gates the handoff to Pengtao, not the batches.

## Level 2. The dataset is shaped like LAB

Why: practice that differs from the exam in shape (tiny folders, instructions that list every file) trains habits
the exam never rewards.

Measured with `scripts/dataset_stats.py` against LAB's contracts and corporate-ma tasks (counts only, never LAB text),
over the tasks of the generator version under test:

| Measure | Must reach | LAB (for reference) | v1 had |
| --- | --- | --- | --- |
| Documents per task, median | 7 or more | 7 to 10 | 4 |
| Words per folder, median | 20,000 or more | 33,000 to 74,000 | 9,400 |
| Instruction words, median | 90 or fewer | 25 to 74 | 160 |
| Instructions naming every file | 5% or fewer | about 0% | 96% |
| Planted problems needing two documents | 40% or more | common | 0% |
| Checklist items per task, median | 20 or more (soft: report, do not fail on it alone) | about 57 | 10 |
| Industries across the dataset | 15 or more | many | few |

A miss on a "must reach" row fails level 2. Grow the checklist through more problems, facts and negative items, not
by splitting one problem into several items (that was the round 8 bloat).

## Level 3. The tasks are about as hard as LAB, measured the same way

Why: if Qwen breezes through our tasks but fails LAB's, our tasks are not practicing what LAB tests.

Same model (Qwen3.8-27B, `qwen3-small`, reasoning low), same tool (LAB's own harness), same judge (Opus through the
SDK, LAB's prompt, one call per item) on both sides:
- LAB side: the frozen 30-task sample (`docs/autopilot/lab_sample.md`). So far 12 scored: all-pass 2 of 12 (17%),
  items passed 87.5%, close to the published 11.25% and 88.8%.
- Our side: at least 20 tasks of the version under test, dev and test split first.

Pass when all hold:
- our all-pass rate is within 15 points of LAB's on the same run (for example LAB 15%: ours between 0% and 30%);
- our item pass rate is within 5 points of LAB's;
- at least 10% of our tasks are solved by Qwen at least once in their 3 labelling tries (otherwise there is nothing
  to learn from; the generator is too hard or unfair, see level 1's strong-model check).

Optional, if cheap (hosted models on NRP cost no Claude usage): run two or three other hosted models on 15 of ours and
15 LAB tasks. If our tasks rank the models in the same order as LAB does, they measure the same skill.

Small samples are noisy: report counts, not only percentages, and a bootstrap interval when comparing.

## Level 4. Training on the tasks moves the LAB score (the real test)

Why: levels 1 to 3 say the tasks look right; only training says they help. Do this before the lab spends a large
run on them.

Pilot fine-tune, planned in `docs/autopilot/pilot_finetune.md` before anything runs:
- **Model:** a small open model the lab is likely to train (the post-training agent's examples use Qwen3 1.7B to 4B);
  default Qwen3-4B. Measure it before training on everything below.
- **Data:** the train split of the passing version, at least 150 tasks, chat messages ending in the gold memo (the
  handoff package's `data/train.jsonl`). Method: LoRA supervised fine-tuning, a few epochs, held-out dev split for
  stopping.
- **Compute:** one Nautilus Job, 1 GPU, within the GPU rules in PROMPT.md; delete it when done.
- **Measure, before and after, same settings:**
  - (a) our test split with the frozen grader (`grade/evaluate.py` from the handoff package): all-pass and item rate;
  - (b) the LAB contracts and corporate-ma tasks of the frozen sample, through LAB's harness;
  - (c) the other LAB tasks of the sample, to catch the model getting worse outside contract review.
- **Control (if compute allows):** the same fine-tune on the same number of v1 tasks. If v2 helps LAB more than v1,
  the hardening was worth it.

Read the result:
- (a) up and (b) up, (c) not down by more than 2 points: the tasks are useful. Scale and hand off.
- (a) up but (b) flat: the model learned our format, not LAB's skill. Look at what LAB tasks it still fails (work type,
  deliverable, length) and close that gap in the generator before making many more.
- (a) flat: the tasks or the training are broken; check the training first (loss, a few outputs), then the data.
- Use the same items on both runs and compare them in pairs; with 30 LAB tasks, small differences are noise.

## What gets recorded per generator version

In `docs/autopilot/LOG.md`, one block per evaluation: version and config, task count, level 1 audit result, level 2
table, level 3 numbers both sides with counts, level 4 if run, and the decision (scale, harden, or ask).
