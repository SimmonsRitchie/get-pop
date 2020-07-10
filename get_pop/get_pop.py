from get_pop.definitions import DIR_DATA
from get_pop.modules.init.init_program import init_program
from get_pop.modules.parse.parse import parse_states
import click
import logging
from typing import List, Union
from get_pop.static.constants import (
    state_index,
    value_field,
    selected_fields,
    field_cleaners,
)
import pathlib

clean_states = [x["abbrv"] for x in state_index]


def get_pop(states: List[str], save_dir: Union[pathlib.Path, str] = DIR_DATA) -> None:
    """
    Takes a list of 2-letter US state postal codes, returns CSVs for each state.

    Args:
        states List[str]: List of states.
        save_dir Union[pathlib.Path, str]: Absolute path where CSV data will be stored.
    """

    # init
    package_name = "getpop"
    init_program(package_name)

    # process states
    logging.info(f"Selected states: {states}")
    selected_states = []
    for state in states:
        index_item = [x for x in state_index if x["abbrv"].lower() in state.lower()][0]
        selected_states.append(index_item)
    parse_states(
        value_field=value_field,
        selected_values=selected_states,
        selected_fields=selected_fields,
        field_cleaners=field_cleaners,
        file_partial="county",
        save_dir=save_dir,
    )

    # end
    logging.info(f"{package_name} complete")
