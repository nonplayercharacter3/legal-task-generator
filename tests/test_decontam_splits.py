import json
from collections import Counter

from ltg.decontam import BloomIndex
from ltg.splits import assign_split

REFERENCE = (
    "The seller shall indemnify the buyer for all losses arising from any breach of the "
    "representations and warranties set forth in article four of this agreement, subject to "
    "the deductible and the cap described in section nine point two."
)
NOVEL = (
    "Quarterly volume rebates accrue on delivered tonnage and are credited against the next "
    "invoice once the distributor confirms receipt of the reconciliation statement in writing."
)


def test_containment_separates_copied_from_novel(tmp_path):
    (tmp_path / "ref").mkdir()
    (tmp_path / "ref" / "task.json").write_text(json.dumps({"criteria": [{"text": REFERENCE}]}))
    idx = BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**20, n=8)
    assert idx.containment(REFERENCE) == 1.0
    assert idx.containment("Preamble words. " + REFERENCE) > 0.8
    assert idx.containment(NOVEL) < 0.05


def test_reference_folder_without_text_is_an_error(tmp_path):
    import pytest

    (tmp_path / "ref").mkdir()
    (tmp_path / "ref" / "scan.pdf").write_bytes(b"%PDF-1.4")  # present, but nothing it can read
    with pytest.raises(ValueError, match="no reference text"):
        BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**16, n=8)
    with pytest.raises(FileNotFoundError):
        BloomIndex.from_dirs([str(tmp_path / "missing")], bits=2**16, n=8)


def test_short_text_has_no_ngrams():
    idx = BloomIndex(bits=2**16, n=8)
    assert idx.containment("too short") == 0.0


def test_split_is_deterministic_and_respects_ratios():
    ratios = {"train": 0.8, "dev": 0.1, "test": 0.1}
    assert assign_split("m-1", ratios) == assign_split("m-1", ratios)
    counts = Counter(assign_split(f"m-{i}", ratios) for i in range(5000))
    assert 0.77 < counts["train"] / 5000 < 0.83
    assert 0.08 < counts["test"] / 5000 < 0.12
