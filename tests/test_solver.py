"""The tool-using solver: tools, the step loop, and paging through the pipeline."""

import json

from ltg import prompts
from ltg.config import load_config
from ltg.models import extract_input
from ltg.orchestrator import Pipeline
from ltg.solver import read_file, search, solve

DOCS = {"a.md": "line one\nThe Supplier may assign freely.\nline three\n", "b.md": "nothing here\n"}


def test_read_file_pages_through_a_document():
    first = read_file(DOCS, "a.md", 1, page_chars=20)
    assert first.startswith("a.md, page 1 of 3:\n")
    pages = [read_file(DOCS, "a.md", k, 20).split("\n", 1)[1] for k in (1, 2, "3")]
    assert "".join(pages) == DOCS["a.md"]  # pages are exact slices, page numbers may arrive as strings
    assert read_file(DOCS, "a.md", 4, 20).startswith("ERROR")
    assert read_file(DOCS, "missing.md", 1, 20).startswith("ERROR")


def test_search_reports_file_page_and_line():
    assert search(DOCS, "MAY ASSIGN", None, page_chars=20) == "a.md page 1 line 2: The Supplier may assign freely."
    assert search(DOCS, "assign", "b.md", 20).startswith("No lines")
    assert search(DOCS, "assign", "missing.md", 20).startswith("ERROR")
    assert search(DOCS, " ", None, 20).startswith("ERROR")


class Scripted:
    """Plays a fixed list of actions, then records what the writer was shown."""

    def __init__(self, actions):
        self.actions, self.written = list(actions), None

    def complete(self, role, system, user):
        if system == prompts.SOLVER_STEP:
            return json.dumps(self.actions.pop(0))
        self.written = extract_input(user)
        return "MEMO"


def test_loop_runs_tools_until_finish_and_survives_bad_actions():
    client = Scripted([
        {"tool": "read_file", "filename": "a.md", "page": 1},
        {"tool": "read_file", "filename": "nope.md"},
        {"tool": "delete_everything"},
        {"tool": "search", "query": "assign"},
        {"tool": "finish"},
    ])
    sol = solve(client, "Review.", DOCS, max_steps=10, page_chars=1000)
    assert sol.answer == "MEMO" and len(sol.steps) == 4
    assert sol.steps[1]["result"].startswith("ERROR") and "unknown tool" in sol.steps[2]["result"]
    assert sol.files_opened() == ["a.md"]
    assert client.written["steps"] == sol.steps


def test_loop_writes_an_answer_when_steps_run_out():
    client = Scripted([{"tool": "search", "query": "line"}] * 3)
    sol = solve(client, "Review.", DOCS, max_steps=3)
    assert sol.answer == "MEMO" and len(sol.steps) == 3


def test_paging_does_not_change_what_the_fake_solver_finds(tmp_path):
    reps = []
    for k, page in enumerate((6000, 300)):
        cfg = load_config(None, {"run": {"out_dir": str(tmp_path / str(k)), "n_matters": 6, "seed": 7},
                                 "gates": {"solver_page_chars": page, "solver_max_steps": 100}})
        reps.append(Pipeline(cfg).run())
    assert reps[0]["matters"] == reps[1]["matters"]
    assert reps[1]["model_calls"]["solver"]["calls"] > reps[0]["model_calls"]["solver"]["calls"]  # more pages, more steps
    trace = json.loads(next((tmp_path / "1" / "accepted").glob("*/solver/attempt_1.trace.json")).read_text())
    assert trace and all(s["action"]["tool"] == "read_file" for s in trace)
