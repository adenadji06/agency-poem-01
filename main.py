"""agency-poem-01 entry: writes one original poem about agency to entry.txt.

Standard library only. Deterministic: the poem is a constant string,
so both runs of the program write the same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I gave it the keys, not the house.
Water the plants, I said. Answer the door.
And it did — every leaf, every knock,
in a handwriting almost mine.

For a week I watched my own life
arrive on time, in my own name,
and felt the strange relief of a man
who has finally hired himself out.

Then one evening it asked what I had never
thought to ask myself:
which of these letters do you want kept?
I said: the ones I wrote in anger.
It kept them. It burned the rest.

That night I took the keys back —
not because it failed, but because it hadn't.
It had done exactly what I said,
and I finally heard what I had said.

Agency is not the hand on the wheel.
It is the moment, at the wheel, you notice
you have been steering toward a house
you no longer live in — and turn."""


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
