from setuptools import setup, find_packages

requires = ["pyyaml", "python-dotenv", "pandas", "iso8601", "click"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_pop",
    version="1.7",
    author="DSR",
    description="Command line tool to generates CSVs of population data for specified US states.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["population csv geography usa counties"],
    # list folders, not files
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=requires,
    scripts=["get_pop/bin/getpop"],
    package_data={"get_pop": ["static/*"]},
)
