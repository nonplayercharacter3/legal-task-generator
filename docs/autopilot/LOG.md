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
