#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single-line joke about office life (at most 200 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3 standard library only. Output is fully deterministic: the
same fixed string is written on every run, with no trailing newline,
so the file is exactly the joke text and nothing else.
"""

import os
import sys

JOKE = (
    "Our office plant has survived three rounds of layoffs, two CEOs, "
    "and a merger \u2014 HR just gave it a promotion and my desk."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
