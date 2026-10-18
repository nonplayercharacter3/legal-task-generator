# legal-task-generator

A preliminary implementation of an agent that automatically creates legal agent tasks in the same shape as
Harvey's Legal Agent Benchmark (LAB): a partner-style instruction, a folder of matter documents, and a rubric
graded all-pass.

**Status:** skeleton. Every stage and gate runs end to end and is tested with an offline **fake model**. The
real-model path (any OpenAI-compatible endpoint) is tested only against a local mock server, so it has not yet been
run on a real LLM. The issue library is a draft and has not been reviewed by anyone with legal training.

## The idea: write the answer key first

In legal work nobody can cheaply tell you the right answer, so the pipeline constructs answers instead of finding
them. For each invented matter it first writes a **ledger**: the facts every document must agree on, plus 3 to 5
**planted issues**, each assigned to a document and section. The documents, instruction, rubric and reference
answers are all generated from that ledger, so ground truth is known by construction rather than guessed by a model.
Then a series of gates tries to break the task and discards anything that fails.

```
Stage 1  Plan       matter spec ─► source scout ─► ledger writer
Stage 2  Build      document drafter ─► instruction writer ─► rubric writer + gold/flawed answers
Stage 3  Filter     ledger_schema ─► consistency ─► issue_check ─► leak_check ─► rubric_trace
                    ─► rubric_tests ─► decontamination ─► solver_check ─► split ─► accepted task
```

"Similar to LAB" means similar in **shape**, not content: our own taxonomy and issue library, no LAB task used as a
seed, every task screened against LAB text, and LAB kept fully held out for evaluation.

## Quick start

Needs Python 3.11+. No third-party packages at runtime.

```bash
pip install -e ".[dev]"        # or just use python -m ltg from the repo root
python -m pytest               # 70 tests, ~5 seconds, fully offline

python -m ltg run --config configs/fake_demo.toml      # 20 matters, fake model, faults injected
cat runs/fake_demo/report.md
python -m ltg inspect runs/fake_demo/accepted/s7-m0002
```

A sample of that output is committed in [`examples/fake_run/`](examples/fake_run/): one accepted task, one task
rejected at `issue_check`, and the run report. The fake model writes short, formulaic documents; it exists to test
the plumbing, not to show realistic drafting.

### Running real models

Point the pipeline at any OpenAI-compatible endpoint, for example vLLM on a lab GPU:

```bash
vllm serve Qwen/Qwen3-32B --port 8000
python -m ltg run --config configs/openai_compat_example.toml --matters 3
```

Or use Claude through the Claude Agent SDK, billed to a logged-in Claude Code subscription rather than an API key:

```bash
python3 -m venv .venv && .venv/bin/pip install -e ".[dev,claude]"
claude                                              # once: /login with the subscription's account
.venv/bin/python -m ltg run --config configs/claude_pilot.toml
```

Each Claude call runs with no tools and none of the machine's settings, skills, memory or MCP servers, from an
empty working directory, so isolation holds as it does for the other backends.

If a run stops part way (a crash, Ctrl-C, an endpoint going down), rerun the same command with `--resume`.
Matters that already have a verdict are kept, matters that ended in an error are retried, and the run refuses to
resume if `settings.json` shows the generation settings have changed.

