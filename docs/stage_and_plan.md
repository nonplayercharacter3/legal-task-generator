# Where the project stands and what comes next

Plain-English summary for people joining the project (updated 2026-10-27). The working detail for Claude Code
sessions is in `CLAUDE.md` ("Now"); this page says the same thing without the jargon.

## What we are building

A tool that writes practice assignments for AI models that do legal work. Each assignment looks like something a
law-firm partner gives a junior lawyer: "Review these contracts for our client and tell me what's wrong." It comes
with a folder of made-up contracts and letters, and a strict pass/fail checklist for grading the answer.

The tool hides the problems in the contracts on purpose, and writes the answer key before anything else, so we
always know what a correct answer must find. Professor Pengtao Xie's lab at UCSD will use these assignments to train
open-source models. Harvey's Legal Agent Benchmark (LAB) is the yardstick we test against later, never a source we
copy from: every assignment is checked against LAB's text to make sure none of it leaked in.

## Where we are

**Phase 1 is done.** In mid-October we ran five test rounds of three assignments each. Claude's strongest model
(Opus) wrote them, a smaller Claude model tried to solve them, and the tool threw away any assignment that was
broken, gave away the answer, or was too easy or impossible. Each round exposed a new kind of mistake, which we fixed
before the next. Round 5 kept 2 of 3 assignments, which was our bar for "the tool works", and a person read both in
full and confirmed they hold up.

**Ready for the next rounds.** Sirui She's laptop has everything a round needs (the LAB copy and its search index,
access to the university's hosted models). A second contributor with a Claude Max plan has joined and runs the
Claude rounds on their own machine.

## What comes next

1. **Round 6 (second contributor, now).** The same setup as round 5. It is the first real test of two changes:
   a fix to one of the quality checks, and more variety in the assignments (before, the same client names and
   contract types kept coming back).
2. **Get an open model to finish its answers (Sirui She, at the same time, no Claude needed).** The point of the
   project is assignments that a mid-sized open model finds hard but possible. We tried the university's hosted Qwen
   model (about 27 billion parameters, free for research) as the solver on the four assignments we already have.
   It handled the hands-on part well: it opened the files, read every page and decided when it was done, in all 12
   tries. Then every try failed at the very last step. It "thinks" at great length before writing, then writes an
   overly long memo, and runs out of room partway through. See "Fixing the open model's memo" below.
3. **Round 7.** The first full round with Qwen as the solver, once step 2 works.
4. **Check the grader.** A model grades each answer against the checklist. We have not measured whether it is too
   generous. We will grade the same answers with and without the extra hints it gets, and compare.
5. **Our own GPUs.** The university cluster (Nautilus) has unfrozen our account, and we may use up to 12 high-end
   GPUs at once. Next we run our own copy of an open model there, then train it on the assignments.

## Fixing the open model's memo

**What goes wrong.** Before writing, the model "thinks" privately, and by default NRP runs it at its highest
thinking setting. It thinks for about 30,000 tokens, which uses up almost all of the 32,000-token room the call
allows, so the memo gets cut off. The memo itself is not the problem: it is about as long as the memos Claude's
Haiku wrote for the same assignments.

**What we tried (2026-10-27).** We replayed the failing step 4 times under each of 8 settings and counted how many
of the planted problems each finished memo named (a rough check, not our real grader):

| Setting | Memos finished | Problems named | Time per memo |
|---|---|---|---|
| Current setup | 0 of 4 | n/a | 5 to 8 min |
| More room (64k tokens) | 4 of 4 | 20 of 20 | 7 to 11 min |
| Ask for a shorter memo | 4 of 4 | 19 of 20 | 3 to 6 min |
| Thinking turned off | 4 of 4 | 15 of 20 | under 1 min |
| Thinking capped at 12k tokens | 4 of 4 | 19 of 20 | about 4 min |
| Medium thinking effort | 4 of 4 | 19 of 20 | about 2 min |
| **Low thinking effort** | **4 of 4** | **20 of 20** | **about 2 min** |

**Recommended fix: set the solver's thinking effort to low** (`reasoning_effort = "low"`, a setting NRP documents).
Every memo finished with room to spare, none missed a planted problem, and each took about 2 minutes instead of
timing out. Turning thinking off is faster but misses problems, which would make the open model look weaker than it
is. Asking for shorter memos would change the assignment for every model, not just this one.

To apply it, the code needs a small option to pass this setting to the solver, then the full test (12 attempts) runs
again. Full sources and numbers: `docs/research/qwen_memo_length.md`.

**One more correction from the research.** NRP limits each key to 48,000 output tokens per minute, not the 200,000
our notes said. Rounds with Qwen solving should run fewer memo calls at once; the client already waits when NRP
says to slow down.

## Decisions waiting on Sirui She

- Approve the recommended fix for the open model's memo (low thinking effort, see above).
- Merge or drop an older, unfinished feature that pulls real contracts from SEC filings to use as drafting examples
  (branch `claude/affectionate-perlman-e65dbe`).
- Commit or keep local the setup files for running a model on Nautilus (`deploy/nautilus/`).
- Whether the second contributor commits under their own name; the repo rule says only Sirui She authors commits.

## How we work together

- Sirui She and the second contributor coordinate through GitHub: issues for questions and requests, pull requests
  for results. Each test round goes on its own branch with a pull request listing its numbers and why each rejected
  assignment was rejected.
- Several Claude sessions on Sirui She's laptop share one notes file, `HANDOFF.md`, which only that laptop has.
