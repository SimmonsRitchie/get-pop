import logging
from get_pop.definitions import parsed_data_type
from pathlib import Path
from typing import Union


def save_csv(
    parsed_data: parsed_data_type, save_dir: Union[Path, str], *, file_partial: str
) -> None:
    """
    Saves a list of dictionaries containing pd.Dataframes as individual CSVs

    Args:
        parsed_data (parsed_data_type): List of dicts with data to save.
        save_dir: Union[pathlib.Path, str]: Path where processed state CSVs will be saved
        file_partial (str): (Optional) String that is used to determine part of final CSV filename for each state.

    Returns:
        None. CSVs are saved.
    """
    logging.info(f"CSVs will be saved in: {save_dir}")
    for item in parsed_data:
        name = item["name"]
        data = item["data"]
        filename = (
            f"{name}-{file_partial}-pop.csv" if file_partial else f"{name}-pop.csv"
        )
        save_dir = Path(save_dir) if isinstance(save_dir, str) else save_dir
        save_dir.mkdir(exist_ok=True)
        output_path = save_dir / filename
        data.to_csv(output_path, index=False)
