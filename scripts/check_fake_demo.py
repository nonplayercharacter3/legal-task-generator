"""Fail unless the fake demo still rejects at every quality gate it used to. CI runs it after the demo:

    python -m ltg run --config configs/fake_demo.toml --out /tmp/fake_demo
    python scripts/check_fake_demo.py /tmp/fake_demo/report.json

The demo injects one fault per gate into ~35% of matters ("How to verify changes" in CLAUDE.md); a gate that stops
rejecting its fault has gone blind.
"""

import json
import sys

GATES = ("consistency", "issue_check", "leak_check", "rubric_trace", "rubric_tests")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: check_fake_demo.py <report.json>", file=sys.stderr)
        return 2
    gates = json.load(open(argv[0]))["gates"]
    blind = [g for g in GATES if gates.get(g, {}).get("failed", 0) < 1]
    for g in GATES:
        print(f"{g:<14} rejected {gates.get(g, {}).get('failed', 0)}")
    if blind:
        print(f"FAIL: the fake demo rejected nothing at {', '.join(blind)}", file=sys.stderr)
        return 1
    print("ok: the fake demo rejects at every quality gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
