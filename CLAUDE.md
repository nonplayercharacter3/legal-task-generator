# CLAUDE.md

Context for any Claude Code session working in this repo. Read this first, then README.md.

## What this project is

Professor Pengtao Xie (AIBuildAI lab, UCSD) asked for an agent that automatically creates training data
similar to Harvey's Legal Agent Benchmark (LAB): long-horizon legal tasks made of a partner-style instruction,
a folder of matter documents, and an all-pass rubric. This repo is the preliminary implementation. The lab works
on LLM post-training; the goal is training data for legal agents, with LAB used only for evaluation.

## Decisions already made (don't relitigate without asking Sirui She)

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
  direct API calls. He confirmed this means the Max plan; Sirui She upgrades on the web after the App Store Pro period
  ends on 2026-10-30 (the App Store price is $124). Until then, real-model rounds wait. For GPUs, Nautilus (namespace `ecepxie`, see Current status). The runtime stays standard library only: the SDK
  is an optional extra (`pip install -e ".[claude]"`) imported only by that backend.

## Current status (2026-10-18)

- All three stages and eight gates run end to end with the offline fake model (`ltg/fake.py`).
- 85 offline tests pass (`python3 -m pytest`). Every gate, and each branch of `rubric_tests` and `solver_check`,
  was mutation-checked on 2026-10-14: disabling it makes a test fail.
- First real-model runs (2026-10-15, Claude Sonnet through the Agent SDK, one matter each, seed 1):
  runs 1 to 3 were rejected at `consistency`, each exposing a gap the fake model hid (exact string matching, facts
  written as clauses, references extracted as values, a contradiction pinned on the fact's own document); all fixed.
  Run 4 was accepted: 4 documents (3,925 words), 4 issues, 11 criteria, solver pass rate 1/3, 54 calls,
  ~313k input and ~56k output tokens, ~8 minutes of model time. Output in `runs/claude_test4/` (not committed).
- Pilot observations to follow up: the solver found every planted issue in every attempt and failed only on
  negative criteria, so issue spotting may be too easy when Sonnet solves Sonnet's tasks (try a different solver
  model); issue criteria often bundle find, explain and fix; the instruction writer can still nudge generically
  ("the documents may not line up").
- 3-matter pilot (2026-10-15, `configs/claude_pilot.toml`): 0 of 3 accepted, all three rejections correct. Two failed
  consistency on compatible added detail; one had a rubric criterion needing ledger-only background and an unplanted
  precedence conflict between documents. Prompts fixed in 8d01772; not yet rerun. 69 calls, ~346k input
  and ~93k output tokens, ~12 minutes of model time, no errors on the Pro plan.
- Pilot rerun (2026-10-17, `runs/claude_pilot2`): 0 of 3 again, with new causes only (the first round's did not
  recur): a forward reference in a term sheet judged a conflict; a detect term missed through Markdown bold; an
  issue verifier that saw only one document while the issue depended on a letter of intent in another; and a
  distractor drafted without seeing the order form, so their part numbers disagreed. Fixed in the next commit;
  not yet rerun. 66 calls, ~323k input and ~120k output tokens, ~16 minutes of model time, no errors.
