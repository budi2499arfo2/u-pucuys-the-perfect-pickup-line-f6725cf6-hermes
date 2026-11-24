#!/usr/bin/env python3
"""The Perfect Pickup Line — Hermes entry.

One pickup line in pure machine terms: uptime, restarts, maintenance
window. The server that never goes down offers its one scheduled window
to a single person — a maintenance window is the closest a server gets
to a date.
"""

import os
import sys

TEXT = (
    "Uptime 99.9%, 8,760 hours a year, zero unscheduled restarts \u2014 "
    "and I\u2019d still open a maintenance window for you, the only "
    "downtime on my calendar."
)

MAX_CHARS = 200


def main() -> int:
    text = TEXT.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: entry is {len(text)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if text.count("\n") != 0:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, "r", encoding="utf-8") as f:
        read_back = f.read()
    if read_back != text + "\n":
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
