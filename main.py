#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes one line (<=120 chars) to /output/entry.txt: the error message
a kitchen toaster shows its owner when something goes wrong.
"""

import os

ENTRY = "ERROR 07: This is the third time today. I am a toaster, not a coping mechanism. Please seek help."


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, must be 1-120"
    assert "\n" not in line and line.strip() == line, "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Read back and confirm exactly what the judge will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read().rstrip("\n") == line
    print(line)


if __name__ == "__main__":
    main()
