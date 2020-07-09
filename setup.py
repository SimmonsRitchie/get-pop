from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_pop",
    version="1.4",
    author="DSR",
    description="Command line tool to generates CSVs of population data for specified US states.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # list folders, not files
    package_dir={"get_pop": "get_pop"},
    packages=[
        "get_pop",
        "get_pop/modules",
        "get_pop/modules/helper",
        "get_pop/modules/init",
        "get_pop/modules/parse",
    ],
    scripts=["get_pop/bin/getpop"],
    package_data={"get_pop": ["static/usa_pop_counties_2019.csv"]},
)
