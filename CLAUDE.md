# CLAUDE.md

Context for any Claude Code session working in this repo. Read this first, then README.md.

## What this project is

Professor Pengtao Xie (AIBuildAI lab, UCSD) asked for an agent that automatically creates training data
similar to Harvey's Legal Agent Benchmark (LAB): long-horizon legal tasks made of a partner-style instruction,
a folder of matter documents, and an all-pass rubric. This repo is the preliminary implementation. The lab works
on LLM post-training; the goal is training data for legal agents, with LAB used only for evaluation.

## Decisions already made (don't relitigate without asking Syrena)

- **Ledger-first design.** For each invented matter, write the answer key first (facts plus 3 to 5 planted issues,
  each tied to a document and section), then generate documents, instruction, rubric and reference answers from it.
  Ground truth is known by construction, not judged by a model.
- **Similar to LAB in shape, not content.** Our own taxonomy and issue library. Never use LAB tasks as seeds,
  examples or templates. Screen generated tasks against LAB text (n-gram containment). LAB stays fully held out.
  A reviewer (Ruiyi) has previously pushed back on work that leans too heavily on LAB specifically.
- **Start with contract review** (commercial and M&A agreements, Delaware and New York law).
- **Isolation is enforced in code** by what goes into each role's payload: the instruction writer never sees the
  issues, the solver sees only the instruction and documents, the judge sees only a response and the rubric.
  Keep it that way; `tests/test_pipeline_fake.py` checks it.
- **Skeleton first, costing later.** Pengtao approved a preliminary implementation. No cost modeling yet.
- **Backends.** Any OpenAI-compatible endpoint, or Claude through the Claude Agent SDK (`backend.kind = "claude_sdk"`).
  Pengtao's direction (2026-10-15): for Claude, use the $100/month subscription through the SDK (reimbursed), never
  direct API calls. For GPUs, Nautilus; ask Li Zhang for access. The runtime stays standard library only: the SDK
  is an optional extra (`pip install -e ".[claude]"`) imported only by that backend.

## Current status (2026-10-14)

- All three stages and eight gates run end to end with the offline fake model (`ltg/fake.py`).
- 66 offline tests pass (`python3 -m pytest`). Every gate, and each branch of `rubric_tests` and `solver_check`,
  was mutation-checked on 2026-10-14: disabling it makes a test fail.
- The real-model paths have only been tested against a local mock server and a stub SDK. **No full matter has run on
  a real LLM yet.** First real Claude call (2026-10-15) failed at login: run `claude` and `/login` first.
- `ltg/data/precedents/` holds three short synthetic samples, not real agreements.
- The issue library in `ltg/taxonomy.py` is a draft and has not been reviewed by anyone with legal training.

Fixed after the 2026-10-14 independent review (one commit each):
- Drafter, solver and answer writer reply in raw Markdown, not JSON strings. The client rejects output cut off
  at `max_tokens` (`finish_reason: length`) and strips `<think>` blocks.
- A rerun no longer leaves rejected matters in `accepted/`. A run into a folder holding another run's matters stops.
- `consistency` checks every fact in every document. Issues that contradict a fact on purpose name it in `contradicts`.
- The exported rubric carries the hints the judge used (`gates.judge_hints` turns them off). The issue verifier no
  longer sees `detect_terms` (`gates.verifier_sees_terms`). Code checks the terms appear verbatim instead.
- `leak_check` also scans filenames and document kinds (punctuation ignored) and rejects HTML comments in documents.
- `rubric_tests` requires the flawed answer to pass every criterion except those for its omitted issue.
- The report shows decontamination as skipped, with a warning, when `reference_dirs` is empty.
- Matters run concurrently (`run.concurrency`, default 4).
- The solver is agentic (`ltg/solver.py`): it gets the file list and works through `read_file` (paged) and `search`
  tool calls, one JSON action per step, then writes its memo in raw Markdown. Plain JSON over `complete()`, not
  native tool calling, so any endpoint works. Each attempt's trace is saved as `solver/attempt_N.trace.json`.
  This raises solver calls from 1 to about (pages read + 2) per attempt, roughly doubling calls per matter.
- `ltg run --resume` keeps matters that already have a verdict and retries those that ended in an error. It refuses
  if `settings.json` in the output folder differs (run size, concurrency and folder may change). Resume is per
  matter, not per stage: a crash loses only the matters in flight. Ctrl-C no longer waits for queued matters.

## Known weaknesses (highest priority first)

1. **Judge leniency not measured.** `gates.judge_hints` exists; run the same matters on a real model with it on
   and off and compare solver pass rates before choosing a default.
2. **Solver context grows with the folder.** The transcript keeps every page read (~30k tokens for five long
   documents). If a model's window is too small, drop old page text and keep the solver's own notes.
3. **Short folders make the agentic solver read everything.** With 3 to 5 short documents the tool-using solver
   behaves like the old one-prompt solver. The difficulty filter only bites once folders get longer or larger.
4. **Decontamination index rebuilt every run.** Probably fine since LAB is small; time it before adding a cache.

Smaller known gaps: no EDGAR fetcher (precedents come from local folders), no diversity tracking across a run,
judge not calibrated against lawyer grades, `solver_attempts = 1` rejects every task (a pass rate of 0 or 1 is
always outside the band), dropped connections (`ConnectionResetError`) are not retried, and one fact lives in one
document, which limits cross-document reasoning.

## How to verify changes

- `python3 -m pytest` must stay green. Add a test for every new gate or behaviour; if you change a gate, check that
  disabling it still makes a test fail.
- `python3 -m ltg run --config configs/fake_demo.toml` then read `runs/fake_demo/report.md`. The demo injects
  faults into ~35% of matters; consistency, issue_check, leak_check, rubric_trace, rubric_tests and solver_check
  should each reject at least one.
- For real-model work: run 3 to 5 matters first and read every output before scaling.
- Quality checklist for a generated task: instruction realistic and does not hint at issues; each planted issue
  is findable where the ledger says; every rubric criterion traces to the ledger; gold passes, flawed fails the
  right criteria; documents read like real drafting.

## Conventions

- Python 3.11+, standard library only at runtime (pytest for dev). Keep it that way unless there's a clear reason.
- Every file that passes between stages is plain JSON or Markdown on disk, so any stage can be inspected by hand.
- Writing style for docs, README and messages: direct, no em dashes.
- **Git:** commits authored by Syrena only (`Syrena(Sirui) She`), with no Claude co-author, "Generated with"
  or other AI attribution lines in commit messages or PR descriptions.
