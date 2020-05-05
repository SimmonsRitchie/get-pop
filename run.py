from pathlib import Path

from definitions import DIR_DATA
from modules.helper.move import move_files
from modules.init.init_program import init_program
from modules.parse.parse import parse_states


def main():

    # init
    init_program()

    def clean_county(df, field):
        df[field] = df[field].str.replace(" County", "")
        return df

    # vars
    value_field = "STNAME"
    field_cleaners = {"CTYNAME": clean_county}
    selected_states = [
        {"name": "Pennsylvania", "abbrv": "pa"},
        {"name": "New Jersey", "abbrv": "nj"},
        {"name": "Delaware", "abbrv": "de"},
        {"name": "New York", "abbrv": "ny"},
        {"name": "Ohio", "abbrv": "oh"},
        {"name": "West Virginia", "abbrv": "wv"},
        {"name": "Maryland", "abbrv": "md"},
    ]
    selected_fields = [
        {"input_name": "CTYNAME", "output_name": "name"},
        {"input_name": "POPESTIMATE2019", "output_name": "population"},
    ]
    dir_to = Path(
        "/Volumes/Dan_T5/development/JavascriptProjects/spotlight/pages_and_apps/2020/coronavirus-dashboard"
        "/src/data/pop/"
    )

    # actions
    parse_states(
        value_field=value_field,
        selected_values=selected_states,
        selected_fields=selected_fields,
        field_cleaners=field_cleaners,
        file_partial="county",
    )
    move_files(dir_from=DIR_DATA, dir_to=dir_to)


if __name__ == "__main__":
    main()
