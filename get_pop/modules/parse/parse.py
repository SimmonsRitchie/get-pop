import pandas as pd
from typing import List, Dict, Union, Callable
from get_pop.definitions import PATH_USA_POP, DIR_DATA
import logging
import pathlib
from mypy_extensions import TypedDict


selected_values_type = List[TypedDict("state_dict", {"name": str, "abbrv": str})]
selected_fields_type = List[
    TypedDict("field_dict", {"input_name": str, "output_name": str})
]


def parse_states(
    value_field: str,
    selected_values: selected_values_type,
    selected_fields: selected_fields_type,
    save_dir: Union[pathlib.Path, str],
    *,
    field_cleaners: Dict[str, Callable[[pd.DataFrame, str], pd.DataFrame]] = None,
    file_partial: str = None,
) -> None:
    """
    Outputs CSVs of state data after parsing a large CSV of U.S. county-level census data for selected states.

    Args:
        value_field (str): Field that will be used to filter data by.
        selected_values (selected_values_type): A list of dictionaries relating to the state's selected for data
            extraction. Each dict has a key-value pairs for the full name of the state and it's two-letter abbreviation.
        selected_fields (selected_fields_type): A list of dictionaries that represent the fields that will be selected from
            the U.S. Census CSV, and how the field will be represented in the final CSV.
        save_dir: Union[pathlib.Path, str]: Path where processed state CSVs will be saved
        field_cleaners (Dict[Callable[[pd.DataFrame, str], pd.DataFrame]]): (Optional) function that cleans a
            specified field
        file_partial (str): (Optional) String that is used to determine part of final CSV filename for each state.

    Returns:
        None. Output is saved as CSV files.
    """

    # read
    df = pd.read_csv(PATH_USA_POP, encoding="ISO-8859-1")

    # filter - remove statewide population counts
    df = df[df["COUNTY"] != 0]

    # filter - include only selected values
    selected_values_names = [x["name"] for x in selected_values]
    df = df[df[value_field].isin(selected_values_names)]

    # option - clean value field
    if field_cleaners:
        for field in field_cleaners.keys():
            cleaner_func = field_cleaners[field]
            df = cleaner_func(df, field)

    # rename field lookuptable
    rename_schema = {}
    for field in selected_fields:
        input_name = field["input_name"]
        output_name = field["output_name"]
        rename_schema[input_name] = output_name

    # group by
    by_state = df.groupby(value_field)

    for name, group in by_state:
        logging.info(f"Processing: {name}")

        # get selected state dict for processing instructions
        selected_state = list(filter(lambda x: x["name"] == name, selected_values))[0]

        # generate FIPS code
        group["STATE"] = group["STATE"].astype(str).str.zfill(2)
        group["COUNTY"] = group["COUNTY"].astype(str).str.zfill(3)
        group["FIPS"] = group["STATE"] + group["COUNTY"]

        # truncate cols in df
        selected_fields_input = [x["input_name"] for x in selected_fields]
        group = group[selected_fields_input]

        # rename
        group = group.rename(columns=rename_schema)

        # option - special processor (special funcs for doing extra stuff to df)
        special_processors = selected_state.get("special_processors")
        if special_processors:
            for processor in special_processors:
                group = processor(group)

        # produce csv
        abbrv = selected_state["abbrv"]
        filename = (
            f"{abbrv}-{file_partial}-pop.csv" if file_partial else f"{abbrv}-pop.csv"
        )
        save_dir = pathlib.Path(save_dir) if isinstance(save_dir, str) else save_dir
        output_path = save_dir / filename
        group.to_csv(output_path, index=False)
