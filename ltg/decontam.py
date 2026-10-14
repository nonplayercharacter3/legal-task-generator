"""Word n-gram containment against reference benchmarks (e.g. a local clone of LAB).

Same measure as the legal-dataset skill's contamination check: the share of a text's
word 8-grams that also occur anywhere in the reference corpus. The reference n-grams
are stored in a Bloom filter so memory stays fixed however large the corpus is.
False positives can only make a task look MORE contaminated, never less.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

_WORD = re.compile(r"\w+")
TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonl"}


def words(text: str) -> list[str]:
    return _WORD.findall(text.lower())


def ngrams(tokens: list[str], n: int) -> list[str]:
    return [" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


class BloomIndex:
    def __init__(self, bits: int = 2**27, n: int = 8) -> None:
        self.bits = bits
        self.n = n
        self.array = bytearray(bits // 8)
        self.count = 0

    def _positions(self, gram: str) -> tuple[int, int, int]:
        d = hashlib.blake2b(gram.encode(), digest_size=12).digest()
        return (
            int.from_bytes(d[0:4], "little") % self.bits,
            int.from_bytes(d[4:8], "little") % self.bits,
            int.from_bytes(d[8:12], "little") % self.bits,
        )

    def add_text(self, text: str) -> None:
        for g in ngrams(words(text), self.n):
            for p in self._positions(g):
                self.array[p >> 3] |= 1 << (p & 7)
            self.count += 1

    def __contains__(self, gram: str) -> bool:
        return all(self.array[p >> 3] & (1 << (p & 7)) for p in self._positions(gram))

    def containment(self, text: str, max_samples: int = 400) -> float:
        grams = ngrams(words(text), self.n)
        if not grams:
            return 0.0
        if len(grams) > max_samples:  # evenly spaced sample keeps long documents cheap
            step = len(grams) / max_samples
            grams = [grams[int(i * step)] for i in range(max_samples)]
        return sum(g in self for g in grams) / len(grams)

    @classmethod
    def from_dirs(cls, dirs: list[str], bits: int = 2**27, n: int = 8) -> "BloomIndex":
        idx = cls(bits=bits, n=n)
        for d in dirs:
            root = Path(d)
            if not root.exists():
                raise FileNotFoundError(f"reference folder not found: {root}")
            for path in root.rglob("*"):
                if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                    idx.add_text(_read_text(path))
        return idx


def _read_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() == ".json":
        try:
            return "\n".join(_strings(json.loads(raw)))
        except json.JSONDecodeError:
            return raw
    return raw


def _strings(obj) -> list[str]:
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, dict):
        return [s for v in obj.values() for s in _strings(v)]
    if isinstance(obj, list):
        return [s for v in obj for s in _strings(v)]
    return []
