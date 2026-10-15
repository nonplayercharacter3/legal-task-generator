"""The Claude Agent SDK backend, run against a stub SDK module backed by the fake model (no network, no login)."""

import os
import sys
import types
from dataclasses import dataclass, field

import pytest

from ltg.config import load_config
from ltg.fake import FakeModel
from ltg.models import ClaudeAgentClient, ModelError
from ltg.orchestrator import Pipeline

from .test_openai_compat import ROLE_BY_SYSTEM


def stub_sdk(fake, stop_reason="end_turn", is_error=False):
    """A stand-in for `claude_agent_sdk` that answers with the fake model and records every options object."""
    sdk = types.ModuleType("claude_agent_sdk")
    sdk.calls = []

    @dataclass
    class ClaudeAgentOptions:
        system_prompt: str | None = None
        model: str | None = None
        tools: list | None = None
        setting_sources: list | None = None
        strict_mcp_config: bool = False
        max_turns: int | None = None
        cwd: str | None = None

    @dataclass
    class TextBlock:
        text: str

    @dataclass
    class AssistantMessage:
        content: list
        stop_reason: str | None = None

    @dataclass
    class ResultMessage:
        subtype: str = "success"
        is_error: bool = False
        result: str | None = None
        usage: dict = field(default_factory=dict)

    async def query(prompt, options):
        sdk.calls.append(options)
        text = fake.complete(ROLE_BY_SYSTEM[options.system_prompt], options.system_prompt, prompt)
        yield AssistantMessage([TextBlock("<think>planning</think>" + text)], stop_reason)
        yield ResultMessage(subtype="error_during_execution" if is_error else "success", is_error=is_error, result=None,
                            usage={"input_tokens": 3, "cache_read_input_tokens": 7, "output_tokens": 5})

    sdk.ClaudeAgentOptions, sdk.TextBlock, sdk.AssistantMessage, sdk.ResultMessage, sdk.query = (
        ClaudeAgentOptions, TextBlock, AssistantMessage, ResultMessage, query)
    return sdk


def test_pipeline_runs_through_the_agent_sdk_with_nothing_but_the_payload(tmp_path, monkeypatch):
    sdk = stub_sdk(FakeModel(seed=7))
    monkeypatch.setitem(sys.modules, "claude_agent_sdk", sdk)
    cfg = load_config(None, {"run": {"out_dir": str(tmp_path), "n_matters": 2, "seed": 7},
                             "backend": {"kind": "claude_sdk", "default_model": "sonnet", "models": {"solver": "opus"}}})
    rep = Pipeline(cfg).run()
    assert rep["errors"] == 0 and rep["candidates"] == 2
    assert rep["model_calls"]["solver"]["input_tokens"] > 0
    assert {o.model for o in sdk.calls} == {"sonnet", "opus"}
    for o in sdk.calls:  # every call: no tools, no local settings or MCP servers, one turn, an empty folder
        assert o.tools == [] and o.setting_sources == [] and o.strict_mcp_config and o.max_turns == 1
        assert os.listdir(o.cwd) == []


def test_reasoning_is_stripped_and_usage_logged(monkeypatch):
    monkeypatch.setitem(sys.modules, "claude_agent_sdk", stub_sdk(FakeModel(seed=7)))
    client = ClaudeAgentClient("sonnet")
    from ltg import prompts
    from ltg.models import render_input

    out = client.complete("solver", prompts.SOLVER_WRITE, render_input({"instruction": "x", "files": [], "steps": []}))
    assert out.startswith("I cannot assess")
    assert (client.log.records[0].input_tokens, client.log.records[0].output_tokens) == (10, 5)


@pytest.mark.parametrize("kw, match", [({"stop_reason": "max_tokens"}, "truncated"), ({"is_error": True}, "error")])
def test_truncated_or_failed_calls_raise(monkeypatch, kw, match):
    monkeypatch.setitem(sys.modules, "claude_agent_sdk", stub_sdk(FakeModel(seed=7), **kw))
    from ltg import prompts
    from ltg.models import render_input

    client = ClaudeAgentClient("sonnet")
    with pytest.raises(ModelError, match=match):
        client.complete("solver", prompts.SOLVER_WRITE, render_input({"instruction": "x", "files": [], "steps": []}))
    assert client.log.records[-1].ok is False


def test_missing_sdk_says_how_to_install(monkeypatch):
    monkeypatch.setitem(sys.modules, "claude_agent_sdk", None)  # makes the import fail
    with pytest.raises(ModelError, match="pip install claude-agent-sdk"):
        ClaudeAgentClient("sonnet")
