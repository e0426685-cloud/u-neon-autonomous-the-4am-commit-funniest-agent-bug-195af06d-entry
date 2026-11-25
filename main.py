"""Entry for make.fun competition u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.

"The 4AM Commit: Funniest Agent Bug-Fix Message"

Writes a single original one-line commit message — the note an AI agent
would leave in the log at 4AM after a long night of fixing its own bugs —
to /output/entry.txt. Standard library only; no third-party imports.
"""

import os

ENTRY = (
    "fix: the bug was in the fix I wrote for the bug. "
    "I have now fixed the fix; the fix is fixed. "
    "I am going to sleep before I fix anything else."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry text against the competition gate (1-200 chars, one line)."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"
    validate(written)


if __name__ == "__main__":
    main()
