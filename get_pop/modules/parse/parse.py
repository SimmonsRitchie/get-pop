import pandas as pd
from typing import Dict, Callable
from get_pop.definitions import PATH_USA_POP, parsed_data_type
import logging
import pathlib
from get_pop.definitions import selected_fields_type, selected_values_type


def parse_states(
    value_field: str,
    selected_values: selected_values_type,
    selected_fields: selected_fields_type,
    *,
    field_cleaners: Dict[str, Callable[[pd.DataFrame, str], pd.DataFrame]] = None,
) -> parsed_data_type:
    """
    Outputs CSVs of state data after parsing a large CSV of U.S. county-level census data for selected states.

    Args:
        value_field (str): Field that will be used to filter data by.
        selected_values (selected_values_type): A list of dictionaries relating to the state's selected for data
            extraction. Each dict has a key-value pairs for the full name of the state and it's two-letter abbreviation.
        selected_fields (selected_fields_type): A list of dictionaries that represent the fields that will be selected from
            the U.S. Census CSV, and how the field will be represented in the final CSV.
        field_cleaners (Dict[Callable[[pd.DataFrame, str], pd.DataFrame]]): (Optional) function that cleans a
            specified field

    Returns:
        parsed_data_type - A list of dictionaries with parsed data
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

    payload = []
    for name, group in by_state:
        logging.info(f"Processing: {name}")

        # get selected state dict for processing instructions
        selected_state = list(filter(lambda x: x["name"] == name, selected_values))[0]

        # generate FIPS code
        # Temporarily disabling SettingWithCopy warning
        pd.reset_option("mode.chained_assignment")
        with pd.option_context("mode.chained_assignment", None):
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
        payload.append({"name": abbrv, "data": group})

    return payload
