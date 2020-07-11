from setuptools import setup, find_packages
from get_pop import __version__, __author__, __project__

requires = [
    "pyyaml",
    "python-dotenv",
    "pandas",
    "iso8601",
    "click",
    "zipp",
    "mypy-extensions",
    "sphinx",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=__project__,
    version=__version__,
    author=__author__,
    description="A python command line utility that generates CSVs of county-level population data for specified US "
    "states.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["population csv geography usa counties"],
    # list folders, not files
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "getpop=get_pop.cli:main",
            "get_pop=get_pop.cli:main",
            "get-pop=get_pop.cli:main",
        ]
    },
    package_data={"get_pop": ["static/*", "logs/config/logging.yaml"]},
)