Each role can use a different model (`[backend.models]`), e.g. a stronger model as solver and judge. A role can
also use a different backend, for example Claude writing the tasks while an open model on a vLLM server (or a
hosted endpoint such as NRP's) solves them, so the difficulty check is measured on the model you plan to train:

```toml
[backend.roles.solver]
kind = "openai_compat"
base_url = "https://your-endpoint/v1"
model = "Qwen/your-model"
api_key_env = "SOLVER_API_KEY"      # the key is read from this environment variable, never from the file
```

Start with a few matters and read every output before scaling up.

## The gates

Cheap deterministic checks run first and the solver (the most expensive) runs last, so a broken task is dropped as
early as possible.

| Gate | What it checks | Kind |
| --- | --- | --- |
| `ledger_schema` | Counts match the spec, ids resolve, issues are spread across documents and never in a distractor, safe filenames | deterministic |
| `consistency` | A separate extractor re-reads every fact from every drafted file (told the fact's name, not its value); values that differ in wording go to a matcher that judges meaning. The fact's own document must match the ledger; other documents may omit it but not contradict it, unless a planted issue does so on purpose | model |
| `issue_check` | Each planted issue is present and findable in its assigned document | model |
| `leak_check` | The instruction, filenames and document kinds do not name an issue or quote its key phrases (punctuation ignored), and documents carry no HTML comments | deterministic |
| `rubric_trace` | Every criterion cites a ledger issue or fact, every issue is graded, reference answers are well formed | deterministic |
| `rubric_tests` | The rubric is unit-tested: gold answer passes everything, a blank answer passes nothing, the flawed answer fails exactly the criteria for the issue it omits and passes the rest | model |
| `decontamination` | Word 8-gram containment against reference benchmarks (e.g. a LAB clone) stays under the threshold | deterministic |
| `solver_check` | A tool-using solver that never sees the ledger attempts the task several times, opening and searching the matter files step by step. Rejected if it passes without the documents (the instruction leaks the answer), if it never passes (probably broken) or if it always passes (too easy) | model |

Accepted tasks get a train/dev/test split assigned by matter id, so tasks from one matter never straddle splits.

### Isolation

What each role can see is enforced by what the orchestrator puts in its payload, not by asking a model to ignore
things. The instruction writer never receives the issues, so it cannot leak them. The solver receives only the
instruction and the file list, and reads documents through `read_file` and `search` tools that can reach nothing else. The judge receives only a response and the rubric. `tests/test_pipeline_fake.py`
checks this on every run.

## Output layout

```
runs/<name>/
  accepted/<matter_id>/    passed every gate; task.json is the exported task
  rejected/<matter_id>/    kept for debugging; gates.json says where and why it failed
  report.md, report.json   pass counts per gate, per-matter results, model calls and tokens per role
  settings.json            the settings that shaped the matters; --resume checks them
  calls.jsonl              one line per model call
```

Each matter folder holds `spec.json`, `precedents.json`, `ledger.json`, `docs/`, `instruction.md`, `rubric.json`,
`answers.json` (gold, flawed and which issue the flawed answer omits), `solver/attempt_N.md` (with `attempt_N.trace.json`, every tool call and its result) and `gates.json`.

## How the fake model works

`ltg/fake.py` reads the same structured payload a real model would get and returns plausible JSON for each role.
Its "legal knowledge" is the issue library's key phrases: the fake solver reads every page of every file, then spots an issue with probability
`solver_skill`, which produces a realistic mix of too-easy, too-hard and accepted tasks. It can also inject
defects on purpose (`drop_issue`, `wrong_fact`, `conflicting_restatement`, `leaky_filename`, `untraceable_criterion`, `weak_gold`); the tests check that each
one is caught by the right gate, and that disabling any gate makes a test fail.

The HTTP client is tested by running the whole pipeline through a local OpenAI-compatible server backed by the
fake model (`tests/test_openai_compat.py`), including auth headers, per-role model routing and retries.

## Code map

```
ltg/
  schema.py        ledger, rubric, answers and their validators
  taxonomy.py      practice areas, work types, issue library (DRAFT, needs legal review)
  sources.py       precedent loading and selection (local folders for now)
  stages.py        generation stages; each builds only the payload its role may see
  solver.py        tool-using solver (read_file, search, finish) behind solve()
  gates.py         the filters above
  prompts.py       system prompt for each role
  models.py        OpenAI-compatible and Claude Agent SDK clients, JSON parsing, call log
  fake.py          offline fake model with fault injection
  decontam.py      n-gram containment with a fixed-memory Bloom filter
  splits.py        per-matter split assignment
  orchestrator.py  runs matters through the stages and writes the report
  cli.py           `run` and `inspect`
configs/           fake demo, real-endpoint example, Claude pilot
examples/          committed sample output from the fake model
tests/             70 offline tests
```

## Not done yet

- **Real precedents.** `ltg/data/precedents` holds three short synthetic samples. Next: an EDGAR fetcher for
  material contract exhibits, or a folder of saved precedents passed via `[sources].precedent_dirs`.
- **First real-model run.** Run 3 to 5 matters on a real endpoint, read every output, and tune prompts.
- **Issue library review.** Every entry in `taxonomy.py` needs approval from someone with legal training.
- **Judge calibration.** Compare the judge's grades with a lawyer-graded sample before using them as rewards.
- **Diversity tracking.** Report the mix of practice areas, issue types and document counts, and resample toward gaps.
- **Downstream test.** Fine-tune on generated tasks and evaluate on LAB.
