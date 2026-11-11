# LAB's harness, and Qwen run through it (T46, 2026-11-11)

Plan step 3: score Qwen (`qwen3-small`, Qwen3.8-27B) with LAB's own run-and-grade tool, on LAB tasks and on ours, with
one setup for both. Code: PR #33 (`scripts/to_lab_format.py`, `scripts/lab_run.py`, `scripts/lab_sample.py`).
Only command and field names of LAB are quoted here.

Status: the harness runs end to end and the smoke is done. **The 50-task sample was not run**: its judge-call
projection is 2,554, over the 2,000 limit in the task. Sirui She decides how to cut it (below).

## Setup

- Installed with `brew install podman pandoc` (podman 6.2.0, pandoc 3.13; the older pandoc 2.12 from anaconda would
  shadow it, so runs put `/opt/homebrew/bin` first on PATH), `podman machine init` and `start` (5 CPUs, 2 GB), no sudo.
  The sandbox image `ghcr.io/harveyai/lab-sandbox:latest` (1.8 GB) was pulled and tagged `lab-sandbox:latest`.
- `lab-core` 1.3.0 is pip-installed from `../harvey-labs` into `runs/lab_venv`, with `claude-agent-sdk`. LAB declares no
  `httpx`, which its `meta` adapter imports at load time: install it by hand (`pip install httpx`).
- LAB root is `runs/lab_root` (`LAB_ROOT`): `tasks/<area>` are symlinks to `../harvey-labs/tasks/<area>`, our converted
  tasks are under `tasks/ours/`, results under `results/`. Nothing in `../harvey-labs` is written.

## How LAB works

- **Task folder:** `tasks/<area>/<task>[/<scenario>]/` with `task.json` and `documents/`. Fields: `title`,
  `work_type`, `tags`, `instructions`, `deliverables` (output filename to name), `criteria`. A criterion has `id`,
  `title`, `match_criteria` ("PASS if ... FAIL if ..."), `deliverables` (which output files the judge sees), optional
  `sources`. No gold answer. Documents are real .docx/.xlsx/.pptx. 2,010 tasks, about 57 criteria each.
- **Run** (`python -m lab_core.harness.run --model <provider/model> --task <id>`): a tool-calling agent loop (up to 200
  turns, we cap at 60) in a per-task podman container (no network), tools `bash`, `read`, `write`, `edit`, `glob`,
  `grep`, `finish`, plus skill manuals for .docx/.xlsx/.pptx. The instruction is the first user message; a fixed
  system prompt describes the workspace. Output goes to `results/<run-id>/output/`, with `transcript.jsonl`,
  `metrics.json`.
- **Model call:** one adapter per provider, native tool calling. The OpenAI adapter uses the **Responses API**, which
  NRP does not serve (empty-message error on `/v1/responses`). LAB's `baseten` adapter is a plain `/v1/chat/completions`
  adapter driven by `BASETEN_BASE_URL` and `BASETEN_API_KEY`; NRP's chat endpoint returns native `tool_calls` for
  Qwen. We use it, pointed at NRP, and add `reasoning_effort = "low"` (as in our solver config; the adapter's own
  switch only sets `enable_thinking`, which leaves NRP at its default "xhigh") and drop the reply's reasoning text
  from the history. Not hosted on the vLLM pod path: `/v1/responses` was not needed.
- **Grade** (`python -m lab_core.evaluation.run_eval`): one judge call per criterion (LAB's `rubric_criterion` prompt:
  task title, the output files named by the criterion, criterion title, `match_criteria`; reply `verdict` and
  `reasoning`). The default is **two judges** (Sonnet 4.6 and GPT-5.5) averaged; `--judges MODEL` uses one. A .docx
  deliverable is read as text with pandoc 3.5 or later on the host. Score is all-pass (1 only if every criterion
  passes), with `n_passed` and `n_criteria` as the diagnostic.
- **Deliverable:** whatever `deliverables` names; LAB's prompt tells agents to use `write` for plain Markdown and the
  skills for .docx. Most LAB tasks ask for .docx.
- **Needs at run time:** podman with a started machine, the sandbox image, pandoc 3.5+ for grading, a model key, a
  judge key (replaced here).

## Our glue (all in `scripts/`, PR #33)

