def clean_county(df, field):
    df[field] = df[field].str.replace(" County", "")
    return df


def merge_nyc_boroughs(df):
    """
    Combines the five buroughs to create NYC row
    """
    df_buroughs = df.loc[
        df["name"].isin(["Bronx", "Queens", "New York", "Kings", "Richmond"])
    ]
    nyc_pop = df_buroughs["population"].sum()
    return df.append(
        {"name": "New York City", "population": nyc_pop}, ignore_index=True
    )
