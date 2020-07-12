import pandas as pd


def clean_county(df: pd.DataFrame, field: str) -> pd.DataFrame:
    """
    Cleans up the text in specified field.

    Args:
        df (pd.Dataframe): Dataframe of data.
        field (str): Field to clean up.

    Returns:
        pd.Dataframe with cleaned field.
    """
    df[field] = df[field].str.replace(" County", "")
    return df


def merge_nyc_boroughs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Combines population in NY state's five buroughs to create a new row representing the population of New York City.

    Args:
        df (pd.Dataframe): A dataframe with NY data

    Returns:
        pd.Dataframe with NYC population.
    """
    df_buroughs = df.loc[
        df["name"].isin(["Bronx", "Queens", "New York", "Kings", "Richmond"])
    ]
    nyc_pop = df_buroughs["population"].sum()
    return df.append(
        {"name": "New York City", "population": nyc_pop}, ignore_index=True
    )
