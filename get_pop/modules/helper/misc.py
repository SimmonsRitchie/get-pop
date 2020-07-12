import os
import shutil
from typing import Union
from pathlib import Path
import logging


def check_and_clear_dir(dir_path: Union[str, Path]) -> None:
    """
    Checks if directory exists, if it does then delete contents of directory but keeps directory.

    Args:
        dir_path (str, pathlib.Path): Absolute path of directory to target.

    Returns:
        None
    """
    # create or clean download dir
    if isinstance(dir_path, str):
        dir_path = Path(dir_path)
    if dir_path.is_dir():
        # delete files from previous run
        delete_dir_contents(dir_path)
    else:
        logging.info(f"Path {dir_path} is not a directory and can't be cleared")


def delete_dir_contents(dir_path: Union[str, Path]) -> None:
    """
    Deletes all files and folders within a directory.

    Args:
        dir_path (str, Path): Absolute path of directory to target.
    """
    if isinstance(dir_path, str):
        dir_path = Path(dir_path)

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))
