# M6 plan: usefulness pilot fine-tune (EVALUATION.md level 4)

Written 2026-11-27 by the autopilot, before anything runs. Nothing here has run yet.

## Question
Does supervised fine-tuning on our tasks move a small open model's LAB score, and does the hardened generator (v3,
or whichever version passes M4) help more than v1?

## Model
Qwen3-4B (instruct, thinking off), the size the post-training agent's examples use. Measured before training with the
same settings as after.

## Data
- **Arm A (hardened):** the train split of the passing version, at least 150 tasks, from `build_handoff.py`'s
  `data/train.jsonl` (system, user = instruction plus every document, assistant = gold memo). Not available yet:
  about 10 v3 tasks exist on 2026-11-27, so arm A waits for M5.
- **Arm B (control, v1):** the same number of v1 tasks (87 exist; use all if arm A has fewer than 150 when it runs).
  Arm B can run first: it tests the whole pipeline (Job, training, serving the adapter, both graders) on data that
  exists now, so arm A only has to swap the data file.
- Dev split for early stopping; our test split and the LAB sample are never trained on.

## Context length (the main technical risk)
v3 user turns are 31,600 to 43,800 words, about 45k to 62k tokens at 1.4 tokens per word, plus a memo of a few
thousand. Qwen3-4B is 32k native, 128k with YaRN rope scaling. So:
- train with YaRN factor 4 (`rope_scaling = {type: yarn, factor: 4, original_max_position_embeddings: 32768}`) and a
  64k sequence cap, gradient checkpointing and flash attention; serve with the same rope setting;
- v1 tasks (about 22k tokens) fit natively, so arm B also tells whether YaRN itself costs score (compare arm B's
  base model with and without YaRN on our test split, one extra cheap eval).
- If 64k LoRA does not fit on one A100 80GB at batch 1, record it as blocked; do not shorten the documents (that
  changes the task). Sequence parallelism over 2 GPUs is the fallback, only after a measured run.

## Method
LoRA SFT (rank 16, alpha 32, all linear layers), loss on the assistant turn only, learning rate 1e-4, 3 epochs,
batch 1 with gradient accumulation 8, keep the checkpoint with the lowest dev loss. `transformers` + `peft` + `trl`,
pinned versions, installed in the Job's start command.

## Compute (NRP rules in PROMPT.md)
- Read https://nrp.ai/llms.txt before writing any YAML, and follow it.
- Training: one Kubernetes **Job**, 1 A100 80GB, requests from a first measured run (start: 8 CPU, 48Gi), limits
  within 20% of requests, no `sleep` anywhere, the script ends when training ends. Base weights and outputs on PVC
  `ltg-hf-cache`. Check GPU use stays above 40% (`nvidia-smi` in the pod) in the first 10 minutes; if it does not,
  stop and fix before going on.
- Evaluation: the vLLM pod from `deploy/nautilus/vllm-qwen.yaml` with the base model and `--enable-lora`, serving base
  and adapter at once, deleted as soon as the evals end (and after 30 idle minutes at most).
- Expected: training about 1.5 to 2 hours per arm (150 tasks x about 50k tokens x 3 epochs, about 22M tokens);
  evaluation about 3 hours per model (see below). Total about 2 days of wall time with queueing, 3 models.

## Measures (before and after, same settings)
- (a) our test split through `grade/evaluate.py` (frozen grader, greedy, 12k new tokens): all-pass and item rate.
  About 30 tasks, one judge call per criterion (about 300 calls per model).
- (b) the 20 contracts and corporate-ma tasks of the frozen LAB sample (`docs/autopilot/lab_sample.md`) through LAB's
  harness (`scripts/lab_run.py`, the vLLM backend from PR #35);
- (c) its 10 other tasks, to catch the model getting worse outside contract review.
- (b) plus (c) cost about 1,750 judge calls per model (M3's last pass), so 3 models are about 5,300 Opus calls: grade
  in daytime chunks of about 8 tasks, never alongside a generation batch (one heavy Opus job at a time).

## Reading the result
As in EVALUATION.md level 4: (a) and (b) up with (c) not down more than 2 points means useful; (a) up and (b) flat
means the model learned our format, not LAB's skill; (a) flat means check training first. With 20 LAB tasks a change
under about 10 all-pass points is noise: report item rates and bootstrap intervals, as M3 did.

## Order
1. Arm B now-ish (after the current generation batch, so the judge does not compete): base-model evals (a, b, c),
   train on v1, re-eval. This proves the pipeline.
2. Arm A once M5 has 150 train tasks of the passing version: train, eval.
3. Write the result into `docs/research/` and STATE.md; if the cluster cannot schedule the Job within two days of
   trying, record that and open a `needs-sirui` issue.
