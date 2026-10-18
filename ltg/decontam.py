"""Word n-gram containment against reference benchmarks (e.g. a local clone of LAB).

Same measure as the legal-dataset skill's contamination check: the share of a text's
word 8-grams that also occur anywhere in the reference corpus. The reference n-grams
are stored in a Bloom filter so memory stays fixed however large the corpus is.
False positives can only make a task look MORE contaminated, never less.
"""

from __future__ import annotations

import email
import hashlib
import html
import json
import re
import zipfile
from email import policy
from pathlib import Path

_WORD = re.compile(r"\w+")
# LAB keeps its matter documents as Office files and emails (2026-10 clone: 42k .docx, 11k .xlsx, 6k .eml,
# 1k .pptx), so plain-text files alone would screen only its instructions and rubrics.
PLAIN_SUFFIXES = {".md", ".txt", ".json", ".jsonl"}
OFFICE_PARTS = {  # zip members that carry the text of each Office format
    ".docx": re.compile(r"word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml"),
    ".pptx": re.compile(r"ppt/(slides/slide|notesSlides/notesSlide)\d+\.xml"),
    ".xlsx": re.compile(r"xl/(sharedStrings|worksheets/sheet\d+)\.xml"),  # LAB's sheets hold inline strings
}
TEXT_SUFFIXES = PLAIN_SUFFIXES | set(OFFICE_PARTS) | {".eml"}
_BREAK = re.compile(r"</(w:p|a:p|si|c)>|<(w:tab|w:br|w:cr|a:br)\b[^>]*/>")
_TAG = re.compile(r"<[^>]+>")


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

    def false_positive_rate(self) -> float:
        """Chance that an n-gram never added still tests as present: the share of set bits, cubed (3 hashes)."""
        chunk = 1 << 26
        ones = sum(int.from_bytes(self.array[i : i + chunk], "little").bit_count() for i in range(0, len(self.array), chunk))
        return (ones / self.bits) ** 3

    def save(self, path: Path, key: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        with open(tmp, "wb") as f:
            f.write((json.dumps({"key": key, "bits": self.bits, "n": self.n, "count": self.count}) + "\n").encode())
            f.write(self.array)
        tmp.replace(path)

    @classmethod
    def load(cls, path: Path, key: str) -> "BloomIndex | None":
        """The saved index, or None when there is none or it was built from other files or settings."""
        if not path.exists():
            return None
        with open(path, "rb") as f:
            head = json.loads(f.readline())
            if head.get("key") != key:
                return None
            idx = cls(bits=head["bits"], n=head["n"])
            f.readinto(idx.array)
        idx.count = head["count"]
        return idx

    @classmethod
    def from_dirs(cls, dirs: list[str], bits: int = 2**27, n: int = 8, cache_dir: str | None = None,
                  max_false_positive: float = 0.05) -> "BloomIndex":
        """Index every readable file under `dirs`. With `cache_dir`, a saved index is reused while the files
        (paths, sizes, modification times) and settings are unchanged: building LAB's takes about 25 minutes."""
        files = []
        for d in dirs:
            root = Path(d)
            if not root.exists():
                raise FileNotFoundError(f"reference folder not found: {root}")
            files += sorted(p for p in root.rglob("*") if ".git" not in p.parts and p.is_file() and p.suffix.lower() in TEXT_SUFFIXES)
        key = _fingerprint(files, bits, n)
        cache = Path(cache_dir) / f"{key[:16]}.bloom" if cache_dir else None
        if cache and (idx := cls.load(cache, key)) is not None:
            return idx
        idx = cls(bits=bits, n=n)
        for path in files:
            idx.add_text(_read_text(path))
        if idx.count == 0:  # an empty index would pass every task while looking screened
            raise ValueError(f"no reference text found in {dirs} (looked for {sorted(TEXT_SUFFIXES)} files)")
        fp = idx.false_positive_rate()
        if fp > max_false_positive:  # an overfull filter calls everything copied
            raise ValueError(f"reference index too full ({idx.count:,} n-grams, false positive rate {fp:.1%}); "
                             "raise gates.decontam_bloom_bits")
        if cache:
            idx.save(cache, key)
        return idx


READER_VERSION = 2  # bump when text extraction changes, so saved indexes are rebuilt


def _fingerprint(files: list[Path], bits: int, n: int) -> str:
    h = hashlib.sha256(f"{READER_VERSION}|{bits}|{n}".encode())
    for p in files:
        st = p.stat()
        h.update(f"|{p.resolve()}|{st.st_size}|{st.st_mtime_ns}".encode())
    return h.hexdigest()


def _xml_text(xml: str) -> str:
    """Text of an Office XML part. Runs inside a paragraph join without a space, since Word splits words across
    runs ("Indem" + "nify"); paragraph ends, tabs and breaks become spaces."""
    return html.unescape(_TAG.sub("", _BREAK.sub(" ", xml)))


def _office_text(path: Path) -> str:
    want = OFFICE_PARTS[path.suffix.lower()]
    try:
        with zipfile.ZipFile(path) as z:
            return "\n".join(_xml_text(z.read(n).decode("utf-8", "replace")) for n in z.namelist() if want.fullmatch(n))
    except (zipfile.BadZipFile, KeyError, OSError):
        return ""  # an LFS pointer stub or a damaged file: nothing to index


def _eml_text(path: Path) -> str:
    msg = email.message_from_bytes(path.read_bytes(), policy=policy.default)
    parts = [str(msg.get("subject", ""))]
    for part in msg.walk():
        if part.get_content_maintype() == "text" and not part.is_attachment():
            try:
                body = part.get_content()
            except (LookupError, ValueError):
                continue
            parts.append(_TAG.sub(" ", body) if part.get_content_subtype() == "html" else body)
    return "\n".join(parts)


def _read_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in OFFICE_PARTS:
        return _office_text(path)
    if suffix == ".eml":
        return _eml_text(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".json":
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
