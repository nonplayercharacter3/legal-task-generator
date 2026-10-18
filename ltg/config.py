"""Run configuration, loaded from TOML. Every field has a default, so an empty file works."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field, fields, replace
from typing import Any

from .models import CallLog, ClaudeAgentClient, ModelClient, OpenAICompatClient, RoleRouter


@dataclass
class RunCfg:
    n_matters: int = 5
    seed: int = 7
    out_dir: str = "runs/demo"
    concurrency: int = 4  # matters in flight at once; each matter's own calls stay in order


@dataclass
class BackendCfg:
    kind: str = "fake"  # "fake" | "openai_compat" | "claude_sdk"
    base_url: str = "http://localhost:8000/v1"
    api_key_env: str = "LTG_API_KEY"
    default_model: str = ""
    models: dict[str, str] = field(default_factory=dict)  # per-role model overrides on this backend
    # Per-role backends, e.g. Opus writing through the SDK while an open model on a vLLM or NRP endpoint solves:
    #   [backend.roles.solver]  kind = "openai_compat", base_url = "...", model = "...", api_key_env = "..."
    roles: dict[str, dict[str, Any]] = field(default_factory=dict)
    temperature: float = 0.7
    max_tokens: int = 8000
    timeout: float = 600


@dataclass
class FakeCfg:
    solver_skill: float = 0.85
    fault: str = ""
    fault_rate: float = 0.0


@dataclass
class SpecCfg:
    practice_areas: list[str] = field(default_factory=lambda: ["commercial_contracts", "mergers_acquisitions"])
    jurisdictions: list[str] = field(default_factory=lambda: ["Delaware", "New York"])
    work_types: list[str] = field(default_factory=lambda: ["issue_spotting_memo"])
    n_documents: list[int] = field(default_factory=lambda: [3, 5])  # inclusive range
    n_issues: list[int] = field(default_factory=lambda: [3, 5])


@dataclass
class GatesCfg:
    solver_attempts: int = 3
    solver_max_steps: int = 20  # tool calls per attempt before the solver must write its answer
    solver_page_chars: int = 6000  # read_file page size (~1,000 words)
    solver_min_pass_rate: float = 0.01  # below: nothing solves it, probably broken
    solver_max_pass_rate: float = 0.99  # above: too easy to teach anything
    probe_without_documents: bool = True
    judge_hints: bool = True  # send rubric hints to the judge (and export them); off to measure leniency
    verifier_sees_terms: bool = False  # terms are checked verbatim in code; the verifier judges blind
    decontam_ngram: int = 8
    decontam_threshold: float = 0.5
    decontam_bloom_bits: int = 2**27
    reference_dirs: list[str] = field(default_factory=list)
    decontam_cache_dir: str = "runs/.decontam_cache"  # saved reference index, reused while the files are unchanged
    decontam_group_depth: int = 0  # >0: wording shared by 2+ benchmark tasks is not a match (3 for LAB's layout)


@dataclass
class SplitsCfg:
    ratios: dict[str, float] = field(default_factory=lambda: {"train": 0.8, "dev": 0.1, "test": 0.1})
    salt: str = "ltg-v0"


@dataclass
class SourcesCfg:
    precedent_dirs: list[str] = field(default_factory=list)  # empty = bundled synthetic samples
    precedents_per_matter: int = 1
    precedent_chars: int = 6000


@dataclass
class Config:
    run: RunCfg = field(default_factory=RunCfg)
    backend: BackendCfg = field(default_factory=BackendCfg)
    fake: FakeCfg = field(default_factory=FakeCfg)
    spec: SpecCfg = field(default_factory=SpecCfg)
    gates: GatesCfg = field(default_factory=GatesCfg)
    splits: SplitsCfg = field(default_factory=SplitsCfg)
    sources: SourcesCfg = field(default_factory=SourcesCfg)


def _fill(cls, data: dict[str, Any]):
    known = {f.name for f in fields(cls)}
    unknown = set(data) - known
    if unknown:
        raise ValueError(f"unknown {cls.__name__} keys: {sorted(unknown)}")
    return cls(**data)


def load_config(path: str | None = None, overrides: dict[str, dict[str, Any]] | None = None) -> Config:
    raw: dict[str, Any] = {}
    if path:
        with open(path, "rb") as f:
            raw = tomllib.load(f)
    for section, values in (overrides or {}).items():
        raw.setdefault(section, {}).update(values)
    cfg = Config()
    for f in fields(Config):
        if f.name in raw:
            setattr(cfg, f.name, _fill(type(getattr(cfg, f.name)), raw.pop(f.name)))
    if raw:
        raise ValueError(f"unknown config sections: {sorted(raw)}")
    return cfg


ROLE_BACKEND_KEYS = {"kind", "base_url", "api_key_env", "model", "temperature", "max_tokens", "timeout"}


def build_client(cfg: Config, log: CallLog) -> ModelClient:
    default = _one_client(cfg, cfg.backend, log)
    if not cfg.backend.roles:
        return default
    routes = {}
    for role, over in cfg.backend.roles.items():
        unknown = set(over) - ROLE_BACKEND_KEYS
        if unknown:
            raise ValueError(f"backend.roles.{role}: unknown keys {sorted(unknown)}")
        fields_ = {k: v for k, v in over.items() if k != "model"}
        b = replace(cfg.backend, roles={}, models={}, **fields_, default_model=over.get("model", ""))
        routes[role] = _one_client(cfg, b, log)
    return RoleRouter(default, routes, log)


def _one_client(cfg: Config, b: BackendCfg, log: CallLog) -> ModelClient:
    if b.kind == "fake":
        from .fake import FakeModel

        return FakeModel(seed=cfg.run.seed, solver_skill=cfg.fake.solver_skill, fault=cfg.fake.fault, fault_rate=cfg.fake.fault_rate, log=log)
    if b.kind == "openai_compat":
        if not b.default_model:
            raise ValueError("backend.default_model is required for openai_compat")
        return OpenAICompatClient(
            base_url=b.base_url,
            default_model=b.default_model,
            api_key_env=b.api_key_env,
            models=b.models,
            temperature=b.temperature,
            max_tokens=b.max_tokens,
            timeout=b.timeout,
            log=log,
        )
    if b.kind == "claude_sdk":
        if not b.default_model:
            raise ValueError("backend.default_model is required for claude_sdk, e.g. \"sonnet\"")
        return ClaudeAgentClient(default_model=b.default_model, models=b.models, log=log)
    raise ValueError(f"unknown backend kind {b.kind!r}")
