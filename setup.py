from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_pop",
    version="1.0",
    author="DSR",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # list folders, not files
    packages=["get_pop"],
    scripts=["get_pop/bin/run_script.py"],
    package_data={"get_pop": ["static/usa_pop_counties_2019.csv"]},
)
