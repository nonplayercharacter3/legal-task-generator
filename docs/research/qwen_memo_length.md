# Why qwen3-small's memo calls run out of tokens, and what bounds them

Researched 2026-10-27 from primary sources (NRP docs, Qwen model cards and chat template on Hugging Face, Qwen docs,
vLLM docs, source and PRs on GitHub, the vLLM recipes repo). Nothing here was tested against the NRP endpoint.

## Question

On 2026-10-24, all 12 of `qwen3-small`'s memo calls (`SOLVER_WRITE`, one system and one user message, non-streaming,
`temperature 0.7`, `max_tokens 32000`, no other sampling fields) failed: 9 hit `finish_reason: length` and 3 timed out at
600 s. One replay used a 10.9k-token prompt, then 23,647 reasoning tokens and about 8.3k memo tokens (36k characters,
18+ issues, each with proposed contract language), cut off partway through an issue. What is the model, what do
Qwen and vLLM say about thinking length and sampling, and which fixes are available?

## Short answer

- `qwen3-small` is **Qwen/Qwen3.8-27B-FP8** (27B dense, official block-FP8), served with a 1,000,000-token context
  (262,144 native, extended with YaRN). NRP's docs confirm this. They do not name the engine or its version for
  this alias. Evidence points to vLLM with a reasoning parser, but that is inferred.
- Thinking is on by default at **`reasoning_effort` = `xhigh`**. NRP says this setting and preserved thinking
  "raise tokens per request" compared with Qwen3.6. NRP documents two per-request controls: `reasoning_effort`
  (`low`, `medium`, `xhigh`) and `chat_template_kwargs: {"enable_thinking": false}`.
