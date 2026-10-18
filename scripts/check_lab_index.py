"""Sanity check for the LAB decontamination index. Run from the repo root after `ltg index`:

    .venv/bin/python scripts/check_lab_index.py

It should show LAB's own text matching (excerpts near 1.0) and our accepted tasks well below the 0.5 cutoff.
Before per-task grouping (decontam_group_depth = 3), our sound documents scored up to 0.56 on shared boilerplate.
"""

import glob
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ltg.config import load_config  # noqa: E402
from ltg.decontam import _read_text  # noqa: E402
from ltg.orchestrator import reference_index  # noqa: E402

config = sys.argv[1] if len(sys.argv) > 1 else "configs/pilot_nrp_solver.toml"
g = load_config(config).gates
t = time.time()
idx = reference_index(g)
if idx.common is None:
    sys.exit("the index is not grouped by task: set gates.decontam_group_depth (3 for LAB)")
print(f"index loaded in {time.time() - t:.0f} s, {idx.count:,} n-grams")

random.seed(0)
lab = [p for p in (Path(g.reference_dirs[0]) / "tasks").rglob("*") if p.suffix.lower() in {".docx", ".eml", ".json"}]
print("LAB excerpts, 400 words each (should be near 1.0):")
shown = 0
for p in random.sample(lab, min(40, len(lab))):
    w = _read_text(p).split()
    if len(w) > 450:
        print(f"  {p.suffix:5} {idx.containment(' '.join(w[50:450])):.3f}")
        shown += 1
    if shown == 6:
        break

print(f"our accepted tasks (cutoff {g.decontam_threshold}):")
for m in sorted(glob.glob("runs/cloud_pilot_r*/accepted/*")):
    texts = {"instruction": Path(m, "instruction.md").read_text(), "gold": json.loads(Path(m, "answers.json").read_text())["gold"]}
    texts.update({d.name: d.read_text() for d in Path(m, "docs").glob("*.md")})
    scores = {k: idx.containment(v) for k, v in texts.items()}
    top = max(scores, key=scores.get)
    print(f"  {Path(m).name}: highest {scores[top]:.3f} ({top})")
