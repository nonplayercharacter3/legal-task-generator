STATUS: RUNNING

# Autopilot state

Plain-words picture of where the project is. The autopilot reads this first and rewrites it last, every iteration.
Keep it under about 150 lines; history goes to LOG.md.

Last updated: 2026-11-21 12:20, autopilot iteration 18.

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
- kubectl login expired again on 2026-11-18 (issue #43); no ltg pods or jobs were left in `ecepxie` on 2026-11-17.
- PR #35 (LAB runner can use the vLLM pod) merged; PR #37 (`scripts/autopilot.sh`) merged.
- PR #38: `ltg label` uses the larger of the label config's and the run's step budget (v2: 40), and records it in
  `labelled_by.solver_max_steps`. Seed 45 was labelled with 28 (its attempts took 17 actions, so the cap did not bite).

## Milestones
- [x] M0 Bootstrap: docs in `docs/autopilot/`, loop script PR #37, label `needs-sirui`, lab-mate issue #36 (old #20 closed)
- [x] M1 `ltg batch` command: PR #39 (tests in `tests/test_batch.py`, README section); lab mate told on #36
- [x] M2 At least 20 v2 tasks, labelled: 30 accepted (s45-s60), 24 labelled by 2026-11-18
- [ ] M3 LAB baseline frozen and scored; v2 tasks through LAB's tool
- [ ] M4 Generator passes EVALUATION.md levels 1-3 (or hardened until it does)
- [ ] M5 250 tasks on the passing version, test split at least 30
- [ ] M6 Usefulness pilot fine-tune
- [ ] M7 Handoff package and notes for Pengtao
- [ ] M8 Docs current, STATUS: DONE

## Running jobs
- LAB regrade `regrade2.py` (PID 67923, output `runs/lab_sample/regrade2.out`), started 11:06 by Sirui She's session:
  hit the usage limit at 11:30, resumed 12:05 on the credit-lending task (114 criteria); 9 more after it.
- Chained after it: `runs/lab_sample/chain_v2.sh` (PID 78677, output `runs/lab_sample/chain_v2.out`): a second
  regrade pass (the sanctions task, re-run at 11:34, was judged into the limit: 10 errored scores still), then
  `scripts/lab_sample.py run ours_v2` (20 v2 tasks, Qwen solve then judge, 202 criteria), then a last regrade pass and
  `check.py`. Expected end about 15:30, later if a limit hits.
- LAB side: 30 of 30 attempted; 20 scored cleanly, 10 to re-judge (sanctions among them).
- `sample.json` now has set `ours_v2` (PR #48): s504-m0003, s506-m0003, s45-m0003, s53-m0002, s55-m0001,
  s55-m0003, s58-m0002 (all dev and test), plus 13 train drawn by seed 46; 7 are the lab mate's, unlabelled yet.
  Old sample kept as `runs/lab_sample/sample.before_v2.json`. The 20 v1 `ours` rows are not run (v1 is superseded).

## v2 numbers (seeds 45-61, ours; lab mate 500-507)
- Lab mate's seeds 500-507: 20 of 24 accepted, on main (PR #45, #46), not labelled yet. Rejections, read 2026-11-21:
  s501-m0003 consistency (drafter's lookback runs from the event, ledger says the claim; correct, same as s59-m0001),
  s503-m0001 issue_check (two-document issue findable from the schedule alone; correct), s507-m0001 ledger_schema
  (a 21-word fact; correct), s502-m0002 issue_check (detect term "delivered on August 3, 2026" not verbatim in SOW
  No. 2; likely false, the drafter wrote "delivered the ... Module on August 3, 2026"; documents are on his machine
  only). Paraphrased detect terms: 1 in about 70 v2 matters, fix only if it recurs.
- Ours: 33 accepted, labels 0.00: 15, 0.33: 7, 0.67: 9, 1.00: 2, mean 0.31.
- Seeds 45-60: 30 accepted of 46 matters; seeds 54-60 (after PR #40): 16 of 21. Rejections 54-60, all read: s54-m0001 and
  s59-m0001 consistency (drafter added a qualifier that changes the fact: a governing-law proviso, a lookback from
  the event not the claim; correct), s56-m0003 issue_check (two-document issue findable from one; correct),
  s59-m0003 ledger_schema (all issues in one document; correct), s60-m0002 issue_check (false: the verifier used the
  real date; fixed in PR #42). issue_check losses 8 of 24 before PR #40, 2 of 21 after.
- Labels (24): 0.00: 10, 0.33: 6, 0.67: 7, 1.00: 1, mean 0.32; items passed 90.7%.
- EVALUATION level 2 (`scripts/dataset_stats.py`, 30 tasks): documents median 8 (pass), instruction 71.5 words
  (pass), naming every file 0% (pass), two-document problems 64% (pass), industries 23 (pass), folder words median
  15,704 (MISS, needs 20,000), checklist median 10 (soft miss, needs 20).

## Next
1. When `chain_v2.out` says "chain done": check `check.py` shows every s1 row clean (LAB 30 and ours_v2 20); if not,
   run `regrade2.py` again. Then re-run `scripts/lab_sample.py run ours_v2` (it skips scored tasks and rewrites
   `summary.json` over all rows), commit `summary.json`, write both sides into `docs/research/lab_harness.md` (M3 done).
2. Label the lab mate's 20 tasks (`ltg label`, runs/lm_s500-507_v2) after the chain (one heavy job at a time).
3. M4: apply EVALUATION.md levels 1-3 with M3's numbers. Known level 2 misses: folder words median 15,704 (needs
   20,000), checklist median 10 (needs 20). Candidate v3: longer folders and more checklist items in one change.
4. Then write the lab mate's next work order in #36 (v2 or v3), test-run in a scratch clone first.
5. If an NRP call stalls a batch (no log line for an hour outside a wait), add a wall-clock cap per solver call.

## Needs Sirui
- When all jobs are done for good: remind Sirui She to undo `sudo pmset -a disablesleep 0` (#44, closed 2026-11-21).
- Issue #43: kubectl login expired (waits for a browser sign-in; checked 2026-11-18 13:45). Needed for the vLLM
  fallback and M6, not for batches. Close once `kubectl get pods -n ecepxie` answers. Never run kubectl without a
  time cap until then: it hangs.
- Someone with legal training to read 10 tasks (EVALUATION.md level 1, human check). Not blocking batches.

## Decisions
- 2026-11-18: M2 met; the two consistency rejections where the drafter added a meaning-changing qualifier stay
  rejections (the answer key must match the documents); fix only if the class grows.
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
- Done: v2 batch seeds 500-507, 20 of 24 accepted (his comment on #36, 2026-11-21 02:41 PST). Seed 500 via PR #45;
  501-507 sat on his branch with no PR because `ltg batch` cached the first PR as open: autopilot opened and merged
  PR #46, fixed the tool in PR #47, told him on #36. Current order (2026-11-21): label his seeds 500-507.
  When he is done, post his next order in the same iteration (PROMPT.md "Never leave him idle").
