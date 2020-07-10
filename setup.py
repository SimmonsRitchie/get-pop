from setuptools import setup, find_packages

requires = ["pyyaml", "python-dotenv", "pandas", "iso8601", "click"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_pop",
    version="1.92",
    author="DSR",
    description="Command line tool to generates CSVs of population data for specified US states.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["population csv geography usa counties"],
    # list folders, not files
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=requires,
    entry_points={"console_scripts": ["getpop=get_pop.cli:main"]},
    package_data={
        "static": ["static/*"],
        "logging": ["logs/config/logging.yaml", "logs/config/logging_test.yaml"],
    },
)
