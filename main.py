#!/usr/bin/env python3
"""The One-Liner Groan-Off: write one original dad joke to entry.txt.

The gate requires UTF-8 text of 1 to 140 characters, not only whitespace.
This program self-checks the line before writing so a bad line can never
reach the gate: it asserts the length and content, then writes exactly
one line with no trailing newline.
"""

import os
import sys

# Original one-line dad joke: a vending machine, "change", and "small
# talk" (small coins / small conversation) collide in one fast twist.
JOKE = "I asked the vending machine for change \u2014 it said, \u201cSorry, I don't do small talk.\u201d"

MAX_CHARS = 140


def main():
    line = JOKE.strip()
    if not line:
        print("error: joke line is empty", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(f"error: joke is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        sys.exit(1)
    # Confirm it encodes cleanly as UTF-8 before writing.
    line.encode("utf-8")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8",
              newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
