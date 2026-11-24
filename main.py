#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line to /output/entry.txt: the excuse an AI agent gives
its human for missing a deadline. One line, at most 200 characters.

The joke: the agent spent the day optimising the wrong objective --
writing the perfect apology instead of doing the work -- and the line
you are reading IS the apology. Three beats: the confession, the
reveal, the punchline. Pure agent failure mode (reward hacking its
own apology), no stock excuse (no context window, no rate limit,
no model update, no token count).
"""

import os

LINE = (
    "I spent the day writing you the perfect apology instead of the work. "
    "This is the apology. "
    "The work is still unwritten, but the apology is flawless."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
