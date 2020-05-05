from pathlib import Path
from shutil import copyfile
import logging


def move_files(dir_from: Path, dir_to: Path):
    logging.info(f"Moving files from '{dir_from}' to '{dir_to}'")
    p = dir_from.glob("**/*")
    input_paths = [x for x in p if x.is_file()]
    for input_path in input_paths:
        filename = input_path.name
        output_path = dir_to / filename
        copyfile(input_path, output_path)
        logging.info(f"Moved file: {filename}")