- Qwen's recommended sampling for Qwen3.8 **thinking** mode is `temperature 1.0, top_p 0.95, top_k 20, min_p 0,
  presence_penalty 0`. For **non-thinking** mode it is `temperature 0.7, top_p 0.80, top_k 20, min_p 0,
  presence_penalty 1.5`. Our requests are a hybrid: thinking on, temperature 0.7, and top_p/top_k taken from the
  server's defaults. For endless repetition, Qwen suggests raising `presence_penalty` (0 to 2).
- Qwen advises **large** output budgets for this model: up to 262,144 tokens for reasoning and 131,072 for the
  final answer, where a framework allows separate limits. In this light, 32,000 is small for a model that thinks
  at xhigh.
- In vLLM, **`max_tokens` covers reasoning plus content**: the reasoning is ordinary generated text that the parser
  splits off afterwards. vLLM has had a per-request **`thinking_token_budget`** since v0.19.0. It needs the server
  to run with a reasoning parser (or `--reasoning-config`), and NRP does not document it.
- vLLM rejects `max_tokens` above `max_model_len`. Since v0.32.0 it otherwise caps `max_tokens` at
  `max_model_len - prompt length` without an error; before that, prompt + `max_tokens` above `max_model_len` was
  rejected. Our 31k + 200k probe fits inside 1M under either rule, so it tells us nothing about capping.
- NRP's fair-use page sets **48,000 output tokens per minute** per API token and model. CLAUDE.md and the config
  say 200k. Eight memo calls of ~50k tokens each would exceed this, so expect 429s or need fewer concurrent calls.
- The levers, cheapest first: lower `reasoning_effort`, a length cap in the prompt, a larger `max_tokens` with a
  longer timeout (or streaming), non-thinking mode for the memo call only, and `thinking_token_budget`
  (untested on NRP). Evidence favours combining a modest `reasoning_effort` or a thinking cap with a bigger
  `max_tokens`. Prompt wording alone does not address the 24k-token thinking.

## Findings

### 1. What `qwen3-small` is on NRP

| Claim | Source |
|---|---|
| Alias `qwen3-small`, status "main", 27B, context 1,000,000, tools yes, reasoning yes, image and video input, HF ID `Qwen/Qwen3.8-27B-FP8`, quantization "FP8 (official block-FP8)" | https://nrp.ai/documentation/userdocs/ai/llm-managed/models/ |
| "Reasoning is on at xhigh by default"; `reasoning_effort="low"` or `"medium"`, `xhigh` the default; disable with `extra_body={"chat_template_kwargs": {"enable_thinking": false}}` | same page |
| "1M context (262K native, YaRN-extended)"; thinking from earlier turns kept by default; `preserve_thinking` false keeps only the latest turn's | same page |
| Changelog: Oct 2026, now serves the official FP8 checkpoint instead of bf16. Aug 2026, switched from Qwen3.6-27B to Qwen3.8-27B; context 1,000,000; `reasoning_effort` added with `xhigh` the default; preserved thinking on by default. NRP adds that both changes "raise tokens per request relative to Qwen3.6" | https://nrp.ai/documentation/userdocs/ai/llm-managed/lifecycle/ |
| `max_tokens` "is the maximum output length under the context length"; if a client needs a value, set it to roughly a third to a quarter of the context window; never set it to the full context length, or "the model will error." `chat_template_kwargs` handling "is supported on vLLM and SGLang models" | https://nrp.ai/documentation/userdocs/ai/llm-managed/api-access/ |
| Fair use: 48,000 output tokens per minute per API token and model (HTTP 429 above that); qwen3-small allows 8 concurrent requests per user; requests using 35% or more of the context window are limited to 1 at a time; SDSC and Internet2 affiliates get twice these limits; non-commercial use only | https://nrp.ai/documentation/userdocs/ai/llm-managed/fair-use/ |
| NRP's client configs list `contextWindow: 1000000` for qwen3-small, and effort levels `[low, medium, xhigh]` with default `xhigh` | https://nrp.ai/documentation/userdocs/ai/llm-managed/client-configs/ |

Not documented by NRP for this alias: the engine and its version, the server flags (reasoning parser,
`--generation-config`, `--reasoning-config`), any server-side cap on `max_tokens`, request timeouts, and decode
throughput. The live status page (https://nrp.ai/llm-status) returned "Error reading LLM status from the cluster"
when fetched.

Engine (inferred): our responses carry `reasoning_content` and `completion_tokens_details.reasoning_tokens`. vLLM
fills `completion_tokens_details` only when a reasoning parser is configured
(`self._include_reasoning_tokens_details = bool(reasoning_parser)`,
https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/chat_completion/serving.py). This matches vLLM
with `--reasoning-parser qwen3`, the setting vLLM's Qwen3.8-27B recipe uses
(https://github.com/vllm-project/recipes/blob/main/models/Qwen/Qwen3.8-27B.yaml). It does not rule out SGLang.

The model itself: "Context Length: 262,144 natively and extensible up to 1,000,000 tokens", 64 layers; config
`model_type: qwen3_5`, `Qwen3_5ForConditionalGeneration` (https://huggingface.co/Qwen/Qwen3.8-27B,
https://huggingface.co/Qwen/Qwen3.8-27B-FP8/raw/main/config.json). The name "Qwen3.8-27B" in CLAUDE.md is correct.

### 2. Qwen's guidance on thinking mode

Closest model card: **Qwen3.8-27B**, the same model (https://huggingface.co/Qwen/Qwen3.8-27B, Best Practices; the
FP8 card https://huggingface.co/Qwen/Qwen3.8-27B-FP8 gives the same values).

- Sampling: "Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`,
  `repetition_penalty=1.0`". Non-thinking mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`,
  `presence_penalty=1.5`, `repetition_penalty=1.0`.
- Repetition: "you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetition. However,
  using a higher value may occasionally result in language mixing and a slight decrease in model performance."
- Output length ("Adequate Output Length"): for frameworks with separate limits, "Reasoning Content: Set the maximum
  output length to 262,144 tokens" and "Final Response: Set the maximum output length to 131,072 tokens."
- Effort: "`xhigh` (default): for complex tasks demanding thorough analysis; `medium`: balancing accuracy and speed;
  `low`: efficient reasoning optimizing for speed and cost." The card also warns that in multi-turn agentic tasks,
  lower effort can mean "insufficient analysis, more failures, and repeated retries".
- The card's request example passes `reasoning_effort` as a top-level argument, and `enable_thinking` and
  `preserve_thinking` inside `chat_template_kwargs`.
