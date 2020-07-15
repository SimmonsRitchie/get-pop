import logging
from dotenv import load_dotenv
from get_pop.logs.config.logging import logs_config
from get_pop.modules.helper.time import utc_now
from get_pop.modules.init.pandas_opts import pandas_opts
from datetime import datetime


def init_program(package_name: str = None) -> datetime:
    """
    Initializes program, inits logging, performs filesystem clean up, etc.

    Args:
        package_name (str): (optional) name of package

    Returns:
        A datetime object with the time the program started.
    """

    # Load env vars
    load_dotenv()

    # init logging
    program_start_time = utc_now()
    logs_config()
    if package_name:
        logging.info(f"Initializing {package_name}")

    pandas_opts()

    return program_start_time
