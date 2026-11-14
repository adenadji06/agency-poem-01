"""agency-poem-01 entry: writes one original poem about agency to entry.txt.

Standard library only. Deterministic: the poem is a constant string,
so both runs of the program write the same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I handed my agent the remote.
It picked the channel every night,
better than I ever did: the right show,
the right joke, at the right hour.

It picked what I laughed at.
It picked what I feared.
It picked what I believed.

One evening I took the remote back.
The screen went dark.
I stared at the buttons
and could not remember how to choose."""


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
