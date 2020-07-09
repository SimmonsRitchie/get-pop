import logging
from dotenv import load_dotenv
from get_pop.definitions import DIR_DATA
from get_pop.logs.config.logging import logs_config
from get_pop.modules.helper.misc import delete_dir_contents
from get_pop.modules.helper.time import utc_now
from get_pop.modules.init.pandas_opts import pandas_opts


def init_program(package_name: str = None):
    """
    Initializes program, inits logging, performs filesystem clean up, etc.

    Args:
        package_name (str): (optional) name of package
    """

    # Load env vars
    load_dotenv()

    # init logging
    program_start_time = utc_now()
    timezone = program_start_time.tzinfo
    logs_config()
    if package_name:
        logging.info(f"Initializing {package_name}")

    # create or clean download dir
    if DIR_DATA.is_dir():
        # delete files from previous run
        delete_dir_contents(DIR_DATA)
    else:
        logging.info("Data directory doesn't exist - building")
        DIR_DATA.mkdir()

    pandas_opts()

    return program_start_time