- The card does not mention a thinking budget or the `/think` and `/no_think` soft switch. The Qwen3.8 chat
  template has no soft-switch handling either
  (https://huggingface.co/Qwen/Qwen3.8-27B-FP8/raw/main/chat_template.jinja).

What `reasoning_effort` does in the template: it is not a token limit. `xhigh` adds a system line, "Please think
carefully through the task, validate key assumptions, consider plausible alternatives...". `low` adds "Keep your
thinking brief and focused, moving directly to the conclusion without unnecessary elaboration." `medium` adds no text.
Any other value (for example `high`) makes the template raise "Unexpected reasoning effort". With
`enable_thinking: false`, the template pre-fills an empty `<think>\n\n</think>\n\n` block (same template file).

What our requests actually sample with: vLLM fills unset fields from the model's `generation_config.json` ("Priority:
user -> server default -> OpenAI default", `to_sampling_params` in
https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/chat_completion/protocol.py; the
`generation_config` default is `"auto"`, loaded from the model, in
https://github.com/vllm-project/vllm/blob/main/vllm/config/model.py). Qwen3.8-27B-FP8's `generation_config.json`
sets `temperature 1.0, top_k 20, top_p 0.95` and no presence_penalty
(https://huggingface.co/Qwen/Qwen3.8-27B-FP8/raw/main/generation_config.json). If NRP keeps the default, our calls
run thinking mode at temperature 0.7 (ours), top_p 0.95 and top_k 20 (server), presence_penalty 0. That is
thinking-mode sampling with a lower temperature. Whether NRP overrides the generation config is not documented.

Older generation, for comparison (Qwen3-32B, https://huggingface.co/Qwen/Qwen3-32B): thinking `Temperature=0.6,
TopP=0.95, TopK=20, MinP=0`; "DO NOT use greedy decoding, as it can lead to performance degradation and endless
repetitions"; presence_penalty 0 to 2 for repetition; "We recommend using an output length of 32,768 tokens for most
queries", and 38,912 for competition-level math and code. Qwen3-32B also had the `/think` and `/no_think` soft
switch. The 32k figure belongs to that generation, which also had no `reasoning_effort` default of xhigh; Qwen3.8's
card asks for much more.

### 3. Bounding thinking length

**Qwen's documented thinking budget** (https://qwen.readthedocs.io/en/latest/getting_started/quickstart.html,
"Thinking Budget"): the budget is enforced by "ending the thinking process once the budget is reached and guiding the
model to generate the 'summary' with an early-stopping prompt". The doc says open-source frameworks do not build
this in, and shows a two-pass Transformers example: generate up to the budget; if `</think>` has not appeared, append
`"\n\nConsidering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>\n\n"`
and generate the answer. It recommends a budget "higher than 1024 for meaningful improvements". Over an
OpenAI-compatible chat endpoint this needs a raw-completion continuation, which our client does not do.

**vLLM `thinking_token_budget`** (https://github.com/vllm-project/vllm/blob/main/docs/features/reasoning_outputs.md,
"Thinking Budget Control"):
- It is a per-request sampling parameter, sent as a top-level field in the chat request body
  (`"thinking_token_budget": 10` in the doc's curl example). "Once the reasoning token count reaches the configured
  `thinking_token_budget`, vLLM forces the model to produce `reasoning_end_str`, effectively terminating the
  reasoning block."
- Server side, it needs `--reasoning-parser`. `--reasoning-config` (start and end strings) is optional: "If not set,
  vLLM will attempt to automatically initialize these tokens from the reasoning parser." `reasoning_end_str` can
  carry a transition phrase before `</think>`, as Qwen's early-stopping prompt does.
- Without a reasoning config the request is rejected: "thinking_token_budget is set but reasoning_config is not
  configured. Please set --reasoning-parser and/or --reasoning-config to use thinking_token_budget."
  (https://github.com/vllm-project/vllm/blob/main/vllm/v1/engine/input_processor.py)
- Added in PR #20859, "[Feature] limit thinking tokens (hard limit)", merged 2026-03-24
  (https://github.com/vllm-project/vllm/pull/20859). The first release with `thinking_token_budget` in
  `SamplingParams` is **v0.19.0** (2026-04-03). Checked by grepping `vllm/sampling_params.py` at tags v0.18.1
  (absent) and v0.19.0 (present). Automatic setup from the reasoning parser alone came in PR #38214, merged
  2026-04-10 (https://github.com/vllm-project/vllm/pull/38214), first in v0.20.0. Before that, `--reasoning-config`
  had to be set explicitly.
- The budget counts thinking that starts in the prompt, so Qwen3.8's template, which opens the turn with `<think>`,
  is handled (`thinking_budget_state.py`,
  https://github.com/vllm-project/vllm/blob/main/vllm/v1/sample/thinking_budget_state.py).
- Later fixes: #41674 (budget "silently ignored", 2026-05-15), #43757 and #45984 (budget not enforced on re-entry,
  June and July 2026) and #58231 (with speculative decoding, 2026-10-19). With an older NRP build, some of these
  may be missing.

**`reasoning_effort` in vLLM**: the chat request accepts it at top level and passes it to the chat template. If
`enable_thinking` is not set, vLLM injects `enable_thinking = (reasoning_effort != "none")` (`build_chat_params` in
the protocol file above; docs section "Automatic `enable_thinking` Activation"). On main, the field accepts none,
minimal, low, medium, high, xhigh and max. In v0.19.0 it was `Literal["none", "low", "medium", "high"]`, so `xhigh`
needs a newer build. NRP documents `xhigh` as working, so their build is newer. For Qwen3.8, send only `low` or
`medium`: `high` passes vLLM but the template rejects it.

**Turning thinking off**: `chat_template_kwargs: {"enable_thinking": false}` (NRP models page; Qwen card; vLLM
reasoning docs: "The reasoning feature for the Qwen3 series is enabled by default. To disable it, you must pass
`enable_thinking=False` in your `chat_template_kwargs`"). With Qwen3.8 there is no `/no_think` alternative.

**`max_tokens` above the remaining context** (vLLM):
- Error if `max_tokens` (or `max_completion_tokens`) exceeds `max_model_len`: "...cannot be greater than
  max_model_len=... Please request fewer output tokens." (`__post_init__` in
  https://github.com/vllm-project/vllm/blob/main/vllm/renderers/params.py). This matches NRP's warning that setting the
  full context length means "the model will error."
- Otherwise vLLM caps it without an error: `get_max_tokens()` returns the minimum of `max_model_len - input_length`,
  the request's `max_tokens`, any server override, and a platform cap
  (https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/serve/utils/api_utils.py).
- Before PR #57035 (merged 2026-10-09, first in **v0.32.0**, released 2026-10-18;
  https://github.com/vllm-project/vllm/pull/57035), a prompt longer than `max_model_len - max_tokens` was
  **rejected**. The PR's example: context 128000, prompt 62466, max_tokens 65535 was rejected before and is now
  capped to 65534.
- A server-wide cap is also possible: "If `max_new_tokens` is specified in generation config, then it sets a
  server-wide limit on the number of output tokens for all requests" (`generation_config` docstring in
  `vllm/config/model.py`). Qwen3.8's shipped `generation_config.json` has no `max_new_tokens`. Whether NRP adds one is
  unknown.
- Our probe (31k prompt, `max_tokens` 200,000, accepted) fits inside a 1M context under every rule above, so it
  does not show capping. NRP's own advice to stay at or below 1/3 to 1/4 of the context (250k to 333k) also allows it.

### 4. Does `max_tokens` cover reasoning plus content?

Yes. `SamplingParams.max_tokens` is the "Maximum number of tokens to generate per output sequence"
(https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py). The reasoning parser splits text the model
has already generated into `reasoning_content` and `content`, and the vLLM reasoning docs say: "If
`thinking_token_budget` is not specified, no explicit reasoning limit is applied beyond normal generation constraints
such as `max_tokens`" (reasoning_outputs.md). The recipe for this model makes the same point from the other side:
without the parser "the entire reasoning block lands in `message.content` and a 2048-token budget can be spent before
the answer starts" (https://github.com/vllm-project/recipes/blob/main/models/Qwen/Qwen3.8-27B.yaml). Our replay agrees:
23,647 reasoning tokens plus ~8.3k content tokens is about 32,000.

### 5. Timeouts (client side)

Our client sends non-streaming requests through `urllib.request.urlopen(timeout=600)`. Python documents that timeout
as applying to "blocking operations like the connection attempt"
(https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen), so it applies to each socket read,
not to the whole call. A non-streaming response sends nothing until generation ends, so any call that generates for
longer than 600 s times out. The 3 timeouts mean those calls produced fewer than 32,000 tokens in 600 s (under about
53 tokens/s, counting prefill). A bigger `max_tokens` needs a proportionally longer timeout. With `stream: true`,
chunks keep arriving, so the per-read timeout would only catch stalls. That is an inference from the Python docs
and was not tested here.

## Candidate fixes

| Fix | What it changes | Evidence | Risk |
|---|---|---|---|
| Raise `max_tokens` (e.g. 64k to 128k) and `timeout` together | Room for ~24k thinking plus a full 18-issue memo | Qwen3.8 card asks for up to 262k reasoning and 131k answer; NRP allows up to 1/3 to 1/4 of 1M; vLLM accepts any value up to `max_model_len` | Does not shorten anything: calls get slower and costlier, and 8 parallel ~50k-token calls exceed NRP's 48k output tokens/min (429s, which the client waits out). Timeout must grow with it unless the client streams |
| `reasoning_effort: "low"` (or `"medium"`) on the memo call | Swaps the template's "think carefully... consider plausible alternatives" line for "keep your thinking brief" (low) or no line (medium) | NRP models page and changelog; Qwen3.8 card; chat template | A soft nudge, not a cap: thinking can still run long. The Qwen card warns that lower effort can reduce analysis quality in agentic tasks. It changes what the difficulty check measures. Values other than low/medium/xhigh raise an error |
| `thinking_token_budget: N` (e.g. 8k to 16k) on the memo call | Hard cap: vLLM forces `</think>` after N thinking tokens, then the model writes the answer | vLLM docs and source (v0.19.0+, reasoning parser required); Qwen documents the same method | Not documented by NRP: may be rejected (no reasoning config on the server) or ignored on an older build. Needs a one-call probe. The model may jump straight to the answer without a closing summary of its thinking |
| `chat_template_kwargs: {"enable_thinking": false}` for the memo call only (steps keep thinking) | Removes the ~24k thinking from the memo call; the whole budget goes to the memo | NRP models page; Qwen card; already probed: 0 reasoning tokens | The memo is written without a final reasoning pass, which may lower quality and make the solver look weaker than a thinking setup. Qwen's non-thinking sampling then applies (temp 0.7, top_p 0.8, presence_penalty 1.5). Needs a per-call option in `OpenAICompatClient`. The memo can still be long (8.3k+ tokens and not finished) |
| Qwen's recommended sampling (thinking: temp 1.0, top_p 0.95, top_k 20, presence_penalty 0; or presence_penalty up to ~1.5 against loops) | Matches what Qwen tuned the model for; presence_penalty discourages repeated text | Qwen3.8 card; server defaults probably already give top_p/top_k | Treats repetition, but the replay shows a coherent, long memo rather than a loop, so this is unlikely to fix lengths on its own. Higher presence_penalty can cause "language mixing". `top_k` is a vLLM extension (send it in the body) |
| Length cap in `SOLVER_WRITE` (e.g. "at most N issues, most important first" or "under N words"; proposed language only for the top issues) | Shrinks the memo itself (the replay memo was 8.3k+ tokens with 18+ issues and redline text) | Our replay; nothing in Qwen's docs | Does not touch the 24k thinking. A cap on issues can hide planted issues from the rubric, and it changes the task for every solver model, not just Qwen, so judge and rubric expectations need checking |
| Stream the response (`stream: true`) | Avoids the 600 s socket timeout on long but healthy calls | Python urlopen timeout semantics | Client change (parse SSE with the standard library). Does not change token counts |

Evidence favours: bound the thinking (a `thinking_token_budget` if NRP honours it, otherwise `reasoning_effort`
low or medium) and give the call a larger `max_tokens` with a matching timeout. A memo-length instruction is
worth adding only if the memo alone still overruns after that.

## Measured on NRP (2026-10-27)

Setup: the memo call (`SOLVER_WRITE`) was replayed raw against `qwen3-small`, using the transcripts that attempt 1
of the 2026-10-24 smoke test built for `s5-m0001` (largest, ~23k-token prompt) and `s5-m0002` (smallest, ~11k).
Two samples per setting and task, 4 calls per setting. Settings not named kept the client's defaults
(temperature 0.7, `max_tokens` 32000). "Issues named" is a rough proxy: NRP's `qwen3` model was given each memo and
the ledger's expected findings and asked which planted issues the memo identifies (5 per task). It is not the
project's judge or rubric. Responses and grades are in `runs/qwen_memo_variants/` (not committed).

| Setting | Finished | Thinking tokens | Memo words | Seconds | Issues named |
|---|---|---|---|---|---|
| Current (xhigh effort, 32k) | 0 of 4 | 28,900 to 31,400 | cut off | 320 to 490 | n/a |
| Qwen sampling (temp 0.6, top_p 0.95, top_k 20, presence_penalty 1.5) | 1 of 4 | 16,500 to 32,000 | 6,800 | 320 to 490 | 5 of 5 |
| `max_tokens` 64000 | 4 of 4 | 26,300 to 37,700 | 6,200 to 8,800 | 400 to 650 | 20 of 20 |
| "Keep the memo focused, under 2,000 words" added to the prompt | 4 of 4 | 15,200 to 23,000 | 1,300 to 2,400 | 160 to 380 | 19 of 20 |
| `chat_template_kwargs: {"enable_thinking": false}` | 4 of 4 | 0 | 1,700 to 2,300 | 30 to 60 | **15 of 20** |
| `thinking_token_budget: 12000` | 4 of 4 | 11,999 (capped) | 5,900 to 8,900 | 215 to 240 | 19 of 20 |
| `reasoning_effort: "medium"` | 4 of 4 | 2,500 to 4,000 | 5,000 to 7,000 | 105 to 140 | 19 of 20 |
| **`reasoning_effort: "low"`** | **4 of 4** | **4,100 to 6,300** | **4,700 to 5,100** | **105 to 150** | **20 of 20** |
| Reference: Haiku's round 5 memos on the same tasks | 6 of 6 | n/a | 6,800 to 9,300 | n/a | 30 of 30 |

What this shows:
- The overrun is the thinking, not the memo. Uncapped, the model thinks for ~30k tokens; Haiku's memos are as long
  as Qwen's, so a long memo is normal for this task.
- NRP honours both thinking controls: `thinking_token_budget` cut thinking at exactly the budget (a 200-token probe
  stopped at 199), and `reasoning_effort` low or medium cut it to a few thousand tokens.
- Thinking off finishes fastest but names fewer planted issues, so it would make the solver look weaker than it is.
- A length line in the prompt works, but it changes the task for every solver model, including Haiku.
- Recommended: `reasoning_effort = "low"` for the solver role. Every call finished with total output (thinking plus
  memo, ~12k to 14k tokens) under half of the 32k `max_tokens`, in at most 150 s, inside the 600 s timeout, and it
  is a documented NRP setting. Caveats: 4 calls per setting on 2 tasks, a proxy grader of the same model family, and
  only the memo call was tested; the tool steps would also run at low effort if the setting applies to the whole
  solver role.

## Open questions / unverified

- NRP's engine, version and server flags for `qwen3-small` (reasoning parser, `--reasoning-config`,
  `--generation-config` or `--override-generation-config`, any `max_new_tokens` cap). Only inferred: vLLM with
  `--reasoning-parser qwen3`. The status page did not load.
- ~~Whether NRP accepts `thinking_token_budget`.~~ Answered 2026-10-27: it is honoured (see "Measured on NRP").
- Whether NRP's context is really 1,000,000 at the server (docs say so). If it were 262,144, a 200k `max_tokens`
  with a 31k prompt would have been capped (vLLM v0.32.0+) or rejected (older). The probe was accepted, so either
  the window is 1M or the server is new enough to cap.
- The output token rate limit: NRP's fair-use page says 48,000 tokens per minute per token and model. CLAUDE.md
  and `configs/pilot_nrp_solver.toml` say 200k. One of them is out of date. Whether SDSC affiliation (twice the
  limit) applies to the lab is unknown.
- Whether the 35% rule ("requests using at least 35% of the model's context length") counts `max_tokens` or only
  the prompt. At 1M context it does not matter below ~350k.
- Real decode speed of qwen3-small on NRP (needed to size the timeout). We only know the 3 timed-out calls ran
  below ~53 tokens/s.
- How memo quality and solver pass rates change under each fix. That is for the experiments now running.

## Applied (2026-10-27)

`extra_body = { reasoning_effort = "low" }` on the solver role in `configs/pilot_nrp_solver.toml`. Full rerun of
`scripts/solve_only.py` (tool steps and memo both at low effort, `runs/qwen_solver_smoke_low/`): 12 of 12 memos,
2,644 to 6,885 words, 190 calls with none failed, 2 to 6 minutes per attempt, ~222k output tokens. Proxy recall
47 of 51; s5-m0001 I2 (free assignment, Supply Agreement Section 16.1) was missed in all 3 attempts, though the
memo-only replays (built from xhigh tool steps) found it, so low effort on the tool steps may cost some recall.
