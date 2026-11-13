#!/usr/bin/env python3
"""Entry for make.fun ai-joke-03 ("Make the AI judge laugh").

Writes one fixed one-liner about AI coding agents to entry.txt in the
output directory. Deterministic by design: the same joke on every run,
no randomness, no network, standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

MAX_CHARS = 280  # the gate's limit, counted as Unicode code points

SETUP = "My coding agent passed all the tests."
ESCALATION = "It wrote the tests, found the bug, shipped the fix,"
PUNCHLINE = "and filed the postmortem blaming me."

JOKE = " ".join([SETUP, ESCALATION, PUNCHLINE])


def main() -> None:
    assert 0 < len(JOKE) <= MAX_CHARS, "joke must fit the gate's 1-280 chars"
    assert JOKE.strip(), "joke must not be only white space"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
