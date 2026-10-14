import pytest

from ltg.models import ModelError, call_json, parse_json


@pytest.mark.parametrize(
    "text",
    [
        '{"a": 1}',
        'Sure! Here it is:\n```json\n{"a": 1}\n```',
        'Result: {"a": 1} hope that helps',
        '{"a": 1, "s": "brace } inside a string"}',
    ],
)
def test_parse_json_tolerates_wrapping(text):
    assert parse_json(text)["a"] == 1


def test_parse_json_rejects_garbage():
    with pytest.raises(ValueError):
        parse_json("no json here")


class Flaky:
    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.prompts = []

    def complete(self, role, system, user):
        self.prompts.append(user)
        return self.outputs.pop(0)


def test_call_json_retries_once_with_reminder():
    client = Flaky(["oops not json", '{"ok": true}'])
    assert call_json(client, "x", "sys", "user") == {"ok": True}
    assert "ONLY the JSON object" in client.prompts[1]


def test_call_json_gives_up():
    with pytest.raises(ModelError):
        call_json(Flaky(["bad", "still bad"]), "x", "sys", "user")
