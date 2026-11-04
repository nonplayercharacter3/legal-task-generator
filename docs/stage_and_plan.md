# Where the project stands and what comes next

Plain-English summary for people joining the project (updated 2026-11-03). The working detail for Claude Code
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

**November 2: eight more rounds, run in two parallel streams on Sirui She's laptop** (now on the Claude Max plan).
Opus wrote every assignment; what differed was who tried to solve them.

- **Claude Haiku solving** (rounds 6, 8, 9): 1 of 9 kept. Three were rightly turned away as too easy, because Haiku
  found every problem in all three tries. The other five each exposed a flaw in how assignments are built or checked,
  and each flaw is fixed. By the last round every assignment passed every quality check; the only thing left is
  difficulty. The variety change worked: nine industries, no repeated names.
- **Qwen solving** (rounds 7 to 11), the open model the lab will actually train: round 9 kept 2 of 3 with no errors,
  which meets our bar on the numbers; Sirui She still has to read those two in full. The other rounds kept none.
  Most rejections were the tool being wrong about a sound assignment, and each kind was fixed before the next round.
  In rounds 10 and 11 the university's hosted model service started refusing every request, which cost 3
  assignments.

So far the tool has kept **7 assignments** in total (4 in October, 3 in November). Every November assignment was
checked against LAB's text, and none came close to the cutoff.

**One mix-up to know about.** Both streams used the same random seeds for rounds 8 and 9, so those are the same six
assignment outlines written twice, not twelve different ones. Later rounds will use new seeds.

**The two streams' work was combined on 2026-11-03.** Both had fixed some of the same problems in slightly different
ways; the combined version keeps one copy of each fix, and every test still passes.

## What comes next

1. **Sirui She reads the two Qwen-round assignments** kept in round 9. If they hold up, the standard is met with Qwen
   solving.
2. **Qwen sets the difficulty bar (decided 2026-11-03).** The lab trains open models like Qwen, so an assignment
   counts as too easy only if Qwen solves it every time. Haiku stays available for comparison.
3. **More rounds**, with new seeds. Qwen rounds need the hosted service back, or our own copy on
   the university GPUs, which works but is about 3.5 times slower.
4. **Train on the assignments.** Not started. Seven assignments are far too few, so the generator has to scale first.

**Done along the way (2026-10-27 to 2026-11-02):**
- **The open model now finishes its answers.** See "Fixing the open model's memo".
- **The grader is checked.** We graded 67 answers twice, with and without the grader's extra hints: the results were
  the same (92% of checklist items passed either way). A second, more careful grader agreed with every pass the first
  one gave. We keep the hints. Both graders are Claude models, so this is not yet a check against real lawyers.
- **Our own GPUs work.** We ran the same Qwen model on one of the university cluster's GPUs (Nautilus). It wrote all
  12 test answers with no failures and scored the same as the hosted copy, but took about 9 minutes per answer
  instead of 2.5.

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
- Reading the two assignments kept in Qwen round 9.

## How we work together

- Sirui She and the second contributor coordinate through GitHub: issues for questions and requests, pull requests
  for results. Each test round goes on its own branch with a pull request listing its numbers and why each rejected
  assignment was rejected.
- Several Claude sessions on Sirui She's laptop share one notes file, `HANDOFF.md`, which only that laptop has.
- Planning happens with Claude in the Claude app; coding happens in the Claude Code terminal on the laptop. The app
  hands the terminal its tasks through `inbox.md` in the project folder.
- The main project folder always stays clean: each piece of work happens in its own copy (a git worktree) and is
  removed once it is merged.
