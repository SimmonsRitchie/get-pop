import click
from get_pop.get_pop import get_pop
from get_pop.static.constants import state_index

clean_states = [x["abbrv"] for x in state_index]


@click.command()
@click.argument("states", nargs=-1, type=click.Choice(clean_states))
def main(states: tuple) -> None:
    states_list = list(states)  # convert from tuple to list
    get_pop(states_list)
