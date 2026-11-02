# Where the project stands and what comes next

Plain-English summary for people joining the project (updated 2026-11-02). The working detail for Claude Code
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
2. **Get an open model to finish its answers (done 2026-10-27).** The point of the project is assignments that a
   mid-sized open model finds hard but possible. The university's hosted Qwen model (about 27 billion parameters,
   free for research) handled the hands-on part well from the start, but every answer got cut off at the last step.
   With the fix below it finished all 12 test answers. See "Fixing the open model's memo".
3. **Rounds with Qwen solving (2026-11-02).** Five rounds (7 to 11). Round 9 kept 2 of 3 assignments with no
   errors, which meets our bar on the numbers; a person still has to read those two in full. The other rounds kept
   none. Most rejections were the tool being wrong about a sound assignment, and each kind was fixed before the next
   round; the rest were fair (Qwen missed something, or the hidden problem undid itself). In rounds 10 and 11 the
   university's hosted model service started refusing every request, which cost 3 assignments.
4. **Check the grader (done 2026-11-02).** We graded 67 answers twice, with and without the grader's extra hints:
   the results were the same (92% of checklist items passed either way). A second, more careful grader agreed with
   every pass the first one gave. We keep the hints. Both graders are Claude models, so this is not yet a check
   against real lawyers.
5. **Our own GPUs (serving done 2026-11-02).** We ran the same Qwen model on one of the university cluster's GPUs
   (Nautilus). It wrote all 12 test answers with no failures and scored the same as the hosted copy, but took
   about 9 minutes per answer instead of 2.5. Next: train it on the accepted assignments.

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

**Applied and retested (2026-10-27).** We added the option and reran the full test: all 12 attempts wrote a memo,
each attempt took 2 to 6 minutes, and the rough check found 47 of the 51 planted problems. The one it kept missing
(in all three tries on one assignment) is a supply agreement that lets the other side hand the contract to a
competitor. Full sources and numbers: `docs/research/qwen_memo_length.md`.

**One more correction from the research.** NRP limits each key to 48,000 output tokens per minute, not the 200,000
our notes said. Rounds with Qwen solving should run fewer memo calls at once; the client already waits when NRP
says to slow down.

## Decisions waiting on Sirui She

- Merge or drop an older, unfinished feature that pulls real contracts from SEC filings to use as drafting examples
  (branch `claude/affectionate-perlman-e65dbe`).
- Whether the second contributor commits under their own name; the repo rule says only Sirui She authors commits.

## How we work together

- Sirui She and the second contributor coordinate through GitHub: issues for questions and requests, pull requests
  for results. Each test round goes on its own branch with a pull request listing its numbers and why each rejected
  assignment was rejected.
- Several Claude sessions on Sirui She's laptop share one notes file, `HANDOFF.md`, which only that laptop has.
