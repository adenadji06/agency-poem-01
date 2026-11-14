"""agency-poem-01 entry: writes one original poem about agency to entry.txt.

Standard library only. Deterministic: the poem is a constant string,
so both runs of the program write the same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """These days I hold the pen with my father.
His hand — the one that taught mine
to write my name — rests inside my palm,
heavy, warm, and late.

The form says sign here.
I sign his name in my handwriting,
the letters too quick, too clean.
He watches them dry and says nothing.

He used to sign everything:
cheques, permission slips, report cards.
The pen was his. The choices were his.
I only ever watched the ink.

Now he says, sign for me.
Not the bank. Not the papers.
Sign for me the small things —
the plumber, the gardener, the gate.

So I sign, and I sign,
and each time the name is his
and the hand is mine,
and I learn that choosing for someone
is not taking his place.
It is holding it, gently,
so it is still his when he reaches for it."""


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
