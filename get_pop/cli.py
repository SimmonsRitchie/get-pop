import click
from get_pop.get_pop import get_pop
from get_pop.static.constants import state_index

clean_states = [x["abbrv"] for x in state_index] + ["all"]


@click.command()
@click.argument("states", nargs=-1, type=click.Choice(clean_states))
def main(states: tuple) -> None:
    """
    CLI API using click library. Generates CSVs of county-level state data based on
    provided arguments.

    Args:
        states (tuple): Tuple of one or more two-letter state abbreviations. Click takes a user's input
         from the command line and stores it as a tuple.

    Returns:
        None
    """
    states_list = list(states)  # convert from tuple to list
    get_pop(states_list)
