from setuptools import setup


setup(
    name="get_pop",
    version="1.0",
    # list folders, not files
    packages=["get_pop"],
    scripts=["get_pop/bin/run_script.py"],
    package_data={"get_pop": ["static/usa_pop_counties_2019.csv"]},
)
