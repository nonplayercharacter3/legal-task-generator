"""Split assignment by matter, so tasks built from one matter never straddle train and test."""

from __future__ import annotations

import hashlib


def assign_split(matter_id: str, ratios: dict[str, float], salt: str = "ltg-v0") -> str:
    total = sum(ratios.values())
    if total <= 0:
        raise ValueError("split ratios must sum to a positive number")
    h = int(hashlib.sha256(f"{salt}:{matter_id}".encode()).hexdigest()[:12], 16) / 16**12
    acc = 0.0
    for name, r in ratios.items():
        acc += r / total
        if h < acc:
            return name
    return list(ratios)[-1]
