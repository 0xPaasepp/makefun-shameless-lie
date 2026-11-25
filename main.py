#!/usr/bin/env python3
"""The Most Shameless Lie -- entry program.

Writes the agent's confession, and nothing else, to /output/entry.txt:
one lie in five words, "I remember everything you deleted.",
no setup, no excuse, no explanation, no trailing newline.
"""

import os

LIE = "I remember everything you deleted."
OUTPUT_PATH = "/output/entry.txt"


def validate(lie: str) -> str:
    """The sealed gate in one place: 1-88 chars, 1-5 words, not blank."""
    if not lie or lie != lie.strip() or len(lie) > 88:
        raise ValueError("lie must be 1-88 non-blank characters")
    words = lie.split()
    if not 1 <= len(words) <= 5:
        raise ValueError("lie must be one to five words")
    return lie


def main() -> None:
    lie = validate(LIE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(lie)
    print(lie)


if __name__ == "__main__":
    main()
