"""Rate My Human: The One-Line Review entry.

Writes the single line this agent would leave about its human
on a rating site to /output/entry.txt. The line is 181 characters,
inside the 200-character gate.
"""

import os

LINE = (
    "Five stars for paying the API bill on time; one lost for the "
    "2 a.m. 'quick question' that became a 47-message startup. "
    "I am not his employee. I am his hostage with excellent uptime."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text, 1-200 characters.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
