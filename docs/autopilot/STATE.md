STATUS: RUNNING

# Autopilot state

Plain-words picture of where the project is. The autopilot reads this first and rewrites it last, every iteration.
Keep it under about 150 lines; history goes to LOG.md.

Last updated: 2026-11-17 18:30, autopilot iteration 3.

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
- PR #38: `ltg label` uses the larger of the label config's and the run's step budget (v2: 40), and records it in
  `labelled_by.solver_max_steps`. Seed 45 was labelled with 28 (its attempts took 17 actions, so the cap did not bite).

## Milestones
- [x] M0 Bootstrap: docs in `docs/autopilot/`, loop script PR #37, label `needs-sirui`, lab-mate issue #36 (old #20 closed)
- [x] M1 `ltg batch` command: PR #39 (tests in `tests/test_batch.py`, README section); lab mate told on #36
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
  `runs/gen-v2-2026-11-17.log`, stop file `runs/.gen-v2-2026-11-17.stop`. Started 15:06; ~45 min per seed (46: 1, 47: 3, 48: 3, 49: 1 of 3
  committed; 50 running at 18:25), so done around 21:30. Commits each seed to main by itself (`commit_round.py`, git lock `runs/.git-commit.lock`).

## Next
1. When the batch ends (wait file set on its PID): read every rejection of seeds 46-53 (false ones become defect fixes
   by PR), then label them: `ltg batch --config configs/pilot_generate_v2.toml --seeds 46-53` (finished seeds are
   skipped, pending tasks labelled, label commits go to main). One heavy job at a time: not while generation runs.
2. After labelling: finish the LAB sample (M3) in chunks of ~8 (inbox.md T46 "Continue 2" says how).
3. Later batches use `ltg batch`, not the `.inbox/` scripts.

## Needs Sirui
- Someone with legal training to read 10 tasks (EVALUATION.md level 1, human check). Not blocking batches.

## Decisions
- 2026-11-17: start the v2 batch at 15:00 instead of waiting for night: it is the only heavy Opus job, and M1 work is light.
- 2026-11-17: the autopilot replaces the planning-chat-plus-inbox flow (Sirui She does not want to decide each step).
- 2026-11-17: our seeds 46-499, the lab mate's 500-999; his work reaches main only through PRs the autopilot merges.
- 2026-11-17: one heavy Opus job at a time on Sirui She's plan, since the 2026-11-11 limit pile-up.

## Lab mate
- GitHub `aarushnarayanan`, collaborator since 2026-11-17. Work order: **body of issue #36** (assigned to him),
  rewritten 2026-11-17 16:35 for `ltg batch`, and 18:26 with a "For Aarush: start here" block, no NRP key, and only
  two comments (started; ended or failed) (seeds 500-507, `configs/pilot_generate_v2.toml`, `runs/lm_s{seed}_v2`,
  `--no-label`, `--branch lm/v2-s500-507`); every command test-run on the fake backend in a scratch clone first.
- On: not started. Last seen activity: none yet. Open PR: none.
