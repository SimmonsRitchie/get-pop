import logging
from typing import List, Union

from get_pop.modules.helper.misc import check_and_clear_dir
from get_pop.static.constants import (
    state_index,
    value_field,
    field_cleaners,
    default_fields,
)
import pathlib
from get_pop.definitions import selected_fields_type
from get_pop.definitions import DIR_DATA
from get_pop.modules.init.init_program import init_program
from get_pop.modules.parse.parse import parse_states

clean_states = [x["abbrv"] for x in state_index]


def get_pop(
    states: List[str],
    *,
    save_dir: Union[pathlib.Path, str] = DIR_DATA,
    clear_dir: bool = False,
    selected_fields: selected_fields_type = default_fields,
) -> None:
    """
    Takes a list of 2-letter US state postal codes, returns CSVs for each state.

    Args:
        states List[str]: List of states.
        save_dir Union[pathlib.Path, str]: (Optional) Absolute path where CSV data will be stored. Defaults to /data
            in current working directory.
        clear_dir (bool):
        selected_fields (selected_fields_type): (Optional) A list of dictionaries with fields that should be
            included in the final CSV for each state. Default fields: "fips", "name", "population"

    Returns:
        None.
    """

    # init
    package_name = "getpop"
    init_program(package_name)

    # process states
    logging.info(f"Selected states: {states}")
    selected_states = []
    if "all" in states[0]:
        selected_states = state_index
    else:
        for state in states:
            index_item = [
                x for x in state_index if x["abbrv"].lower() in state.lower()
            ][0]
            selected_states.append(index_item)

    # clear directory flag
    if clear_dir:
        check_and_clear_dir(save_dir)

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
