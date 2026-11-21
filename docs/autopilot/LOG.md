# Autopilot log

Dated, append-only. One entry per iteration.

## 2026-11-17 iteration 1
- M0: copied PROMPT, EVALUATION, STATE to `docs/autopilot/`; created label `needs-sirui`; posted lab-mate issue #36
  (v2, seeds 500-507) and closed #20 (v1 work order for the same seeds, never run). inbox.md marked superseded, T46
  moved to autopilot.
- PR #37 `scripts/autopilot.sh` (header comment now points at `scripts/`), CI green, merged.
- PR #35 (LAB runner `LAB_BASE_URL`, `LAB_MODEL_NAME` for the vLLM pod; default unchanged): read the 4-line diff, CI
  green, merged.
- kubectl works again (pods in `ecepxie` list); nothing of ours running there.
- Started the v2 generation batch, seeds 46-53, PID 59738, log `runs/gen-v2-2026-11-17.log`.
- PR #38 (label step budget), PR #39 (`ltg batch`, 7 tests, README) reviewed, CI green, merged; 157 tests pass on
  main. First CI run of #39 failed (branch test committed without an author on a runner with no git identity); fixed
  in the same PR. Commented on #36 with the `ltg batch --branch` command for the lab mate.
- CLAUDE.md "Now" and docs/overview.md note the autopilot and `ltg batch`.

## 2026-11-17 16:35, iteration 2
- Sirui's note (lab mate `aarushnarayanan` now a collaborator): rewrote issue #36's body as his current work order
  for `ltg batch` and assigned it to him. Every command in it was first run from a scratch clone
  (`/tmp/ltg-labmate-test`, origin a local bare repo) on `configs/fake_demo.toml`: batch over seeds 500-501 with
  `--no-label --branch lm/test-throwaway --author ...` committed one commit per seed to the branch and pushed;
  the stop file stopped it (exit 1); a rerun skipped finished seeds and ran 502; the
  `--author "$(git config user.name) <$(git config user.email)>"` form worked; `ltg index` with the v2 config hit the
  cache in 7 s. Only `gh pr create` could not be tested (local remote), so the issue gives the manual fallback.
- Added "Lab mate work order" to PROMPT.md (checked every iteration), his username to CLAUDE.md, a Lab mate section
  to STATE.md.
- v2 batch: seeds 46 (1 of 3) and 47 (3 of 3) committed; seed 48 running; ~30 min per seed.

## 2026-11-17 18:30, iteration 3
- Sirui's note (lab mate confused by #36): rewrote the body's top with a "For Aarush: start here" block (log in,
  open `claude` in an empty folder, paste one sentence, leave the laptop on; ~40 min setup, 30 to 60 min per seed).
  NRP key now "not needed" (labels deferred; `ltg/models.py` sends no Authorization header when the key is empty).
  Per-seed comments dropped: only "started" and "ended or failed"; seed numbers come from the PR's commits.
  "Last updated" now uses the real time (18:26 PST). Deleted my 23:19 UTC comment (it pointed at the old shell
  loop) and commented what changed. No new commands, so nothing new to test-run.
- PROMPT.md lab-mate rules: the work order opens with a human "start here" block; never ask him for steps that need
  someone watching or credentials the step does not use.
- v2 batch: seeds 46 to 49 committed (1, 3, 3, 1 of 3); seed 50 running; ~49 min per seed, end ~21:40.

