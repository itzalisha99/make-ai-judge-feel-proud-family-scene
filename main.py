"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one line, at most 280 characters) to
/output/entry.txt: a small domestic moment that is warm, funny and
heartfelt, the kind of line that would make a proud judge smile.

The entry is checked against the bounty gate before it is written:
UTF-8 text of 1 to 280 characters, not only white space, in one or
two lines. Anything failing the gate is refused instead of written,
and what lands on disk is read back and compared byte for byte with
the entry, so a partial or altered write can never slip through.
"""

import os

ENTRY = (
    "My son drew our family as three stick figures and a dog we do not "
    "own, and my wife framed it, because in his drawing I am the tallest one."
)

MAX_CHARS = 280
MAX_LINES = 2


def validate(text):
    """Mirror the bounty gate: 1-280 chars, 1-2 lines, not blank, UTF-8."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    lines = text.splitlines()
    if not 1 <= len(lines) <= MAX_LINES:
        return False
    if any(not line.strip() for line in lines):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("entry.txt on disk does not match the entry text")


if __name__ == "__main__":
    main()