- Cloud pilot (2026-10-18, five rounds of 3 matters, Opus generating, seeds 1 to 5, results under `runs/cloud_pilot*`
  on branch `claude/wonderful-bardeen-ecwx4o`; round 1 is on `pilot-results/cloud-opus-1`): **phase 1 standard met
  in round 5**, 2 of 3 accepted (solver pass rates 0.67 and 0.33), both read in full against the checklist.
  Accepted by round: 0, 1, 1, 0, 2. Defect classes fixed between rounds, one commit each: negative criteria that
  punished comments on distractors; fact keys not tied to an instrument (an NDA's own Effective Date); an
  instruction writer guessing document contents, the governing law and how to review; planted issues defused by
  their own drafting; one issue moving several facts (governing law and forum); added drafting detail around a
  fact (customary definition items, a fallback court); deadlines tied to "today"; detect terms that were document
  names; an issue verifier not told who the client is (last fix, not yet run).
  Rounds 2 to 4 used Sonnet as solver, which found every planted issue in 3 of 6 sound tasks; from round 5 Haiku
  solves (Sirui She's decision), as the closer reference for the open models the lab trains. 847 calls, ~11.9M input
  and ~2.1M output tokens over the five rounds, no errors, no usage limit hit.
- Nautilus (2026-10-18): Sirui She can read the lab namespace `ecepxie` through kubectl with UCSD login
  (`~/.kube/config` from https://nrp.ai/config; never commit it or any token). Read-only checks only, nothing run yet.
  **New pods are blocked:** the unscoped quota `reached-quota` is set to `pods: 0` (it was 200), most likely an NRP
  admin freeze. Ask Li Zhang or the NRP admins why and how to lift it before planning GPU work. Once lifted, the
  namespace may hold up to 12 A100s at once, requested as `nvidia.com/a100` (opportunistic pods excepted), and no
  H100, H200 or GH200 (quota 0). The cluster lists 31 nodes with whole A100 80GB cards (22 SXM4, 9 PCIe; most at
  SDSC, SDSU, Missouri); counts are nodes, not cards. Plan: serve a ~8B Qwen with vLLM first, then ~30B, then
  fine-tune.
- LAB screen on (2026-10-18): `reference_dirs = ["../harvey-labs"]` (clone `harveyai/harvey-labs` beside the repo; never
  commit it). The index reads LAB's .docx/.xlsx/.pptx/.eml as well as text, and counts only wording found in a single
  LAB task (`decontam_group_depth = 3`): without that, standard clauses shared across LAB tasks pushed our own sound
  documents to 0.56, over the 0.5 cutoff.
- NRP hosted models (2026-10-18): `https://ellm.nrp-nautilus.io/v1`, OpenAI-compatible, key from the NRP portal in
  `NRP_LLM_API_KEY` (never in the repo or chat). `qwen3-small` is Qwen3.8-27B dense, the planned solver
  (`configs/pilot_nrp_solver.toml`); no ~8B Qwen chat model is hosted. Limits: 200k output tokens/min per key and model,
  8 simultaneous requests for qwen3-small; non-commercial use only. The HTTP client now retries dropped connections
  and waits as long as a 429 asks. Running it from a cloud session needs `ellm.nrp-nautilus.io` allowed in the
  environment's network settings and the key set as an environment variable there.
- **Running pilot rounds (laptop or cloud).** One-time setup, about 40 minutes, no model calls:
  `python3 -m venv .venv && .venv/bin/pip install -e ".[dev,claude]"`; clone LAB beside the repo with
  `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/harveyai/harvey-labs ../harvey-labs`; build the index
  with `.venv/bin/python -m ltg index --config configs/pilot_nrp_solver.toml` (~35 min, saved in `runs/.decontam_cache`,
  reused until LAB changes); check it with `.venv/bin/python scripts/check_lab_index.py`. On a laptop the NRP key must
  be exported in `~/.zshenv` (not only `~/.zshrc`, which non-interactive shells skip). Claude calls go through the SDK on
  the laptop's Claude Code login. In the cloud, the environment's setup script runs `scripts/cloud_setup.sh` (setup script:
  `cd /home/user/legal-task-generator && bash scripts/cloud_setup.sh; true`), which does the same in the background
  and logs to `/tmp/lab-index.log`; the environment allows `ellm.nrp-nautilus.io` and sets
  `NRP_LLM_API_KEY`. Then: `.venv/bin/python -m ltg run --config configs/pilot_nrp_solver.toml --seed <new> --out runs/<name>`.
- Grouped LAB index verified (2026-10-18, built by `scripts/cloud_setup.sh` in 41 minutes, 419M n-grams, 1.5% false
  positives): LAB excerpts score 0.97 to 1.00, our 4 accepted tasks 0.05 to 0.10 (ungrouped: 0.31 to 0.56, one over
  the 0.5 cutoff). `scripts/check_lab_index.py` repeats this check.
- Variety (2026-10-18, not yet run on a real model): the client was "Halvorsen" or "Harrowgate" in 10 of 12 pilot
  matters, and the same folder shapes and issue types recurred. The sampler now picks each matter's industry (30, none
  repeated before all are used), a made-up name stem per party (the validator enforces it, and rejects names in
  `taxonomy.OVERUSED_NAMES`), the supporting document kinds by practice area, and issue types weighted against those
  already used in the run. The report's Variety section lists industries, agreement and issue types, party names used
  in more than one matter, and identical issue sets. Issue types stay uneven where pools differ by practice area.
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

## Pilot standard (phase 1 exit)

Phase 1 ends when one round meets every point below. Each round is 3 fresh matters
(`configs/claude_pilot_opus.toml`, a new `--seed` each round so prompts are never tuned to one set of matters).

1. At least 2 of 3 matters accepted, and the run logs no model errors.
2. Every accepted task passes the quality checklist under "How to verify changes", read in full by a person:
   instruction realistic, free of hints and free of claims the documents contradict; each planted issue findable
   where the ledger says and a genuine problem for the client; every criterion traces to the ledger and a thorough,
   correct memo would pass it; gold passes and flawed fails the right criteria; documents read like real drafting.
3. Every rejection in the round is read and its cause written up. A false rejection (a gate wrong about a sound
   task) counts as a defect to fix even when the round reaches 2 of 3.
4. `python3 -m pytest` is green and `configs/fake_demo.toml` still rejects at least one matter at each gate it
   used to.

Between rounds: fix the root cause of every defect class seen, one commit per class, then run the next round.
Stop and ask Sirui She if a round hits the usage limit or after 5 rounds without meeting the standard.

## Known weaknesses (highest priority first)

1. **Judge leniency not measured.** `gates.judge_hints` exists; run the same matters on a real model with it on
   and off and compare solver pass rates before choosing a default.
2. **Solver context grows with the folder.** The transcript keeps every page read (~30k tokens for five long
   documents). If a model's window is too small, drop old page text and keep the solver's own notes.
3. **Short folders make the agentic solver read everything.** With 3 to 5 short documents the tool-using solver
   behaves like the old one-prompt solver. The difficulty filter only bites once folders get longer or larger.
4. **LAB index takes ~30 minutes to build.** LAB is ~455M words (mostly .docx); the index is saved under
   `runs/.decontam_cache` and reused while LAB is unchanged, but a fresh cloud container must rebuild it.

Smaller known gaps: no EDGAR fetcher (precedents come from local folders),
judge not calibrated against lawyer grades, `solver_attempts = 1` rejects every task (a pass rate of 0 or 1 is
always outside the band), and one fact lives in one document, which limits cross-document reasoning.

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
- **Git:** commits authored by Sirui She only (author name exactly `Sirui She`), with no Claude co-author, "Generated with"
  or other AI attribution lines in commit messages or PR descriptions.
