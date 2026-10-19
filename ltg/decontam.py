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
    """N-grams of a reference corpus in a Bloom filter.

    With groups (one per benchmark task), an n-gram found in two or more groups goes into a second filter,
    `common`, and stops counting as a match: wording shared across tasks ("shall be governed by and construed in
    accordance with the laws of") is ordinary legal language, while text found in one task only is that task's
    content. Without groups every n-gram counts.
    """

    def __init__(self, bits: int = 2**27, n: int = 8, grouped: bool = False) -> None:
        self.bits = bits
        self.n = n
        self.array = bytearray(bits // 8)
        self.common = bytearray(bits // 8) if grouped else None
        self.count = 0

    def _positions(self, gram: str) -> tuple[int, int, int]:
        return self._split(hashlib.blake2b(gram.encode(), digest_size=12).digest())

    def _split(self, d: bytes) -> tuple[int, int, int]:
        return (
            int.from_bytes(d[0:4], "little") % self.bits,
            int.from_bytes(d[4:8], "little") % self.bits,
            int.from_bytes(d[8:12], "little") % self.bits,
        )

    @staticmethod
    def _has(array: bytearray, pos: tuple[int, int, int]) -> bool:
        return all(array[p >> 3] & (1 << (p & 7)) for p in pos)

    @staticmethod
    def _set(array: bytearray, pos: tuple[int, int, int]) -> None:
        for p in pos:
            array[p >> 3] |= 1 << (p & 7)

    def add_text(self, text: str) -> None:
        for g in ngrams(words(text), self.n):
            self._set(self.array, self._positions(g))
            self.count += 1

    def add_group(self, texts: list[str]) -> None:
        """Add one task's texts. Its n-grams already seen in an earlier task are marked common."""
        digests = {hashlib.blake2b(g.encode(), digest_size=12).digest() for t in texts for g in ngrams(words(t), self.n)}
        for d in digests:
            pos = self._split(d)
            if self._has(self.array, pos):
                self._set(self.common, pos)
            else:
                self._set(self.array, pos)
        self.count += len(digests)

    def __contains__(self, gram: str) -> bool:
        pos = self._positions(gram)
        return self._has(self.array, pos) and not (self.common is not None and self._has(self.common, pos))

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
        head = {"key": key, "bits": self.bits, "n": self.n, "count": self.count, "grouped": self.common is not None}
        with open(tmp, "wb") as f:
            f.write((json.dumps(head) + "\n").encode())
            f.write(self.array)
            if self.common is not None:
                f.write(self.common)
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
            idx = cls(bits=head["bits"], n=head["n"], grouped=head.get("grouped", False))
            f.readinto(idx.array)
            if idx.common is not None:
                f.readinto(idx.common)
        idx.count = head["count"]
        return idx

    @classmethod
    def from_dirs(cls, dirs: list[str], bits: int = 2**27, n: int = 8, cache_dir: str | None = None,
                  max_false_positive: float = 0.05, group_depth: int = 0) -> "BloomIndex":
        """Index every readable file under `dirs`. With `cache_dir`, a saved index is reused while the files
        (paths, sizes, modification times) and settings are unchanged: building LAB's takes about 30 minutes.

        `group_depth` > 0 groups files by the first that many folders of their path under each root (3 for LAB:
        tasks/<area>/<task>), and wording found in two or more groups stops counting as a match."""
        files: list[tuple[Path, Path]] = []
        for d in dirs:
            root = Path(d)
            if not root.exists():
                raise FileNotFoundError(f"reference folder not found: {root}")
            files += sorted((root, p) for p in root.rglob("*")
                            if ".git" not in p.parts and p.is_file() and p.suffix.lower() in TEXT_SUFFIXES)
        key = _fingerprint([p for _, p in files], bits, n, group_depth)
        cache = Path(cache_dir) / f"{key[:16]}.bloom" if cache_dir else None
        if cache and (idx := cls.load(cache, key)) is not None:
            return idx
        idx = cls(bits=bits, n=n, grouped=group_depth > 0)
        if group_depth > 0:
            groups: dict[tuple, list[Path]] = {}
            for root, p in files:
                rel = p.relative_to(root).parts
                unit = rel[:group_depth] if len(rel) > group_depth else rel[:-1]  # files above task level: by folder
                groups.setdefault((str(root), *unit), []).append(p)
            for paths in groups.values():
                idx.add_group([_read_text(p) for p in paths])
        else:
            for _, path in files:
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


READER_VERSION = 3  # bump when text extraction or indexing changes, so saved indexes are rebuilt


def _fingerprint(files: list[Path], bits: int, n: int, group_depth: int = 0) -> str:
    h = hashlib.sha256(f"{READER_VERSION}|{bits}|{n}|{group_depth}".encode())
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
