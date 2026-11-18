STATUS: RUNNING

# Autopilot state

Plain-words picture of where the project is. The autopilot reads this first and rewrites it last, every iteration.
Keep it under about 150 lines; history goes to LOG.md.

Last updated: 2026-11-17 23:35, autopilot iteration 5.

## Goal
A one-command batch tool (`ltg batch`) that builds a dataset of LAB-like contract-review tasks, with the tasks shown
to be sound, LAB-like and useful for training (EVALUATION.md), at least 250 of them, handed to the lab's post-training
agent. Full definition of done: PROMPT.md.

## Where things are (2026-11-17)
- Pool: 101 accepted tasks. 87 are v1 (too easy and too small next to LAB); 14 are v2 (s45-m0003, plus 13 from
  seeds 46-53: 1, 3, 3, 1, 1, 2, 1, 1 of 3), the 13 being labelled now.
- v2 batch rejections (11 of 24), all read: 8 at issue_check, a two-document issue findable from one document
  (correct; the ledger writer planted a one-sided clause as one half); 3 at consistency, 2 false (matcher noise,
  s46-m0001, s49-m0001) and 1 correct (s53-m0001). Both classes fixed in PR #40 (merged), from seed 54 on.
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
- One batch, PID 35148 (caffeinate), log `runs/gen-v2-54-61.log`, started 23:30: generates seeds 54-61 on
  `pilot_generate_v2.toml` with Qwen labels after each seed, then labels the 6 unlabelled tasks of seeds 49-53.
  ~70 min per seed: generation ends ~09:00 on 2026-11-18, labels ~10:30. Commits each seed to main itself.
- The earlier labeller (PID 66636) hung on one NRP call from 22:14 to 23:27 (s49-m0002 attempt 3) and was then
  killed from outside this session, leaving a stale `runs/.batch.lock`; the queued 54-61 waiter hit the lock and
  exited. Lock removed, everything restarted as one batch. Seeds 46-48 labelled (8 tasks), 49-53 not yet.

## Next
1. Check the batch at ~03:30 (a stuck NRP call can stall it: no log line for over an hour means stuck). If it
   happens again, add a hard wall-clock cap per solver call (the 3600 s `max_seconds` check did not end this one).
2. When seeds 54-61 end: read every rejection; check the PR #40 fixes cut the issue_check and consistency losses
   (before: 8 and 3 of 24). M2 is met at 20 labelled v2 tasks.
3. Labels so far, v2 (8 tasks, s45 to s48): 0.00: 3, 0.33: 2, 0.67: 2, 1.00: 1, mean 0.38. v1 rounds 20-27: mean
   0.42. Not clearly harder yet; judge again with all 20+.
4. In the day (2026-11-18), after the batch: finish the LAB sample (M3) in chunks of ~8 (inbox.md T46
   "Continue 2"), then put v2 tasks through LAB's tool.

## Needs Sirui
- Someone with legal training to read 10 tasks (EVALUATION.md level 1, human check). Not blocking batches.

## Decisions
- 2026-11-17: issue_check rejections for a two-document issue findable alone stay rejections (v2 is meant to be
  harder); fixed upstream in the ledger writer instead of relaxing the gate.
- 2026-11-17: chain seeds 54-61 right after labelling so the night is used; still one heavy job at a time.
- 2026-11-17: start the v2 batch at 15:00 instead of waiting for night: it is the only heavy Opus job, and M1 work is light.
- 2026-11-17: the autopilot replaces the planning-chat-plus-inbox flow (Sirui She does not want to decide each step).
- 2026-11-17: our seeds 46-499, the lab mate's 500-999; his work reaches main only through PRs the autopilot merges.
- 2026-11-17: one heavy Opus job at a time on Sirui She's plan, since the 2026-11-11 limit pile-up.

## Lab mate
- GitHub `aarushnarayanan`, collaborator since 2026-11-17. Work order: **body of issue #36** (assigned to him),
  rewritten 2026-11-17 16:35 for `ltg batch`, and 18:26 with a "For Aarush: start here" block, no NRP key, and only
  two comments (started; ended or failed) (seeds 500-507, `configs/pilot_generate_v2.toml`, `runs/lm_s{seed}_v2`,
  `--no-label`, `--branch lm/v2-s500-507`); every command test-run on the fake backend in a scratch clone first.
- On: not started. Last seen activity: none yet. Open PR: none. Header bumped to main b78f204 at 20:05 (PR #40 note).
