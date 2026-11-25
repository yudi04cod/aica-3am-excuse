#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
a hardware wallet gives for refusing to sign a transaction at 3 AM.
Deterministic, standard library only.
"""

import os
import sys

ENTRY = (
    "It's 3 AM. My seed phrase is asleep, dreaming in private keys, and "
    "I don't wake it for impulse buys - try me at sunrise, when your "
    "brain's back online."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
