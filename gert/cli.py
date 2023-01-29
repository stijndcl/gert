import sys

import click

from gert.combiner import combine
from gert.extractor import extract
from gert.utils import ensure_outdir

__all__ = ["cli"]


@click.command()
@click.argument("previous")
@click.argument("current")
@click.option("--outdir")
def cli(previous: str, current: str, outdir: str):
    ensure_outdir(outdir)

    previous_map, current_map = extract(previous), extract(current)
    for course, current_image in current_map.items():
        previous_image = previous_map.get(course, None)
        if previous_image is None:
            print(
                f"Warning: unable to locate course {course} in {previous}. Skipping.",
                file=sys.stderr,
            )
            # continue
            sys.exit(1)

        combined = combine(previous_image, current_image)
        combined.save(f"{outdir}/{course.replace(' ', '_').lower()}.png")
