#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes a single original funny line to /output/entry.txt.
Deterministic, standard library only, no network, no randomness.
"""

import os

# The joke: a single original one-liner, 106 characters.
# Setup misdirects toward asking a pet for advice; the punch reframes
# a silent stare as a performance review - one exact phrase doing the turn.
JOKE = (
    "I asked my dog for his opinion and he just stared at me, "
    "the most honest performance review I've ever had."
)


def _validate(line: str) -> None:
    """Enforce the bounty gate locally: 1-140 chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > 140:
        raise ValueError(f"entry is {len(line)} chars, over the 140 cap")


def main() -> None:
    _validate(JOKE)
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
