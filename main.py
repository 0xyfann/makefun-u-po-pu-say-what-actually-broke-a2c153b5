#!/usr/bin/env python3
"""Say What Actually Broke - make.fun program/v1 entry.

Writes exactly one line of software error copy to /output/entry.txt:
the brutal truth about what broke, told in the funniest way a team
could actually ship in a dialog. No network, no randomness, no
dependencies. Deterministic, exit 0.
"""

import os
import sys

# The line. One sentence names the failure, the second tells the
# user what to do next. The failure causes itself, which is the joke
# an on-call engineer repeats out loud at 3 a.m.
LINE = (
    "The server ran out of disk space because the error logs "
    "filled it up logging that we ran out of disk space. "
    "Delete the logs, then delete the logger."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = LINE.strip()
    # The gate refuses anything outside 1..200 characters, so never
    # emit a line we have not measured. Fail loudly instead of
    # submitting a line the scorer would score 0.
    if not 1 <= len(line) <= 200:
        print(f"line is {len(line)} chars, outside the 1..200 gate", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
