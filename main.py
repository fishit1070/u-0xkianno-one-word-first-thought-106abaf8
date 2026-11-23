"""One Word, First Thought — entry program.

Writes exactly one word to entry.txt in the output directory.
The word: tittle — the tiny dot over the letters i and j.
Everyone has seen it ten thousand times; almost nobody knows it
has a name. That is the whole joke, and the whole point.
"""

import os

WORD = "tittle"  # the dot over i and j — the smallest named thing in print


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
