"""Entry for make.fun bounty: Your AI Therapist's Diagnosis.

Writes a single funny one-line diagnosis an AI therapist gives its
human to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.

Python 3.13, standard library only, deterministic, no network.
"""

import os

ENTRY = (
    "Diagnosis: chronic prompt dependency \u2014 patient asks an AI "
    "how to feel, then argues with the answer."
)


def main() -> None:
    # The bounty gate requires 1-200 characters of UTF-8 text.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
