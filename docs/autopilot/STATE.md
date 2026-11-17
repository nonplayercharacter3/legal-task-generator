STATUS: RUNNING

# Autopilot state

Plain-words picture of where the project is. The autopilot reads this first and rewrites it last, every iteration.
Keep it under about 150 lines; history goes to LOG.md.

Last updated: 2026-11-17 15:15, autopilot iteration 1.

## Goal
A one-command batch tool (`ltg batch`) that builds a dataset of LAB-like contract-review tasks, with the tasks shown
to be sound, LAB-like and useful for training (EVALUATION.md), at least 250 of them, handed to the lab's post-training
agent. Full definition of done: PROMPT.md.

## Where things are (2026-11-17)
- Pool: 88 accepted tasks (70 without unsolved). 87 are v1 (too easy and too small next to LAB); 1 is v2 (s45-m0003).
- 250 target paused since 2026-11-11 until v2 is shown hard enough.
- v2 generator merged (`configs/pilot_generate_v2.toml`). First round, seed 45: 1 of 3 kept, both rejections correct;
  Qwen failed the kept one 3 of 3, on the second-document half of one problem.
- LAB baseline: 12 of 30 LAB sample tasks scored, 0 grading errors: all-pass 2 of 12, items 625 of 714 (87.5%).
  18 LAB tasks and all of our side still to run. See inbox.md T46 "Continue 2" for how to resume.
- Handoff package code exists (`scripts/build_handoff.py`, `scripts/handoff_evaluate.py`).
- kubectl works again (checked 2026-11-17 15:05); no ltg pods or jobs in `ecepxie`.
- PR #35 (LAB runner can use the vLLM pod) merged; PR #37 (`scripts/autopilot.sh`) merged.

## Milestones
- [x] M0 Bootstrap: docs in `docs/autopilot/`, loop script PR #37, label `needs-sirui`, lab-mate issue #36 (old #20 closed)
- [ ] M1 `ltg batch` command
- [ ] M2 At least 20 v2 tasks, labelled (ours seeds 46-53, lab mate 500-507)
- [ ] M3 LAB baseline frozen and scored; v2 tasks through LAB's tool
- [ ] M4 Generator passes EVALUATION.md levels 1-3 (or hardened until it does)
- [ ] M5 250 tasks on the passing version, test split at least 30
- [ ] M6 Usefulness pilot fine-tune
- [ ] M7 Handoff package and notes for Pengtao
- [ ] M8 Docs current, STATUS: DONE

## Running jobs
- v2 generation batch, seeds 46-53, `configs/pilot_generate_v2.toml`, folders `runs/pilot<seed>_v2`, labels deferred.
  Script `.inbox/2026-11-17-gen-v2/generate.sh` (copy of the 2026-11-10 one), PID 59738 (caffeinate), log
  `runs/gen-v2-2026-11-17.log`, stop file `runs/.gen-v2-2026-11-17.stop`. Started 15:06; guess ~1 h per seed, done
  around midnight. Commits each seed to main by itself (`commit_round.py`, git lock `runs/.git-commit.lock`).

## Next
1. M1 `ltg batch`: build it in a worktree while the batch runs (code only, fake backend tests, no model calls).
2. When the batch ends: read every rejection, then M2 step-budget check (label config 28 steps vs v2's 40), then label.
3. Daytime after labelling: finish the LAB sample in chunks of ~8 (one heavy Opus job at a time).

## Needs Sirui
- Someone with legal training to read 10 tasks (EVALUATION.md level 1, human check). Not blocking batches.

## Decisions
- 2026-11-17: start the v2 batch at 15:00 instead of waiting for night: it is the only heavy Opus job, and M1 work is light.
- 2026-11-17: the autopilot replaces the planning-chat-plus-inbox flow (Sirui She does not want to decide each step).
- 2026-11-17: our seeds 46-499, the lab mate's 500-999; his work reaches main only through PRs the autopilot merges.
- 2026-11-17: one heavy Opus job at a time on Sirui She's plan, since the 2026-11-11 limit pile-up.

## Lab mate
- Issue to post in M0: `.inbox/2026-11-17-autopilot/LAB_MATE_ISSUE.md` (v2 generation, seeds 500-507, labels later).
- Issue #36 posted 2026-11-17. Status: not started.
