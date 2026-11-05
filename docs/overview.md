# Legal Task Generator Overview

High-level picture for people, kept current as the project moves (updated 2026-11-04, night). Working detail for Claude
Code sessions is in `CLAUDE.md` ("Now"); the plain-English history of rounds is in `docs/stage_and_plan.md`.

## What we're building

We are building a machine that writes LAB-like practice assignments, so other agents can be trained on them and do
better on Harvey's LAB benchmark. The generator itself is model-neutral: it makes sound assignments and labels how hard
each one is; whoever trains picks the slice that fits their model.

Each assignment looks like work a partner hands a junior lawyer: an instruction ("review these contracts for our
client"), a folder of invented contracts and letters, and a strict pass/fail checklist. The machine writes the answer
key first, so we always know what a correct answer must find.

The "agent" is that machine: a chain of AI roles, each with one job (plan the matter, draft documents, write the
checklist, check the work), plus a test-taker that tries each assignment. LAB is used only as the final exam, never
copied from.

How the parts fit:

```
The machine (working today)
  Plan:   Opus invents a matter and writes the answer key first
    -> Build:  Opus drafts the documents, instruction and checklist
    -> Check:  8 checks; Qwen tries 3 times, kept if it passes 1 or 2

Training and testing (ahead)
  Export:     kept assignments become training files (built)
    -> Fine-tune: Qwen trains on them on Nautilus A100s
    -> LAB exam:  score Qwen before and after training, compare
```

## The steps

Eight steps take us from an empty repo to a trained model; the first four are built, the last four are not started.

1. **Build the machine with a fake model.** Every stage and check runs offline, so the plumbing can be tested for
   free. *Done (October).*
2. **Run it on real models and fix what breaks.** Small test rounds of 3 assignments each; every mistake found becomes
   a fix before the next round. *Done for phase 1 (October 18), and continuing.*
3. **Label difficulty instead of filtering on it.** Test models try each assignment 3 times and their pass rates are
   recorded on the assignment; only a pass without the documents (a leak) still rejects it. *Decided November 4; queued.*
4. **Package assignments as training files.** A standard chat-style format with the checklist attached for grading.
   *Merged November 4.*
5. **Measure Qwen on LAB before training.** The "before" score, so we can show improvement. *Feasibility checked November 4: LAB's tool can run Qwen with no code changes;
   grading needs a small add-on for our own judge, plus a few installs on the laptop.*
6. **Scale up.** Move from a handful of assignments to hundreds. *Not started.*
7. **Fine-tune Qwen** on the assignments, most likely by handing them to the lab's own post-training agent, which picks
   the method, writes the training code and runs it on a GPU. *Not started.*
8. **Measure Qwen on LAB again** and compare with step 5. *Not started.*

## Where we are

We are between steps 3 and 5: the machine works end to end on real models, and 7 assignments have passed every check,
all screened against LAB's text.

- **Blocked:** since November 2 the account has lost access to the lab's Nautilus space and to the university's hosted
  Qwen, so no Qwen runs can happen. Pengtao has been asked to restore access.
- **Not blocked:** preparing the LAB run (step 5).
- **Waiting on a person:** a read-through of the two newest assignments, and someone with legal training to review the
  list of planted problems.

## Decided

The shape of the machine is settled; these choices hold unless Sirui She reopens them.

| Area | Decision | Why |
| --- | --- | --- |
| Ground truth | Answer key first: facts and 3 to 5 planted problems, each tied to a document and section; everything else is written from it | We know the right answer by construction instead of trusting a model's judgment |
| Relation to LAB | Same shape, our own content; every assignment screened against LAB's text; LAB used only as the final exam | Keeps the test honest; a reviewer pushed back on leaning on LAB |
| Scope | Contract review: commercial and M&A deals, Delaware and New York law | Narrow enough to get right first |
| Who sees what | Each AI role gets only what its job needs (the test-taker never sees the answer key), enforced in code | Prevents answers leaking into the assignment |
| Quality checks | Eight automatic checks, cheapest first: consistency, problems findable, no hints, checklist traces to the key, checklist unit-tested, LAB overlap, then the test-taker | Broken assignments are dropped early and cheaply |
| Author model | Claude Opus, through the Max subscription (Agent SDK), never pay-per-token API calls | Pengtao's direction; fixed, reimbursed cost |
| Difficulty | A label, not a filter: test models (Qwen 27B for now) try each assignment 3 times and their pass rates are stored with it; never-passed assignments are flagged for review | The generator serves any trainer; each picks the band that fits its model, and no sound assignment is thrown away |
| Compute | Nautilus A100 GPUs, running Qwen with vLLM; the university's hosted Qwen as the faster option | Free for research; we control it |
| Format | Plain files (Markdown, JSON) at every stage; standard-library Python | Anyone can inspect any stage by hand |
| Workflow | Plan in the Claude app, code in the Claude Code terminal, tasks handed over through `inbox.md`; one worktree per task, main checkout always clean | Keeps work traceable and the repo tidy |

## Still open

Most open questions are about training, and most wait on Pengtao.

| Question | Options | Who decides |
| --- | --- | --- |
| How do we train? | Leaning: the lab's AIBuildAI post-training agent (`aibuildai-inc/aibuildai-llm-posttrain-agent`). It takes a task folder (task statement, training data, a grader script) and chooses the method itself. Open: which machine runs it (it needs a Linux GPU box with systemd and bubblewrap, which a Nautilus pod may not provide) | Pengtao |
| Which model will the lab train first? | The lab agent's examples use small base models (Qwen3 1.7B to 4B, one H100 for 10 hours); if that is the target, add it as a labelling test model | Pengtao (heads-up, not a blocker) |
| How many LAB tasks to grade? | Decided: our own Claude judge through the SDK, per Pengtao's no-API rule (scores comparable only to our own runs; the judge is about 40 lines of code). Open: grading 50 tasks is roughly 2,900 judge calls, a large share of a day's Max limit, so how big a sample | Sirui She |
| How many assignments do we need? | Depends on the training method; at least hundreds | Pengtao and Sirui She |
| How do we make assignments harder if needed? | Longer folders, more problems that only show across two documents | Sirui She, after the next rounds |
| Who checks the legal substance? | A lawyer or law student reviews the problem list and grades a few answers | Sirui She to find someone |
| Real contracts as drafting examples? | Pull public agreements from SEC filings (code exists, parked) or keep invented ones | Sirui She |
| Expand beyond contract review? | Other practice areas later | Later, once scale works |
