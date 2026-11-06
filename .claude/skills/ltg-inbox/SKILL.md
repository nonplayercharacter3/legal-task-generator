---
name: ltg-inbox
description: Work through the legal-task-generator repo's own task list, inbox.md at the repo root, which the planning session writes. Use when asked to do the next inbox task, a task by number (T1, T2...), or to check this repo's inbox.
---

# Work the legal-task-generator inbox

This skill belongs to this repo only. **Never use the user-level `/inbox` skill here**: it points at a different
project's folder.

## Where things are

- Task list: `inbox.md` at the root of the main checkout, `~/Projects/legal-task-generator/inbox.md`. Gitignored,
  one copy: from a worktree, always read and edit it at that absolute path, never a copy.
- Attachments for a task: `~/Projects/legal-task-generator/.inbox/<task folder>/` (also gitignored).
- Session log: `~/Projects/legal-task-generator/HANDOFF.md`.
- Project context: `CLAUDE.md` in the repo.

## Steps

1. Read `inbox.md` in full, then `CLAUDE.md`. If the user named a task (T3), take it; otherwise take the top task
   whose status is `open` and whose prerequisites ("after T1") are `done`. If none qualifies, say so and stop.
2. Set the task's status to `in progress` in `inbox.md`.
3. **Keep the main checkout clean.** It stays on `main` with an empty `git status`. Never switch its branch.
   - **Code changes** (anything under `ltg/`, `tests/`, `configs/`, `scripts/`, `deploy/`, `.github/`, or
     `pyproject.toml`): work in a worktree (`git worktree add ../ltg-wt/<branch> -b <branch> <base>`), push, open a
     PR into `main`, do not merge. The planning session reviews and merges.
   - **Round results** (the run-output rule's files in `CLAUDE.md`), `docs/`, `README.md` text and `CLAUDE.md`
     "Now": commit directly to `main` from the main checkout (`git pull --ff-only` first, commit, `git push`), then
     check CI on that commit with `gh run list --limit 1`. A pilot round still runs in a worktree; afterwards its
     results are committed to `main` from the main checkout, with the round's numbers and rejection causes in the
     commit message instead of a PR. If a push is refused or CI fails, set `blocked` and report.
   - Never mix code and results in one commit.
4. Follow the task's steps exactly. Do not widen scope. If a step fails, a check does not match what the task
   expects, or a decision is marked for Sirui She, set the status to `blocked`, write why in the Report, and stop.
5. Commits: author `Sirui She <shesirui1902@gmail.com>`, with no Claude co-author, "Generated with" or other AI
   attribution, in commits or PR descriptions. One commit per change.
6. Finish:
   - Write the **Report** under the task: what you did, test counts, commits, PR link or the commit on `main` with
     its CI result, numbers asked for, anything odd.
   - Set the status to `done`.
   - Append a short entry to `HANDOFF.md` (format in its rules).
   - Remove any worktree whose branch has merged.
   - Check `git status` in the main checkout is empty.
7. Tell the user in two or three lines what finished and what the report says, and that the planning session can
   read it.
