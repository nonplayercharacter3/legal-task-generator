"""Tool-using solver: works through the matter folder like an associate, instead of reading one giant prompt.

Each step is one model call that returns a JSON action. The tool runs here, on the documents only, so the
solver can never reach the ledger or the rubric. After `finish` (or when steps run out) a last call writes
the work product in raw Markdown from the transcript of what it read.

The protocol is plain JSON over `complete()`, not native tool calling, so it works on any OpenAI-compatible
endpoint without model-specific server flags.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from . import prompts
from .models import ModelClient, call_json, call_text, render_input
from .stages import Documents

MAX_HITS = 20


@dataclass
class Solution:
    answer: str
    steps: list[dict] = field(default_factory=list)  # [{"action": {...}, "result": str}]

    def files_opened(self) -> list[str]:
        return sorted({s["action"]["filename"] for s in self.steps if s["action"].get("tool") == "read_file" and not s["result"].startswith("ERROR")})


def _pages(text: str, page_chars: int) -> int:
    return max(1, -(-len(text) // page_chars))


def read_file(docs: Documents, filename, page, page_chars: int) -> str:
    if filename not in docs:
        return f"ERROR: no file named {filename!r}"
    n = _pages(docs[filename], page_chars)
    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 0
    if not 1 <= page <= n:
        return f"ERROR: {filename} has pages 1 to {n}"
    return f"{filename}, page {page} of {n}:\n" + docs[filename][(page - 1) * page_chars : page * page_chars]


def search(docs: Documents, query, filename, page_chars: int) -> str:
    q = str(query or "").strip().lower()
    if not q:
        return "ERROR: empty query"
    if filename and filename not in docs:
        return f"ERROR: no file named {filename!r}"
    hits = []
    for name in [filename] if filename else docs:
        offset = 0
        for n, line in enumerate(docs[name].splitlines(keepends=True), 1):
            if q in line.lower():
                hits.append(f"{name} page {offset // page_chars + 1} line {n}: {line.strip()}")
            offset += len(line)
    if not hits:
        return f"No lines contain {query!r}."
    more = f"\n({len(hits) - MAX_HITS} more not shown)" if len(hits) > MAX_HITS else ""
    return "\n".join(hits[:MAX_HITS]) + more


def solve(client: ModelClient, instruction: str, docs: Documents, max_steps: int = 20, page_chars: int = 6000) -> Solution:
    files = [{"filename": f, "words": len(c.split())} for f, c in docs.items()]
    steps: list[dict] = []
    # ponytail: the transcript keeps every page read, so context grows with the folder (~30k tokens for five long
    # documents). If that exceeds the model's window, drop old page text and keep only the solver's notes.
    while len(steps) < max_steps:
        payload = {"instruction": instruction, "files": files, "steps": steps, "steps_left": max_steps - len(steps)}
        action = call_json(client, "solver", prompts.SOLVER_STEP, render_input(payload))
        tool = action.get("tool")
        if tool == "finish":
            break
        if tool == "read_file":
            result = read_file(docs, action.get("filename"), action.get("page", 1), page_chars)
        elif tool == "search":
            result = search(docs, action.get("query"), action.get("filename"), page_chars)
        else:
            result = f"ERROR: unknown tool {tool!r}; use read_file, search or finish"
        steps.append({"action": action, "result": result})
    payload = {"instruction": instruction, "files": files, "steps": steps}
    return Solution(call_text(client, "solver", prompts.SOLVER_WRITE, render_input(payload)), steps)
