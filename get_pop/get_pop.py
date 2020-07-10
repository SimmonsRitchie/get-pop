from get_pop.modules.init.init_program import init_program
from get_pop.modules.parse.parse import parse_states
import click
import logging
from get_pop.static.constants import (
    state_index,
    value_field,
    selected_fields,
    field_cleaners,
)

clean_states = [x["abbrv"] for x in state_index]


def get_pop(states: tuple) -> None:

    # init
    package_name = "getpop"
    init_program(package_name)

    # process states
    states = list(states)
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
    )

    # end
    logging.info(f"{package_name} complete")
