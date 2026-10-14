"""Source scout: finds real precedents to adapt.

For now it reads precedents from local folders. Each file is Markdown or plain text:
    line 1: "# <title>"
    line 2: "tags: <comma-separated tags>"   (optional; match on agreement type)
    rest:   the agreement text

The bundled files in ltg/data/precedents are short SYNTHETIC samples written for
testing only. For real runs, save EDGAR exhibit agreements (or other licensed
precedents) as .md/.txt into a folder and list it under [sources].precedent_dirs.
An EDGAR fetcher is the planned next step.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path

BUILTIN_DIR = Path(__file__).parent / "data" / "precedents"


@dataclass
class Precedent:
    id: str
    title: str
    tags: list[str]
    text: str

    def excerpt(self, chars: int) -> str:
        return self.text[:chars]


def load_precedents(dirs: list[str] | None = None) -> list[Precedent]:
    roots = [Path(d) for d in dirs] if dirs else [BUILTIN_DIR]
    out: list[Precedent] = []
    for root in roots:
        if not root.exists():
            raise FileNotFoundError(f"precedent folder not found: {root}")
        for path in sorted(root.rglob("*")):
            if path.suffix.lower() not in (".md", ".txt") or not path.is_file():
                continue
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            title = lines[0].lstrip("# ").strip() if lines else path.stem
            tags: list[str] = []
            body_start = 1
            if len(lines) > 1 and lines[1].lower().startswith("tags:"):
                tags = [t.strip().lower() for t in lines[1][5:].split(",") if t.strip()]
                body_start = 2
            out.append(Precedent(id=path.stem, title=title, tags=tags, text="\n".join(lines[body_start:]).strip()))
    return out


def select_precedents(pool: list[Precedent], agreement_type: str, k: int, rng: random.Random) -> list[Precedent]:
    """Prefer precedents tagged with the agreement type; fall back to any."""
    matching = [p for p in pool if agreement_type.lower() in p.tags]
    chosen = rng.sample(matching, min(k, len(matching)))
    if len(chosen) < k:
        rest = [p for p in pool if p not in chosen]
        chosen += rng.sample(rest, min(k - len(chosen), len(rest)))
    return chosen
