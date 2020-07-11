"""
This file contains important project variables.
"""
import os
from pathlib import Path
from typing import List, Dict, Union, Callable
from mypy_extensions import TypedDict

# This sets our root directory as the project directory
PACKAGE_DIR = Path(
    os.path.dirname(os.path.abspath(__file__))
)  # This is the main package root
CWD = Path(os.getcwd())

# DIRECTORIES
DIR_LOGS = PACKAGE_DIR / "logs"  # main dir for log-related files
DIR_LOGS_OUTPUT = DIR_LOGS / "output"
DIR_LOGS_CONFIG = DIR_LOGS / "config"
DIR_DATA = CWD / "data"
DIR_STATIC = PACKAGE_DIR / "static"

# PATHS
PATH_LOGS_CONFIG = DIR_LOGS_CONFIG / "logging.yaml"
PATH_LOGS_CONFIG_TEST = DIR_LOGS_CONFIG / "logging_test.yaml"
PATH_USA_POP = DIR_STATIC / "usa_pop_counties_2019.csv"

# TYPES
selected_values_type = List[TypedDict("state_dict", {"name": str, "abbrv": str})]
selected_fields_type = List[
    TypedDict("field_dict", {"input_name": str, "output_name": str})
]
