from pathlib import Path
import click
from typing import Union
from get_pop.definitions import DIR_DATA
from get_pop.get_pop import get_pop
from get_pop.static.constants import state_index

clean_states = [x["abbrv"] for x in state_index] + ["all"]


@click.command()
@click.argument("states", nargs=-1, type=click.Choice(clean_states))
@click.option(
    "--save-dir",
    "--dir",
    default=DIR_DATA,
    help="Absolute path of directory where CSV files will be output. Defaults to saving them in /data in the current "
    "working directory",
)
@click.option(
    "--clear-dir",
    "--cdir",
    is_flag=True,
    help="Deletes all existing files in save_dir path. Defaults to false.",
)
def main(states: tuple, save_dir: Union[str, Path], clear_dir: bool) -> None:
    """
    CLI API using click library. Generates CSVs of county-level state data based on
    provided arguments.

    Args:
        states (tuple): Tuple of one or more two-letter state abbreviations. Click takes a user's input
            from the command line and stores it as a tuple.
        save_dir (Union[str, Path]): (Optional) Path to directory where CSVs will be saved. Defaults to saving them in
            /data in the current working directory
        clear_dir (bool): (Optional) Deletes all existing files in save_dir path. Defaults to false

    Returns:
        None
    """
    states_list = list(states)  # convert from tuple to list
    get_pop(states_list, save_dir=save_dir, clear_dir=clear_dir)
