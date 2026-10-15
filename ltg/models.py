"""Model clients.

Every stage talks to a model through `ModelClient.complete(role, system, user)`.
The role name lets the config route different stages to different models
(for example a strong model as the solver and a cheaper one as the drafter).

Two backends:
  * FakeModel (ltg.fake): deterministic, offline, used for tests and demos.
  * OpenAICompatClient: any OpenAI-compatible /chat/completions endpoint
    (vLLM, Ollama, OpenAI, or a provider's OpenAI-compatible endpoint).
"""

from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from typing import Any, Protocol

INPUT_OPEN, INPUT_CLOSE = "<input>", "</input>"
_THINK = re.compile(r"<think>.*?</think>", re.S)  # reasoning models served without a reasoning parser


class ModelClient(Protocol):
    def complete(self, role: str, system: str, user: str) -> str: ...


@dataclass
class CallRecord:
    role: str
    model: str
    seconds: float
    input_tokens: int | None = None
    output_tokens: int | None = None
    ok: bool = True
    error: str | None = None


@dataclass
class CallLog:
    records: list[CallRecord] = field(default_factory=list)

    def add(self, rec: CallRecord) -> None:
        self.records.append(rec)

    def by_role(self) -> dict[str, dict[str, int]]:
        out: dict[str, dict[str, int]] = {}
        for r in self.records:
            s = out.setdefault(r.role, {"calls": 0, "input_tokens": 0, "output_tokens": 0, "errors": 0})
            s["calls"] += 1
            s["input_tokens"] += r.input_tokens or 0
            s["output_tokens"] += r.output_tokens or 0
            s["errors"] += 0 if r.ok else 1
        return out

    def dump(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            for r in self.records:
                f.write(json.dumps(asdict(r)) + "\n")


class ModelError(RuntimeError):
    pass


class OpenAICompatClient:
    """Minimal OpenAI-compatible chat client with no third-party dependencies."""

    def __init__(
        self,
        base_url: str,
        default_model: str,
        api_key_env: str | None = None,
        models: dict[str, str] | None = None,
        temperature: float = 0.7,
        max_tokens: int = 8000,
        timeout: float = 600,
        max_retries: int = 3,
        log: CallLog | None = None,
    ) -> None:
        self.url = base_url.rstrip("/") + "/chat/completions"
        self.default_model = default_model
        self.models = models or {}
        self.api_key = os.environ.get(api_key_env, "") if api_key_env else ""
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries
        self.log = log if log is not None else CallLog()

    def model_for(self, role: str) -> str:
        return self.models.get(role, self.default_model)

    def complete(self, role: str, system: str, user: str) -> str:
        model = self.model_for(role)
        body = json.dumps(
            {
                "model": model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            }
        ).encode()
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        last_err = ""
        for attempt in range(self.max_retries + 1):
            t0 = time.time()
            try:
                req = urllib.request.Request(self.url, data=body, headers=headers, method="POST")
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = json.loads(resp.read())
                choice = data["choices"][0]
                usage = data.get("usage") or {}
                self.log.add(
                    CallRecord(
                        role=role,
                        model=model,
                        seconds=round(time.time() - t0, 2),
                        input_tokens=usage.get("prompt_tokens"),
                        output_tokens=usage.get("completion_tokens"),
                    )
                )
                if choice.get("finish_reason") == "length":  # a cut-off document must not pass as complete
                    raise ModelError(f"{role}: output truncated at max_tokens={self.max_tokens}")
                return _THINK.sub("", choice["message"]["content"] or "").strip()
            except urllib.error.HTTPError as e:
                last_err = f"HTTP {e.code}: {e.read()[:300]!r}"
                retryable = e.code == 429 or e.code >= 500
            except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as e:
                last_err = f"{type(e).__name__}: {e}"
                retryable = not isinstance(e, KeyError)
            self.log.add(CallRecord(role=role, model=model, seconds=round(time.time() - t0, 2), ok=False, error=last_err))
            if not retryable or attempt == self.max_retries:
                break
            time.sleep(min(2**attempt * 2, 30))
        raise ModelError(f"{role}: {last_err}")


# ---------------------------------------------------------------- helpers


def render_input(payload: dict[str, Any]) -> str:
    """Wrap a stage's structured input so prompts and the fake model see the same thing."""
    return f"{INPUT_OPEN}\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n{INPUT_CLOSE}"


def extract_input(user: str) -> dict[str, Any]:
    start = user.index(INPUT_OPEN) + len(INPUT_OPEN)
    end = user.index(INPUT_CLOSE, start)
    return json.loads(user[start:end])


_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.S)


def parse_json(text: str) -> Any:
    """Parse a JSON object from model output, tolerating code fences and stray prose."""
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    m = _FENCE.search(text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in model output")
    depth, in_str, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise ValueError("unbalanced JSON object in model output")


_WHOLE_FENCE = re.compile(r"^```[\w-]*\n(.*)\n```$", re.S)


def call_text(client: ModelClient, role: str, system: str, user: str) -> str:
    """Call a model for long free text (a document or memo). Raw text, not a JSON string, so escaping can't break."""
    out = client.complete(role, system, user).strip()
    m = _WHOLE_FENCE.match(out)
    out = (m.group(1) if m else out).strip()
    if not out:
        raise ModelError(f"{role}: empty output")
    return out


def call_json(client: ModelClient, role: str, system: str, user: str, retries: int = 1) -> dict[str, Any]:
    """Call a model and parse a JSON object, retrying once with a reminder on bad output."""
    prompt = user
    last = ""
    for _ in range(retries + 1):
        out = client.complete(role, system, prompt)
        try:
            obj = parse_json(out)
            if isinstance(obj, dict):
                return obj
            last = "output was JSON but not an object"
        except (ValueError, json.JSONDecodeError) as e:
            last = str(e)
        prompt = user + "\n\nYour previous reply was not a valid JSON object. Reply with ONLY the JSON object."
    raise ModelError(f"{role}: could not parse JSON ({last})")
