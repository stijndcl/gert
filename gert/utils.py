import os
import pathlib
import sys

__all__ = ["ensure_outdir"]


def ensure_outdir(outdir: str):
    """Make sure that a directory exists, otherwise create it"""
    path = pathlib.Path(outdir)
    if path.exists() and not path.is_dir():
        print(f"Path {outdir} exists and is not a directory.", file=sys.stderr)
        sys.exit(1)

    if not path.exists():
        os.mkdir(path)