## 2026-11-17 20:10, iteration 4
- v2 batch seeds 46-53 ended 19:53: 13 of 24 accepted (1, 3, 3, 1, 1, 2, 1, 1), labels deferred, all committed.
- Read all 11 rejections. 8 at issue_check, all the same class: a two-document issue the solo verifier found from
  one document (s46-m0002 I6, s49-m0003 I2, s50-m0002 I6, s50-m0003 I1, s51-m0003 I3, s52-m0001 I4, s52-m0002 I3,
  s53-m0003 I2). Correct: one half was already a bad clause on its own (one-sided assignment, overbroad exclusivity,
  narrow warranty, uncapped assumption, a "notwithstanding" override). 3 at consistency: re-asked the matcher twice
  on the 3 pairs (6 Opus calls, `/tmp/ltg-probe/matcher.py`): s46-m0001 (forum, extractor dropped "which have
  exclusive jurisdiction") and s49-m0001 (survival, stated word for word plus Buyer's own) came back same both
  times, so false; s53-m0001 (Losses with a third-party carve-back) different both times, correct.
- PR #40 (merged, CI green, 158 tests, fake demo unchanged): consistency asks the matcher again on pairs it called
  different and keeps its reasons in gates.json; the ledger writer tests each half of a two-document issue alone.
- Started labelling seeds 46-53 (PID 66636), queued seeds 54-61 behind it (waiter PID 71591).
- Issue #36 header now says main b78f204, with a comment that the fixes are on main; his command is unchanged.

## 2026-11-17 23:26, iteration 5
- Labeller PID 66636 made no progress after 22:14 (s49-m0002, attempt 3; attempt 2 had taken 47 min). NRP answered
  a tiny request in 0.9 s at 23:28, so the connection was dead, not NRP. At 23:27 the process ended from outside this
  session (someone else killed it; no finally ran) and left `runs/.batch.lock`; the 54-61 waiter (71591) then found
  the lock and exited at 23:27:58. Removed the empty lock folder and started one batch: `--seeds 54-61,49-53`
  (PID 35148, log `runs/gen-v2-54-61.log`), so the night goes to generation and seeds 49-53 get labelled after.
- Seeds 46-48 were labelled with 40 solver steps (PR #38, `labelled_by.solver_max_steps`).
- v2 labels so far (s45-s48, 8 tasks): 0.00: 3, 0.33: 2, 0.67: 2, 1.00: 1 (mean 0.38; v1 rounds 20-27 mean 0.42).
- Open question: the `max_seconds` check runs only when a line arrives, and the 600 s socket timeout did not fire
  either, so one call can stall a batch indefinitely. Fix if it recurs.

## 2026-11-18 04:32, iteration 8
- Iterations 6 and 7 (03:32, 04:02) hit the 5-hour limit at once and did nothing.
- The batch (PID 35148) had labelled seeds 54-56 and generated 57 (54: 2, 55: 3, 56: 2, 57: 3 of 3 accepted), then
  hit the usage limit labelling seed 57 at 02:36 and slept 106 min. At 03:41 the planning chat's watchdog
  (`~/.claude/jobs/14386149/tmp/watchdog.sh`: kill a batch whose log is silent 60 min) killed it, which left
  `runs/.batch.lock` (default SIGTERM skips `finally`). This is probably also how PID 66636 died at 23:27.
- Removed the lock, restarted: `ltg batch --config configs/pilot_generate_v2.toml --label-config
  configs/pilot_nrp_solver.toml --seeds 57-61,49-53` (PID 40471, same log).
- PR #41 (merged, CI green, 159 tests): `_wait` sleeps in 10-minute steps with a log line and a stop-file check each,
  and SIGTERM exits through `finally` so the lock is removed.
- v2 so far: 24 accepted (s45-s57), 15 labelled, mean pass rate 0.33 (0.00: 6, 0.33: 4, 0.67: 4, 1.00: 1).

## 2026-11-18 12:13, iteration 10
- Iteration 9 (08:56) hit the usage limit. The watchdog killed batch 40471 at 08:51 while it waited out a 105-min
  limit on seed 61 (pre-PR #41 code). Removed `runs/.batch.lock`, moved the errored seed 61 folder to
  `runs/_trash/2026-11-18/pilot61_v2`, restarted `--seeds 61,49-53` (PID 38866) on main 627e862.
- Read all 5 rejections of seeds 54-60 (16 of 21 accepted); 1 false (s60-m0002, verifier used the real date to call
  a 2025 survival window lapsed). PR #42 (merged, CI green, 160 tests) adds the rule to ISSUE_VERIFIER.
- M2 done: 30 v2 accepted, 24 labelled, mean 0.32. Level 2 stats: only folder length misses (15,704 vs 20,000).
- `git push --delete` hung (killed); deleted the merged branch through `gh api` instead.
- Issue #36 header bumped to 119b8dd.
- kubectl hung on an expired OIDC login; opened needs-sirui issue #43.
- s61-m0002 errored at 13:56: "Your computer went to sleep mid-response" (lid closed? caffeinate -i stops only idle sleep). The batch retries errored matters on its next try.

## 2026-11-19 12:12, iteration 11
- Loop restarted 12:12 (it had not run since 2026-11-18 14:14). Batch 38866 died: the laptop slept, all 3 seed 61
  matters errored "computer went to sleep mid-response" (13:56, 15:15), and the watchdog killed it at 15:15 (log
  silent 76 min). The watchdog itself is gone. Opened needs-sirui #44 (lid open while jobs run).
- M3 started: froze the LAB side in `docs/autopilot/lab_sample.md` (30 tasks, 1,927 criteria; 12 scored, 0 errors).
  Started LAB chunk 1 (8 tasks, 541 criteria) with `runs/lab_sample/chunk_lab.py` (LAB rows only), PID 95600.
- Seed 61 and labels for 49-53 wait for the evening, so the LAB run is the only heavy Opus job.
- Issue #36 matches STATE (main has moved only by docs since 119b8dd); lab mate has not started.

## 2026-11-19 17:00, iteration 12
- LAB chunk 1 (PID 95600) finished, but all 8 tasks' judging hit the 5-hour limit ("resets 3:30pm"): 409 criteria
  errored, the Qwen runs themselves completed. Errored scores.json copied to `runs/_trash/2026-11-19/lab_s1_errored/`.
- New `runs/lab_sample/regrade.py` (local, gitignored): `lab_run.py --judge-only` per errored task, one at a time,
  stops if errors recur. Started PID 11811.
- Moved `runs/pilot61_v2` (3 matters lost to laptop sleep) to `runs/_trash/2026-11-19/pilot61_v2_slept`.
- Chain `runs/lab_sample/tonight.sh` (PID 13075): regrade, then `chunk_lab.py 10` (last 10 LAB tasks), then
  `ltg batch --seeds 61,49-53`. One heavy Opus job at a time.
- Lab mate: no activity on #36 since 2026-11-18; work order still matches main's code (only docs commits since 119b8dd).

## 2026-11-19 21:05, iteration 13
- Regrade of LAB chunk 1 fixed 4 tasks, then hit the 5-hour limit again at 17:2x ("resets 8:30pm"); chunk 2's 10 LAB
  runs completed with Qwen but 9 of them judged into the same limit. Now 17 of 30 LAB rows clean, 13 errored
  (~874 criteria). The LAB judge makes one Opus call per criterion with the full memo, about 250 to 400 per window.
- Seed 61 generated 3 of 3 (150d94a, by the batch); the batch is labelling 61, then 49-53.
- New `runs/lab_sample/regrade2.py` (local): waits for the reset named in the error and retries, instead of stopping.
  `morning.sh` (PID 46874) starts it once the night chain (13075) ends, so it does not compete with labelling.
- Lab mate: no activity on #36 since 2026-11-18; no code changes since 119b8dd, so the work order still matches.

## 2026-11-20 18:50, iteration 14
- Laptop slept from 2026-11-19 22:09 (clamshell, battery) to 2026-11-20 18:25: labelling of seed 51 hung 20 hours,
  then both solver calls timed out; `ltg batch` waits 30 min and retries. Commented on issue #44.
- Labels landed overnight before the sleep: s61 (0.67, 0.00, 0.00), s49-m0002 0.00, s50-m0001 0.67.
- Lab mate started seeds 500-507 at 18:01; PR #45 (seed 500, 3 of 3 accepted, 52 files, only runs/lm_s500_v2,
  run-output rule kept, CI green) reviewed and merged.

## 2026-11-20 21:30, iteration 15
- Laptop slept at 19:02 on battery (pmset: dark wakes only since), during seed 51's label retry (attempt 2 of 3).
  Batch PID 10390 and morning chain 46874 alive but stalled. Commented on #44. No lab-mate PR open (seed 500 merged;
  his batch started 18:01, PID 61989 on his machine). No code or result changes this iteration.

## 2026-11-21 07:35, iteration 16
- Night chain finished 22:19: labels for seeds 51-53 committed. Our 33 v2 tasks all labelled (0.00: 15, 0.33: 7,
  0.67: 9, 1.00: 2, mean 0.31).
- LAB regrade2: 3 of 13 clean, then the 5-hour limit at 22:30 (32 errors on one task, retried after the wait); the
  laptop slept on battery overnight, so the wait is still pending.
- Lab mate finished seeds 500-507: 20 of 24 accepted. Seeds 501-507 had no PR (PR #45 merged mid-batch and
  `ltg batch` never re-checked). Opened and merged PR #46 (runs/lm_s50*_v2 only, CI green), fixed `ltg batch` in
  PR #47 (open_pr after every push), commented on #36.
- PR #47 merge first failed on a dropped connection; the cleanup chain then deleted the branch and closed the PR. Restored the branch from 7cbb101, reopened, CI green, merged. Lesson: cleanup only after a confirmed merge (`&&`, not `;`).

## 2026-11-21 11:20, iteration 17
- Laptop woke 10:55 (slept on battery overnight). The LAB regrade (PID 55990) was stuck in its usage-limit wait, which
  counts only awake time; restarted (Sirui She's session restarted it at the same minute with a wall-clock wait fix, PID 67923, output in `regrade2.out`; kept that one), 10 errored s1 scores to re-judge.
- Found one LAB sample task with no score at all: technology control plan scenario-02, Qwen run died on
  `APIConnectionError` during sleep. Chained a full re-run after the regrade (`rerun_sanctions.sh`, PID 69249); partial
  output to `runs/_trash/2026-11-21/lab_s1_connerror/`.
- Read the lab mate's 4 rejections (seeds 501, 502, 503, 507): 3 correct (known classes), 1 likely false
  (s502-m0002, paraphrased detect term in the second document; first case in about 70 v2 matters; not fixed yet).
- 2026-11-21 12:15 (Sirui She's session): issue #36 rewritten as the lab mate's next work order, labelling his seeds
  500-507 (20 tasks, all label_pending, 0 errors) on his machine, branch `lm/v2-s500-507-labels`; STATE Next 2 updated.
