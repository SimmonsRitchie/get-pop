import pandas as pd


def pandas_opts() -> None:
    """
    Sets desired pandas options.

    Returns:
        None
    """
    pd.set_option("display.max_columns", 20)
    pd.set_option("display.width", 2000)
    pd.set_option("display.max_rows", 2000)
