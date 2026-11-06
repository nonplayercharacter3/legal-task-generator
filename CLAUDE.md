# CLAUDE.md

Context for any Claude Code session working in this repo (for people, `docs/stage_and_plan.md` says the same in plain
English). A person should read `docs/overview.md` first, the high-level picture. Then read this file, then README.md,
then "Working with other people and sessions" below before you change anything.

## Now (updated 2026-11-04)

**Goal.** Generate long-horizon contract-review tasks (instruction, matter folder, all-pass rubric) that the lab can
train open models on. The tasks must be sound by construction. The generator is model-neutral: every sound task is
kept and labelled with how hard it is; whoever trains picks the band that fits their model.

**Difficulty is a label, not a filter (Sirui She's decision, 2026-11-04).** `solver_check` no longer rejects a task
solved 3 of 3 or 0 of 3; only the probe without documents (a leak) rejects. Each role in `gates.solver_models`
(default `["solver"]`) makes `solver_attempts` attempts and its pass rate is stored per model under `difficulty` in
`gates.json` and `task.json`; a task no model ever passes is kept with `unsolved: true` for a person to check.
`ltg export --model <id> --min-pass --max-pass` selects a band (`--include-unsolved` to keep flagged tasks) and the
report shows the pass-rate spread per model. `scripts/relabel_past_runs.py` recovered 6 tasks that earlier rounds
rejected for a pass rate of 1.0 (s2-m0002, s3-m0002, s4-m0002 Sonnet; s6-m0001, s9-m0001, s9-m0003 Haiku), their
folders restored on the laptop from the commit before the slim; s9-m0003 is also an accepted Qwen task from the same
spec; since `fix/unique-task-ids` the export keys tasks `<run folder>/<matter id>` and keeps both, and `ltg run`
refuses a `--seed` another run folder has used (`--allow-seed-reuse` overrides). Tasks with a label: 15 on the laptop.

**Stage.** Phase 1 is done: its exit standard (see "Pilot standard") was met in cloud round 5 on 2026-10-18. On
2026-11-02 two laptop sessions ran pilot rounds in parallel, both with Opus generating on Sirui She's Max plan
(active since 2026-11-02):

- **Haiku solving**, rounds 6, 8 and 9, branch `pilot/round6-haiku`: 1 of 9 accepted. Every false rejection has a fix;
  in round 9 all three matters passed every quality gate, so what blocks the standard against Haiku is difficulty
  (Haiku passed 3 of 3 attempts on 3 of 9 matters).
- **Qwen solving** (NRP `qwen3-small`), rounds 7 to 11, branch `plan/phase2-unattended` (PR #3): accepted 0, 0, 2,
  0, 0. Round 9 meets the standard's numbers (2 of 3, no errors), pending Sirui She's read of the two tasks.
- Also done that day on `plan/phase2-unattended`: judge leniency measured (keep `judge_hints = true`) and Qwen served
  with vLLM on Nautilus.

**Both branches were merged into `main` on 2026-11-03.** They had fixed some defect classes independently; the merge
keeps one copy of each rule (see "Done steps"). All November rounds ran the LAB screen (every task under the cutoff),
so the "skipped" warning in the October cloud pilot reports no longer applies.

**Seeds 8 and 9 were used by both streams.** `runs/pilot8_haiku` and `runs/pilot8_nrp` (likewise `pilot9_*`) hold the
same six matter specs, drafted twice by different prompt versions, not separate rounds. Use seed 12 or higher next,
and give each round one seed across all solvers.

Totals for 2026-11-02 (8 rounds, 24 candidates): 3 accepted (s6-m0002 Haiku 0.33; s9-m0002 and s9-m0003 Qwen 0.33),
1,270 calls, ~16.7M input tokens, 0 model errors except 3 matters lost to NRP 403s (rounds 10 and 11). Accepted tasks
so far, all phases: 8 (4 from the October cloud pilot, 4 from November).

**Round 12 (2026-11-04, seed 12, Opus generating, Qwen 27B solving on the vLLM pod, PR #10):** 1 of 3 accepted
(s12-m0003, data center cooling distribution agreement, 5 documents, 5 issues, pass rate 0.33, to be read by Sirui She);
154 calls, ~1.49M input and ~245k output tokens, 0 model errors, 36 minutes. First real run of c0a90fa, 5c66350 and
c3f891c. Two defect classes, fixed on `fix/round12` (one commit each):
- Issue criteria bundled one particular harm and one particular remedy with the finding, and the judge enforced them
  (s12-m0001, false rejection at `solver_check` 0 of 3; 5c66350 did not prevent it). Now an issue criterion may require
  only the finding, where it is, that it matters and that a fix is recommended; a harm or remedy clause whose words
  the issue's `expected_finding` does not carry is sent back to the rubric writer once with the flagged clauses, and
  `rubric_trace` rejects only if the corrected rubric still has one (`gates.check_bundling`: `"repair"` default,
  `"warn"` records only, `"off"`; the repair is in `gates.json` and counted in `report.md`). It is a repair, not a
  gate, because on past rubrics the word-overlap rule flagged 34 of 157 issue criteria in 19 of 31 real matters,
  6 of the 9 accepted ones among them, with some synonym false flags. The judge passes any sound route.
- An issue planted as history the client already ratified (s12-m0002, I3: a missed dispute window followed by a
  restated note the client signed, nothing in the folder objecting; `issue_check` rejected it, correctly). Now the
  ledger writer keeps every issue actionable and puts the client's position in the folder, the issue verifier asks
  whether it is still actionable, and `issue_check` stores the verifier's `reason` in `gates.json`.

Code check (2026-11-04, `feat/difficulty-labels`): `configs/fake_demo.toml` rejects consistency 3, issue_check 1,
leak_check 2, rubric_trace 1, rubric_tests 1; `solver_check` rejects only leaks now, so 0 in the demo (it has no leak
fault), and 12 of 20 are accepted with labels (pass rates 0.33: 5, 0.67: 5, 1.00: 2).

**Plan.** Each step says what done looks like.
1. **Sirui She reads round 9 (Qwen):** `runs/pilot9_nrp/accepted/s9-m0002` (glass supply, dev) and `s9-m0003` (dental
   MSA renewal, train), against the checklist in "How to verify changes". Done: if both hold up, the pilot standard
   is met with Qwen solving.
2. **Qwen labels difficulty (superseded 2026-11-04: a label, not a bar; see above).** Pilot rounds use
   `configs/pilot_nrp_solver.toml` (or `configs/vllm_nautilus_solver.toml` when NRP is down), so Qwen 27B is the
   default labelling model; add roles to `gates.solver_models` to label with more. Same spec, different solvers:
   s9-m0003 scored 0.33 with Qwen and 1.0 with Haiku, though the two drafts differ. If tasks must get harder: longer
   folders, more cross-document issues (known weaknesses 2 and 3).
3. **Next rounds** on merged `main`, seed 13 or higher, after the `fix/round12` PR merges. Qwen rounds need NRP
   back (since ~23:00 on 2026-11-02 every chat request returns an empty 403, even with a bad key, while `/v1/models`
   works; not rechecked) or the vLLM pod (`configs/vllm_nautilus_solver.toml`, about 3.5 times slower).
4. **Fine-tune on Nautilus: not started.** Serving works (below). Seven accepted tasks is far too few; scale the
   generator first.
5. **Tell the second contributor that round 6 already ran on the laptop** (a GitHub issue), so it is not run twice.

Done steps, for reference:
- **Merge of `pilot/round6-haiku` and `plan/phase2-unattended` (2026-11-03).** Overlaps resolved by keeping one copy
  of each rule: `consistency` keeps both trimmed-extraction rules (e144c20: the extraction is part of the ledger value
  and the document states the whole value; 3e4f5f7: a 4+ word ledger value stated verbatim in its own document);
  the ledger writer keeps c0a90fa's cross-reference rule with 238bbc2's remedy (cite the damaging subsection or say
  "notwithstanding"), and 6593250's deal-event rule plus c3f891c's "name that document"; the rubric writer keeps
  exactly one issue criterion per issue (e134b3f) with 5c66350's "require the conclusion, not one route" and
  "a fact criterion is passable by a response that misses every issue". Committed run output was slimmed (see
  "Working with other people and sessions"); the full output stays on the laptop under `runs/`.
- **Rounds 6, 8, 9 with Haiku (2026-11-02).** `configs/claude_pilot_opus.toml`, `runs/pilot{6,8,9}_haiku`, branch
  `pilot/round6-haiku`. 568 calls, ~8.7M input and ~1.8M output tokens, 0 errors, about 45 minutes per round.
  Accepted: s6-m0002 (distribution agreement, 5 documents, 5 issues, pass rate 0.33). Rejections and causes:
  - Too easy, correct (Haiku truly found every issue): s6-m0001, s9-m0001, s9-m0003.
  - s6-m0003 `rubric_tests`, correct: the fix for I1 was filed as a fact criterion. Fixed (69294e2, rubric writer).
  - s8-m0003 `consistency`, **false**: the extractor dropped "exclusively" from a forum clause. Fixed (3e4f5f7: a
    value of 4+ words found verbatim in its own document passes).
  - s8-m0002 `issue_check`, correct: "subject to the limitations set forth in Section 8.7" also pulled in 8.7(c),
    which exempted the very claims the issue said were capped. Fixed (238bbc2, ledger writer).
  - s8-m0001 `solver_check` 0 of 3, **false**: all memos found the issue but C3 also demanded citing a precedence
    clause the conclusion does not need. Fixed (5c66350, rubric writer: require the conclusion, not one route).
  - s9-m0002 `solver_check` 0 of 3, correct: issue I1 rested on a planned sale stated only in the ledger summary.
    Fixed (c3f891c, ledger writer). 5c66350 and c3f891c have not run on a real model yet.
- **Make qwen3-small write its memo: done 2026-10-27.** Every memo call had failed on 2026-10-24 (32k `max_tokens`
  or 600 s timeouts) because NRP runs the model at `reasoning_effort = "xhigh"` and it thinks for ~30k tokens
  (`docs/research/qwen_memo_length.md`). Fix: `extra_body` on a backend or role adds fields to each OpenAI-compatible
  request; `configs/pilot_nrp_solver.toml` sets `reasoning_effort = "low"` for the solver. `solve()` also unwraps
  `{"action": {...}}` replies. Rerun (`scripts/solve_only.py`, `runs/qwen_solver_smoke_low/`, not committed): 12 of
  12 memos written (2,600 to 6,900 words), 190 calls, 0 failed, 2 to 6 minutes per attempt, 20 wrapped actions
  handled. Proxy issue recall (NRP `qwen3` against the ledger, not our judge) 47 of 51; all 3 attempts on s5-m0001
  missed I2 (free assignment in the supply agreement).
- **Rounds 7 to 11 with Qwen (2026-11-02).** `configs/pilot_nrp_solver.toml`, `runs/pilot7_nrp` to
  `runs/pilot11_nrp`, branch `plan/phase2-unattended`. Accepted 0, 0, 2, 0, 0 of 3. Round 9 accepted s9-m0002 (glass
  supply, dev, 0.33) and s9-m0003 (dental MSA renewal, train, 0.33), 0 model errors; read in full by Claude, one weak
  criterion each (fixed upstream), still to be read by Sirui She. Defect classes fixed, one commit each: extractor
  trimming a value its own document states (e144c20); a contradiction not marked in `contradicts` but quoted in the
  issue (48206e3); a fix filed as a fact criterion (e134b3f; e2951d9, which allowed several issue criteria per issue,
  bloated rubrics to 15 to 17 criteria and caused round 8's 0 of 3); an issue resting on a deal event stated only in
  the ledger summary (6593250); a mutual clause called one-sided (261f669); a bare 403 from NRP not retried
  (4703747); issues cured by their own cross-references (c0a90fa, not yet run). Correct rejections: Qwen missed a
  detail in each of 3 attempts (s7-m0002, s10-m0002: never turned a renewal window into dates).
- **Judge leniency: done 2026-11-02, keep `judge_hints = true`.** `scripts/judge_leniency.py`, `runs/judge_leniency*`:
  11 matters, 67 responses, 1,352 criterion grades per condition. Hints on vs off: 0 settled flips (5 and 7 grades
  of noise), pass rates 0.923 vs 0.921; gold passed 99.5% and 100% of criteria; a flawed answer got credit for its
  omitted issue 2 and 1 times in 26. A ledger-aware referee (also Opus, so not lawyer calibration) regraded all 102
  Qwen issue grades: no judge pass it would fail, 3 judge fails it would pass, all on criteria bundling several asks.
- **GPUs on Nautilus: serving works (2026-11-02).** `deploy/nautilus/vllm-qwen.yaml` (on `plan/phase2-unattended`,
  merged there from PR #2) serves Qwen3.8-27B-FP8 (the same model as `qwen3-small`) with vLLM 0.30.0 on one A100
  80GB; weights cached on PVC `ltg-hf-cache` (100Gi, kept). Start with `kubectl apply`, then
  `kubectl port-forward pod/ltg-vllm-qwen 8000:8000` and use `configs/vllm_nautilus_solver.toml`. Queued ~20 minutes
  for an A100, ready ~7 minutes later, KV cache 623k tokens, honours `reasoning_effort = "low"`.
  `scripts/solve_only.py` against it (`runs/qwen_solver_smoke_vllm`): 12 of 12 memos, 0 failed calls, median 8.9
  minutes per attempt (NRP 2.5), all-pass 3 of 12 as on NRP. Delete the pod when done (it also stops itself after
  6 hours).

Loose ends: branch `claude/affectionate-perlman-e65dbe` (local only, worktree under `.claude/worktrees/`, 2 commits
from 2026-10-18) adds an EDGAR fetcher and is not merged; recommended parking it, Sirui She has not decided.
Work only in `~/Projects/legal-task-generator` (the old Desktop clone was removed on 2026-11-03).

## Working with other people and sessions

**Planning and coding are split (Sirui She's rule, 2026-11-03).** Sirui She plans with Claude in the Claude app; the
Claude Code terminal on the laptop does the coding. The app session assigns work through `inbox.md` at the repo root
(gitignored, one copy, attachments under `.inbox/`). In the terminal, `/ltg-inbox` (`.claude/skills/ltg-inbox/`) works
the next task: read `inbox.md` first, take the top open task, follow its steps, write the result under the task, and
set its status. **Never use the user-level `/inbox` skill in this repo**; it belongs to another project. Do not start work that is not in the
inbox or asked for by Sirui She directly.

**Keep the work tree clean.** The main checkout (`~/Projects/legal-task-generator`) stays on `main`, with nothing
uncommitted and nothing untracked outside `.gitignore`. Every task runs in its own worktree on its own branch
(`git worktree add ../ltg-wt/<branch> -b <branch> main`), and the worktree and branch are removed once the PR
merges. Never switch the main checkout's branch. Before ending a task, `git status` must be empty in the main
checkout and `git worktree list` must show only live work.

Two people work on this repo: Sirui She (owner, on the laptop) and a second contributor (on their own machine, with
their own Max plan). Each may run several Claude Code sessions.

**Between the two people: GitHub.** Questions, requests and hand-offs go in GitHub issues; results go in pull
requests. A pilot round goes on its own branch: `runs/` is gitignored, so force-add only what reviewers need
(`git add -f`): `report.md`, `report.json`, `settings.json`, the whole `accepted/` folder, and `spec.json`,
`ledger.json` and `gates.json` of each rejected matter; for analysis folders (`judge_leniency*`, solver smoke tests)
only `summary.json`. Never commit `calls.jsonl`, solver traces or logs. Then open a PR into `main` whose description has the round's numbers (accepted, pass rates,
calls, tokens, errors) and the cause of every rejection. If a round leads to code fixes, one commit per defect
class, as in "Pilot standard". Pull `main` before starting work; whoever changes the stage or plan updates "Now" in
the same PR.

**Between sessions on Sirui She's laptop: the handoff board.**
`/Users/shesirui/Projects/legal-task-generator/HANDOFF.md`. It is gitignored on purpose, so there is exactly one copy:
sessions in a worktree edit it at that absolute path, never a copy on their branch. Its top section gives the rules.
Only that laptop has it. Sessions elsewhere (the second contributor's, cloud sessions) use GitHub as above, and a
laptop session logs what they report.

What belongs where: the board and GitHub issues hold who is doing what right now, requests and a running log.
Anything that stays true (stage, plan, decisions, results) also goes into this file, on your branch, in the same change.
Whoever changes the stage, a step's status or a decision updates `docs/overview.md` in the same PR.

## What this project is

Professor Pengtao Xie (AIBuildAI lab, UCSD) asked for an agent that automatically creates training data
similar to Harvey's Legal Agent Benchmark (LAB): long-horizon legal tasks made of a partner-style instruction,
a folder of matter documents, and an all-pass rubric. This repo is the preliminary implementation. The lab works
on LLM post-training; the goal is training data for legal agents, with LAB used only for evaluation.

## Decisions already made (don't relitigate without asking Sirui She)

- **Ledger-first design.** For each invented matter, write the answer key first (facts plus 3 to 5 planted issues,
  each tied to a document and section), then generate documents, instruction, rubric and reference answers from it.
  Ground truth is known by construction, not judged by a model.
- **Difficulty is a label, not a filter (2026-11-04).** The generator is model-neutral: any sound task is kept, the
  solver models' pass rates are stored with it, and whoever trains picks the band. `solver_check` rejects only a leak
  (solved without the documents). Tasks no model passes are kept and flagged `unsolved` for a person to check.
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
  direct API calls. He confirmed this means the Max plan; Sirui She is on Max from 2026-11-02 and runs Claude rounds on the laptop.
  The second contributor (from 2026-10-27) runs Claude rounds on their own Max plan (Sirui She's decision). For GPUs, Nautilus (namespace `ecepxie`, see "Background and history"). The runtime stays standard library only: the SDK
  is an optional extra (`pip install -e ".[claude]"`) imported only by that backend.

## Background and history (status as of 2026-10-24; "Now" supersedes it)

- All three stages and eight gates run end to end with the offline fake model (`ltg/fake.py`).
- Offline tests pass (`python3 -m pytest`; counts per branch in "Now"). Every gate, and each branch of `rubric_tests` and `solver_check`,
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
  (`~/.kube/config` from https://nrp.ai/config; never commit it or any token). Our vLLM pod ran there on 2026-11-02 (see "Now", step 5).
  The pod freeze seen on 2026-10-18 (`reached-quota` at `pods: 0`) was lifted by 2026-10-24: the quota reads
  7/200, `kubectl auth can-i create pods` and `persistentvolumeclaims` say yes, and 0 of 12 A100s were in use.
  NRP limits a pod without a controller to 2 GPUs, 32 GB RAM and 6 hours. The namespace may hold up to 12 A100s at once, requested as `nvidia.com/a100` (opportunistic pods excepted), and no
  H100, H200 or GH200 (quota 0). The cluster lists 31 nodes with whole A100 80GB cards (22 SXM4, 9 PCIe; most at
  SDSC, SDSU, Missouri); counts are nodes, not cards. Plan: serve a ~8B Qwen with vLLM first, then ~30B, then
  fine-tune.
- LAB screen on (2026-10-18): `reference_dirs = ["../harvey-labs"]` (clone `harveyai/harvey-labs` beside the repo; never
  commit it). The index reads LAB's .docx/.xlsx/.pptx/.eml as well as text, and counts only wording found in a single
  LAB task (`decontam_group_depth = 3`): without that, standard clauses shared across LAB tasks pushed our own sound
  documents to 0.56, over the 0.5 cutoff.
- NRP hosted models (2026-10-18): `https://ellm.nrp-nautilus.io/v1`, OpenAI-compatible, key from the NRP portal in
  `NRP_LLM_API_KEY` (never in the repo or chat). `qwen3-small` is Qwen3.8-27B dense, the planned solver
  (`configs/pilot_nrp_solver.toml`); no ~8B Qwen chat model is hosted. Limits: 48k output tokens/min per key and model (NRP fair-use page, checked 2026-10-27; 200k was wrong),
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
- qwen3-small solver smoke test (2026-10-24, `scripts/solve_only.py`, 3 attempts on each of the 4 accepted cloud
  pilot tasks, no judging; logs in `runs/qwen_solver_smoke/`, not committed): every attempt called `finish` after 9
  to 18 actions (limit 28) and read every page, so the tool protocol works. Slips were rare and recovered: 2 prose
  replies fixed by the JSON retry, 6 actions wrapped as `{"action": {...}}`. Every memo call failed (fixed, see "Now", step 2).
  The endpoint took a 31k-token prompt with `max_tokens` up to 200,000 (the server may clamp silently) and honours
  `chat_template_kwargs.enable_thinking = false`. 216 calls, ~1.95M input and ~568k output tokens, free on NRP.
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
(Opus generating and Qwen solving: `configs/pilot_nrp_solver.toml`, or `configs/vllm_nautilus_solver.toml`; until
2026-11-02 `configs/claude_pilot_opus.toml` with Haiku solving; a new `--seed` each round so prompts are never tuned to
one set of matters).

1. At least 2 of 3 matters pass every quality gate (all gates except the difficulty label), with no model errors.
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

1. **Solver context grows with the folder.** The transcript keeps every page read (~30k tokens for five long
   documents). If a model's window is too small, drop old page text and keep the solver's own notes.
2. **Short folders make the agentic solver read everything.** With 3 to 5 short documents the tool-using solver
   behaves like the old one-prompt solver. The difficulty filter only bites once folders get longer or larger.
3. **LAB index takes ~30 minutes to build.** LAB is ~455M words (mostly .docx); the index is saved under
   `runs/.decontam_cache` and reused while LAB is unchanged, but a fresh cloud container must rebuild it.

Smaller known gaps: no EDGAR fetcher (precedents come from local folders),
judge not calibrated against lawyer grades (hints on vs off measured, no difference; see "Now", step 4), `solver_attempts = 1` gives
only the labels 0 and 1, and one fact lives in one document, which limits cross-document reasoning.

## How to verify changes

- `python3 -m pytest` must stay green. Add a test for every new gate or behaviour; if you change a gate, check that
  disabling it still makes a test fail.
- `python3 -m ltg run --config configs/fake_demo.toml` then read `runs/fake_demo/report.md`. The demo injects
  faults into ~35% of matters; consistency, issue_check, leak_check, rubric_trace and rubric_tests should each
  reject at least one. solver_check rejects only leaks (none in the demo); the Difficulty section shows the labels.
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
