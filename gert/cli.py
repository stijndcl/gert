import click

from gert.extractor import extract

__all__ = ["cli"]


@click.command()
@click.argument("previous")
@click.argument("current")
@click.option("--outdir")
def cli(previous: str, current: str, outdir: str):
    previous_map, current_map = extract(previous), extract(current)
