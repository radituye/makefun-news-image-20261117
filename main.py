#!/usr/bin/env python3
"""Entry for the make.fun bounty news-image-20261117: "Sum up 17 November's
world news in one image".

The entry's image is the file image.png beside this program: a front page
that sums up Tuesday 17 November 2026. The lead story is the Ukrainian
strike that collapsed a road span of the Kerch Bridge to Crimea, with
Russia answering by striking Kyiv's bridges. Around it: Trump's arrival
in Manila for his Asia trip ahead of trilateral talks with Xi Jinping
and Vladimir Putin, two tankers hitting mines in the Strait of Hormuz as
a third US carrier reaches the region, the Vulcan rocket failure that
destroyed 40 Amazon satellites, and the JPMorgan outage blamed on a
software bug. The footer adds the Pentagon's ninth failed audit, Nvidia
reporting after Huang's exit, Estonia's plan to shut its Russia border,
Japan scrambling jets, and five EU states' Rwanda migrant hub plan.

The program copies image.png, byte for byte, to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png outside the grader), so two runs always
write the same bytes. It uses only the standard library and needs no
network.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "image.png"
    if not source.is_file():
        print("image.png missing beside main.py", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)
    if dest.stat().st_size != source.stat().st_size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
