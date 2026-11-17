import json
import subprocess
from datetime import datetime

import pytest

from ltg import batch, orchestrator
from ltg.cli import main
from ltg.fake import FakeModel
from ltg.models import ModelError


def test_parse_seeds():
    assert batch.parse_seeds("46-49") == [46, 47, 48, 49]
    assert batch.parse_seeds("46, 48,50-51,48") == [46, 48, 50, 51]


def test_limit_wait_reads_the_reset_time():
    now = datetime(2026, 11, 17, 18, 0)
    msg = "Claude Code returned an error result: You've hit your session limit · resets 8:40pm (America/Los_Angeles)"
    assert batch.limit_wait(msg, 1800, now) == 2 * 3600 + 40 * 60 + 120
    assert batch.limit_wait("You've hit your weekly limit · resets Nov 20, 9am", 1800, now) == 15 * 3600 + 120  # next 9am
    assert batch.limit_wait("You've hit your usage limit", 1800, now) == 1800
    assert batch.limit_wait("HTTP 500: b'oops'", 1800, now) is None


@pytest.fixture
def ws(tmp_path, monkeypatch):
    """A working folder with a deferred-labels fake config; runs/ lives in it."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "gen.toml").write_text('[run]\nn_matters = 2\n[gates]\nsolver_check = "defer"\n')
    return tmp_path


def args(*extra):
    return ["batch", "--config", "gen.toml", "--out-pattern", "runs/b{seed}", "--no-commit", "--retry-wait", "1", *extra]


def tasks(run):
    return [json.loads(t.read_text()) for t in sorted((run / "accepted").glob("*/task.json"))]


def test_batch_generates_labels_and_exports(ws, capsys):
    assert main(args("--seeds", "3-4", "--export-out", "export")) == 0
    for s in (3, 4):
        rep = json.loads((ws / f"runs/b{s}/report.json").read_text())
        assert rep["errors"] == 0 and rep["label_pending"] == 0
        assert all("label_pending" not in t and t["difficulty"] for t in tasks(ws / f"runs/b{s}"))
    assert (ws / "export/train.jsonl").exists() and not (ws / "runs/.batch.lock").exists()
    assert main(args("--seeds", "3-4")) == 0  # a rerun finds both seeds finished and labelled
    assert capsys.readouterr().out.count("already finished") == 2


def test_batch_waits_for_a_usage_limit_then_resumes(ws, monkeypatch):
    fails = {"n": 2}

    class Limited(FakeModel):
        def complete(self, role, system, user):
            if role == "ledger_writer" and fails["n"]:
                fails["n"] -= 1
                raise ModelError("ledger_writer: You've hit your session limit · resets 8:40pm (America/Los_Angeles)")
            return super().complete(role, system, user)

    monkeypatch.setattr(orchestrator, "build_client", lambda c, log: Limited(seed=c.run.seed, log=log))
    slept = []
    ns = __import__("argparse").Namespace
    a = ns(config="gen.toml", seeds="5", out_pattern="runs/b{seed}", label_config=None, no_label=False, commit=False,
           author=None, branch=None, max_tries=3, retry_wait=1, export_out=None, lock="runs/.batch.lock",
           stop_file="runs/.batch.stop")
    assert batch.run_batch(a, sleep=slept.append) == 0
    assert len(slept) == 1 and slept[0] > 120  # waited for the reset, not the 1-minute retry
    assert json.loads((ws / "runs/b5/report.json").read_text())["errors"] == 0 and (ws / "runs/b5/tries").is_dir()


def test_batch_stops_on_an_nrp_refusal(ws, monkeypatch):
    class Refused(FakeModel):
        def complete(self, role, system, user):
            if role == "ledger_writer":
                raise ModelError("ledger_writer: HTTP 403: b'{\"error\": \"key revoked\"}'")
            return super().complete(role, system, user)

    monkeypatch.setattr(orchestrator, "build_client", lambda c, log: Refused(seed=c.run.seed, log=log))
    monkeypatch.setattr(batch.time, "sleep", lambda s: pytest.fail("must not wait on a refusal"))
    assert main(args("--seeds", "6-7")) == 2
    assert not (ws / "runs/b7").exists()


def git(*a, cwd):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout


def repo(ws):
    git("init", "-q", "--bare", "-b", "main", str(ws / "origin.git"), cwd=ws)
    git("init", "-q", "-b", "main", cwd=ws)
    (ws / ".gitignore").write_text("runs/\n")
    git("add", ".gitignore", "gen.toml", cwd=ws)
    git("-c", "user.name=T", "-c", "user.email=t@x", "commit", "-qm", "init", cwd=ws)
    git("remote", "add", "origin", str(ws / "origin.git"), cwd=ws)
    git("push", "-q", "-u", "origin", "main", cwd=ws)


def test_batch_commits_by_the_run_output_rule(ws):
    repo(ws)
    a = [x for x in args("--seeds", "8") if x != "--no-commit"]
    assert main(a + ["--author", "Sirui She <s@example.com>"]) == 0
    log = git("log", "--format=%an <%ae>|%s", cwd=ws).splitlines()
    assert log[0].startswith("Sirui She <s@example.com>|Labels for seed 8") and log[1].startswith("Sirui She <s@example.com>|Round 8:")
    files = git("ls-files", cwd=ws).split()
    assert "runs/b8/report.json" in files and "runs/b8/settings.json" in files
    assert any(f.startswith("runs/b8/accepted/") and f.endswith("task.json") for f in files)
    assert not any(f.endswith(("calls.jsonl", ".trace.json", "label_error.txt")) for f in files)
    assert git("rev-parse", "HEAD", cwd=ws) == git("rev-parse", "origin/main", cwd=ws)  # pushed
    body = git("log", "-1", "--format=%B", cwd=ws)
    assert "Co-Authored-By" not in body and "Committed by `ltg batch`" in body


def test_batch_on_a_branch_pushes_it_and_opens_one_pr(ws, monkeypatch):
    repo(ws)
    prs = []
    monkeypatch.setattr(batch, "open_pr", lambda branch, title: prs.append((branch, title)) or True)
    a = [x for x in args("--seeds", "9-10") if x != "--no-commit"]
    assert main(a + ["--branch", "lm/v2-test", "--author", "Lab Mate <lm@example.com>"]) == 0
    assert git("rev-parse", "--abbrev-ref", "HEAD", cwd=ws).strip() == "lm/v2-test"
    assert git("rev-parse", "HEAD", cwd=ws) == git("rev-parse", "origin/lm/v2-test", cwd=ws)
    assert git("rev-parse", "origin/main", cwd=ws) == git("rev-parse", "main", cwd=ws)  # main untouched
    assert len(git("log", "--oneline", "main..HEAD", cwd=ws).splitlines()) == 4  # round and labels, per seed
    assert prs == [("lm/v2-test", "Round 9: 2 of 2 accepted (seed 9, gen, labels next)")]
