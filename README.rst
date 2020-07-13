get-pop
---------

.. image:: https://badge.fury.io/py/get-pop.svg
    :target: https://badge.fury.io/py/get-pop

.. image:: https://travis-ci.org/SimmonsRitchie/get-pop.svg?branch=master
    :target: https://travis-ci.org/SimmonsRitchie/get-pop

.. image:: https://readthedocs.org/projects/get-pop/badge/?version=latest
    :target: https://get-pop.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


A command line utility that generates CSVs of county-level population data for specified US states.

Data is based on 2019 U.S. census data.

The full documentation is hosted at `Read the Docs <https://get-pop.readthedocs.io/en/latest/index.html>`_

Install
----------

::

    pip install get-pop

Basic usage
--------------

Command line
================

In the command line, enter the getpop command followed by the two letter postal code of one or more states.
 
Eg.:

::

   getpop ny

   >> Initializing getpop
   >> Selected states: ['ny']
   >> Processing: New York
   >> getpop complete
 
Or:

::

   getpop ny nj tx

   >> Initializing getpop
   >> Selected states: ['ny', 'nj', 'tx']
   >> Processing: New Jersey
   >> Processing: New York
   >> Processing: Texas
   >> getpop complete


To get CSVs for all states, enter:

::

    getpop all


CSVs will be saved in a new directory called 'data' in the current working directory. See 'advanced usage' to override
the location where CSVs are saved.

Programmatic
================

If you prefer, you can also import and call get-pop from within your python app:
  
::

    from get_pop.get_pop import get_pop

    states = ["ny","nj","tx","pa"]
    get_pop(states)


Advanced usage
--------------

Command line
================

In addition to take state abbreviations as positional arguments, getpop takes a handful of optional arguments:


--save-dir, --dir

    TEXT. Absolute path of directory where CSV files will be output. Defaults to saving them in /data in the current
    working directory

--clear-dir, --cdir

    Deletes all existing files in save_dir path. Defaults to false.

--help

    Show this message and exit.

Example:

::

    getpop ny ca tx --save-dir ./state_csvs --clear-dir

License
-----------

`MIT <https://choosealicense.com/licenses/mit/>`_
