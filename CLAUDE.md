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
- **Backend-agnostic.** Any OpenAI-compatible endpoint. Lab GPUs with open models (vLLM) is the likely target;
  not confirmed yet.

## Current status (2026-10-14)

- All three stages and eight gates run end to end with the offline fake model (`ltg/fake.py`).
- 31 offline tests pass (`python3 -m pytest`). Each gate was mutation-checked: disabling it makes a test fail.
- The real-model path has only been tested against a local mock server. **It has never run on a real LLM.**
- `ltg/data/precedents/` holds three short synthetic samples, not real agreements.
- The issue library in `ltg/taxonomy.py` is a draft and has not been reviewed by anyone with legal training.

## Known weaknesses (review findings, highest priority first)

1. **Sequential model calls.** ~20 to 25 calls per matter, all serial, matters serial too. Matters are independent:
   run them concurrently (thread pool), with a configurable concurrency limit.
2. **Long documents returned inside JSON.** The drafter returns a full contract as a JSON string; real models often
   break escaping on long outputs. Have the drafter (and other long-text roles) return raw Markdown instead.
3. **Solver is not agentic.** All documents are pasted into one prompt. LAB evaluates agents that open and search
   files with tools, so the difficulty filter does not measure the right thing yet. Consider a tool-using solver
   (list_files, read_file, search) behind the same `solve()` interface.
4. **No resume.** A crash restarts the whole run. Cache per-stage outputs per matter and skip completed stages.
5. **Decontamination index rebuilt every run.** Save the Bloom filter to disk keyed by reference dirs and settings.
6. **Grading can be biased.** The judge receives `hints`, which may make it lenient; the issue verifier receives
   the exact `detect_terms`, which weakens it as a check. Make both optional and measure the difference.

Smaller known gaps: no EDGAR fetcher (precedents come from local folders), no diversity tracking across a run,
judge not calibrated against lawyer grades.

## How to verify changes

- `python3 -m pytest` must stay green. Add a test for every new gate or behaviour; if you change a gate, check that
  disabling it still makes a test fail.
- `python3 -m ltg run --config configs/fake_demo.toml` then read `runs/fake_demo/report.md`. The demo injects
  faults into ~30% of matters; consistency, issue_check, rubric_trace, rubric_tests and solver_check
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
