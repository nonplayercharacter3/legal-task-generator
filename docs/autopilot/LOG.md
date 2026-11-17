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
