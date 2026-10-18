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


def _docx(path, *paragraphs):
    import zipfile

    body = "".join(f"<w:p><w:r><w:t>{p[:5]}</w:t></w:r><w:r><w:t>{p[5:]}</w:t></w:r></w:p>" for p in paragraphs)
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("word/document.xml", f'<w:document xmlns:w="w"><w:body>{body}</w:body></w:document>')


def test_office_files_and_emails_are_indexed(tmp_path):
    (tmp_path / "ref").mkdir()
    _docx(tmp_path / "ref" / "contract.docx", REFERENCE)  # each paragraph split across two runs mid-word
    (tmp_path / "ref" / "note.eml").write_text(f"Subject: deal\nContent-Type: text/plain\n\n{NOVEL}\n")
    idx = BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**20, n=8)
    assert idx.containment(REFERENCE) == 1.0  # words split across Word runs are rejoined
    assert idx.containment(NOVEL) == 1.0


def test_saved_index_is_reused_until_the_files_change(tmp_path):
    (tmp_path / "ref").mkdir()
    (tmp_path / "ref" / "a.txt").write_text(REFERENCE)
    args = ([str(tmp_path / "ref")],)
    kw = {"bits": 2**20, "n": 8, "cache_dir": str(tmp_path / "cache")}
    BloomIndex.from_dirs(*args, **kw)
    assert len(list((tmp_path / "cache").iterdir())) == 1
    (tmp_path / "ref" / "a.txt").write_text("unrelated words only " * 20)  # the saved index must not be reused
    (tmp_path / "ref" / "b.txt").write_text(NOVEL)
    idx = BloomIndex.from_dirs(*args, **kw)
    assert idx.containment(NOVEL) == 1.0 and idx.containment(REFERENCE) < 0.05
    again = BloomIndex.from_dirs(*args, **kw)  # unchanged files: loaded from disk
    assert again.array == idx.array and again.count == idx.count


def test_overfull_index_is_refused(tmp_path):
    import pytest

    (tmp_path / "ref").mkdir()
    (tmp_path / "ref" / "a.txt").write_text(" ".join(f"w{i}" for i in range(5000)))
    with pytest.raises(ValueError, match="too full"):
        BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**10, n=8)


def test_short_text_has_no_ngrams():
    idx = BloomIndex(bits=2**16, n=8)
    assert idx.containment("too short") == 0.0


def test_split_is_deterministic_and_respects_ratios():
    ratios = {"train": 0.8, "dev": 0.1, "test": 0.1}
    assert assign_split("m-1", ratios) == assign_split("m-1", ratios)
    counts = Counter(assign_split(f"m-{i}", ratios) for i in range(5000))
    assert 0.77 < counts["train"] / 5000 < 0.83
    assert 0.08 < counts["test"] / 5000 < 0.12


def test_wording_shared_by_two_tasks_is_not_a_match(tmp_path):
    boiler = "This Agreement shall be governed by and construed in accordance with the laws of the State of New York without regard to conflict of laws."
    for task, own in (("t1", REFERENCE), ("t2", NOVEL)):
        d = tmp_path / "ref" / "tasks" / "area" / task / "documents"
        d.mkdir(parents=True)
        (d / "contract.txt").write_text(f"{own}\n{boiler}")
    (tmp_path / "ref" / "tasks" / "area" / "t1" / "task.json").write_text(json.dumps({"rubric": "Identify the indemnity cap problem in the agreement and explain the consequences for the buyer."}))
    grouped = BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**20, n=8, group_depth=3)
    assert grouped.containment(boiler) < 0.1  # in both tasks: ordinary legal language
    assert grouped.containment(REFERENCE) == 1.0 and grouped.containment(NOVEL) == 1.0  # each task's own text still matches
    assert grouped.containment("Identify the indemnity cap problem in the agreement and explain the consequences") == 1.0  # rubric and documents of one task are one group
    flat = BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**20, n=8)
    assert flat.containment(boiler) == 1.0

    cache = str(tmp_path / "cache")  # the grouped index survives a save and load
    BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**20, n=8, group_depth=3, cache_dir=cache)
    again = BloomIndex.from_dirs([str(tmp_path / "ref")], bits=2**20, n=8, group_depth=3, cache_dir=cache)
    assert again.containment(boiler) < 0.1 and again.containment(REFERENCE) == 1.0
