#!/usr/bin/env python3
"""news-image-20261124 entry runner.

Copies the pre-rendered front page (entry.png, bundled in the repo) to
the output directory the harness provides. Standard library only.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
TARGET_NAME = "entry.png"


def resolve_output_dir() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"missing bundled image: {source}", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    # The harness mounts /output writable; never delete or recreate it.
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME
    shutil.copyfile(source, target)
    size = target.stat().st_size
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
