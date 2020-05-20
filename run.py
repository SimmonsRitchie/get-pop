from modules.init.init_program import init_program
from modules.parse.helpers import clean_county, merge_nyc_boroughs
from modules.parse.parse import parse_states


def main():

    # init
    init_program()

    # vars
    value_field = "STNAME"
    field_cleaners = {"CTYNAME": clean_county}
    selected_states = [
        {"name": "Pennsylvania", "abbrv": "pa"},
        {"name": "New Jersey", "abbrv": "nj"},
        {"name": "Delaware", "abbrv": "de"},
        {"name": "New York", "abbrv": "ny", "special_processors": [merge_nyc_boroughs]},
        {"name": "Ohio", "abbrv": "oh"},
        {"name": "West Virginia", "abbrv": "wv"},
        {"name": "Maryland", "abbrv": "md"},
    ]
    selected_fields = [
        {"input_name": "CTYNAME", "output_name": "name"},
        {"input_name": "POPESTIMATE2019", "output_name": "population"},
    ]

    # actions
    parse_states(
        value_field=value_field,
        selected_values=selected_states,
        selected_fields=selected_fields,
        field_cleaners=field_cleaners,
        file_partial="county",
    )


if __name__ == "__main__":
    main()
