import json

import pytest

from ltg.config import load_config
from ltg.fake import FakeModel
from ltg.models import extract_input


class RecordingFake(FakeModel):
    """FakeModel that also keeps every payload it was sent, keyed by role."""

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.payloads: dict[str, list[dict]] = {}

    def complete(self, role, system, user):
        self.payloads.setdefault(role, []).append(extract_input(user))
        return super().complete(role, system, user)


@pytest.fixture
def cfg(tmp_path):
    return load_config(None, {"run": {"out_dir": str(tmp_path / "run"), "n_matters": 6, "seed": 7}})


@pytest.fixture
def read_json():
    return lambda p: json.loads(p.read_text())