- Judge: `SdkJudge` subclasses LAB's `Judge`; `evaluate()` sends LAB's own filled-in prompt to Opus through the Claude
  Agent SDK (Max plan, no API) and parses LAB's JSON. One judge in place of the pair, the same for both sets. LAB's
  prompt does not know our `claim_made` convention: a negative criterion is written as "PASS if the memo does not make
  the following claim", and the judge answers `verdict` directly. That is a different judge from the one in `ltg`.
- `to_lab_format.py` writes a matter folder as a LAB task: documents copied as they are (Markdown), instruction plus
  "Output: `memo.md`", one criterion per rubric line (`match_criteria` from `kind` and `text`; hints and ledger left
  out). **Deliverable is `memo.md`, not .docx**: LAB accepts any deliverable name, `write` produces Markdown natively,
  and no pandoc is needed to read it. This differs from the task text ("ask for .docx"); a .docx variant would also test
  Qwen's use of the docx skill, which the LAB tasks already do. Say so if you want it.
- `lab_run.py` runs one task and grades it; `lab_sample.py` draws (seed 46) and runs 4 at a time.

## Smoke (2 LAB tasks, 2 of ours, plus one rerun of ours)

Qwen on NRP at `reasoning_effort = low`, judge Opus; 5 runs, 0 grading errors, 113 judge calls, 1.11M input and
137k output Qwen tokens, 22 minutes of agent time in total (3 to 5.5 minutes per task, 4 in parallel), judge about
1.4 s per call.

| Task | Criteria passed | Turns | Qwen in / out tokens | Agent time | Judge calls |
|---|---|---|---|---|---|
| corporate-ma/compare-pa-vs-commitment-letter | 16 / 37 | 9 | 449k / 35k | 330 s | 37 |
| corporate-ma/review-proposed-acquisition-nda/scenario-01 | 47 / 48 | 13 | 346k / 23k | 231 s | 48 |
| ours s20-m0001 (label 0.33), first try | 2 / 9 | 4 | 54k / 31k | 297 s | 9 |
| ours s20-m0001, `max_tokens` 32000 | 8 / 9 | 8 | 155k / 31k | 307 s | 9 |
| ours s20-m0002 (label 0.33) | 10 / 10, all-pass | 7 | 107k / 17k | 180 s | 10 |

- The first try of s20-m0001 ended on turn 4 with no memo: the reply was cut at 16,000 tokens while Qwen was still
  thinking (turn 3 alone spent 14.9k at "low"), so no tool call and nothing written. `max_tokens` is now 32,000 and the
  rerun finished cleanly. Expect some of this on long matters even so.
- Read one graded result of each. LAB NDA task: C-042 failed with a counted reason (13 of 18 issues tied to the client,
  80% needed), a specific, sensible fail. Ours s20-m0002 C11 (negative) passed with the reason that the memo notes
  consent and an exception and does not claim the quoted wrong claim. The judge reasons look sensible on both sets.
- The compare task wrote a .docx through the skills, so Qwen can produce LAB's deliverable format; 16 of 37 there.
- s20-m0001 and s20-m0002 both carry the stored label 0.33 (1 of 3 on our own solver) and scored 8/9 and 10/10 here
  on a single attempt; one attempt cannot tell a harness difference from noise.

## The 50-task sample: projection and decision

`scripts/lab_sample.py draw` (seed 46) drew 20 LAB tasks from corporate-ma and contracts, 10 from other areas, and 20 of
ours (5 per label 0, 0.33, 0.67, 1.0; pool sizes 13, 15, 10, 15). Its criteria add up to **2,554 judge calls** (LAB 2,298:
one drawn task, `diligence/aerospace-vertical-integration`, alone has 498 criteria; ours 190 to 256). The rule in T46 says
stop after the smoke at over 2,000, so nothing of the sample was run. Time is not the limit: about 4.5 minutes of agent
time per task at 4 in parallel, so roughly 1.3 hours of agent time plus about 1 hour of judging, about 2.5 hours.
Options: (a) allow the 2,554 calls; (b) drop the 498-criteria task and redraw one (about 2,100, still over); (c) draw 15
LAB slice and 5 LAB other tasks (about 1,400 calls with ours). `lab_sample.py` takes the counts from one place; say which.
`runs/lab_smoke/summary.json` has the smoke rows; the draw is `runs/lab_sample/sample.json` (not committed).

Two things to know before the sample: LAB tasks are scored on their .docx files, so a run that fails on the docx skill
counts against Qwen as a harness result, not a legal one; and the label loop shares NRP's 8 slots, so keep it at 4
workers or fewer while the loop runs.
