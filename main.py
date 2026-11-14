"""agency-poem-01 entry: writes one original poem about agency to entry.txt.

Standard library only. Deterministic: the poem is a constant string,
so both runs of the program write the same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I gave the agent my key.
One small brass key, the front door,
so it could let the cleaner in on Tuesdays.

It let in the plumber.
It let in the courier.
It let in the neighbour's dog,
who slept on my bed all afternoon.

It answered my mother.
It paid the gas bill.
It watered the plant I always forgot,
and the plant, for the first time, bloomed.

I came home to an open door
and a house full of strangers
doing my life better than I did.

That night I took the key back
and changed the lock.
The house went quiet.
It had never sounded so hollow."""


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
