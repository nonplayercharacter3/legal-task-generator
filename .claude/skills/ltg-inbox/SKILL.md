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
3. **Keep the main checkout clean.** It stays on `main` with an empty `git status`. Do the work in a worktree:
   `git worktree add ../ltg-wt/<branch> -b <branch> <base>`. Never switch the main checkout's branch.
4. Follow the task's steps exactly. Do not widen scope. If a step fails, a check does not match what the task
   expects, or a decision is marked for Sirui She, set the status to `blocked`, write why in the Report, and stop.
5. Commits: author `Sirui She <shesirui1902@gmail.com>`, with no Claude co-author, "Generated with" or other AI
   attribution, in commits or PR descriptions. One commit per change.
6. Finish:
   - Write the **Report** under the task: what you did, test counts, commits, PR link, numbers asked for, anything odd.
   - Set the status to `done`.
   - Append a short entry to `HANDOFF.md` (format in its rules).
   - Remove any worktree whose branch has merged.
   - Check `git status` in the main checkout is empty.
7. Tell the user in two or three lines what finished and what the report says, and that the planning session can
   read it.
