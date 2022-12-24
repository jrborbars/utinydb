uTinyDB
*******
WIP! But it works, even using lots of memory.

|Build Status| |Coverage| |Version|

Quick Links
***********

- `Example Code`_
- `Supported Python Versions`_
- `Documentation <http://utinydb.readthedocs.org/>`_

Introduction
************

uTinyDB is a VERY lightweight document oriented database optimized for embedded systems.
It's written in pure Python and has no external dependencies. The target are
REALLY small apps that need a database BUT does not need all the clutter that come with.

uTinyDB is:

- **tiny:** The current source code has XXXX lines of code.

- **document oriented:** Like MongoDB_, you can store any document
  (represented as ``dict``) in TinyDB.

- **optimized for embedded systems:** TinyDB is designed to be simple and
  fun to use by providing a simple and clean API.

- **written in pure Python:** TinyDB neither needs an external server (as
  e.g. `PyMongo <https://api.mongodb.org/python/current/>`_) nor any dependencies
  from PyPI.

- **works on uPython 1.12+:** TinyDB works on all modern versions of uPython.
''
To dive straight into all the details, head over to the `uTinyDB docs
<https://utinydb.readthedocs.io/>`_. You can also discuss everything related
to uTinyDB like general development, extensions or showcase your uTinyDB-based
projects.

Example Code
************

.. code-block:: python

    >>> from utinydb import TinyDB, Query
    >>> db = uTinyDB('/path/to/db.json')
    >>> db.insert({'int': 1, 'char': 'a'})
    >>> db.insert({'int': 1, 'char': 'b'})

Query Language
==============

.. code-block:: python

    >>> User = Query()
    >>> # Search for a field value
    >>> db.search(User.name == 'John')
    [{'name': 'John', 'age': 22}, {'name': 'John', 'age': 37}]

    >>> # Combine two queries with logical and
    >>> db.search((User.name == 'John') & (User.age <= 30))
    [{'name': 'John', 'age': 22}]

    >>> # Combine two queries with logical or
    >>> db.search((User.name == 'John') | (User.name == 'Bob'))
    [{'name': 'John', 'age': 22}, {'name': 'John', 'age': 37}, {'name': 'Bob', 'age': 42}]

    >>> # Apply transformation to field with `map`
    >>> db.search((User.age.map(lambda x: x + x) == 44))
    >>> [{'name': 'John', 'age': 22}]

    >>> # More possible comparisons:  !=  <  >  <=  >=
    >>> # More possible checks: where(...).matches(regex), where(...).test(your_test_func)

Tables
======

.. code-block:: python

    >>> table = db.table('name')
    >>> table.insert({'value': True})
    >>> table.all()
    [{'value': True}]


Contributing
************

Whether reporting bugs, discussing improvements and new ideas or writing
extensions: Contributions to uTinyDB are welcome! Here's how to get started:

1. Check for open issues or open a fresh issue to start a discussion around
   a feature idea or a bug
2. Fork `the repository <https://github.com/jrborbars/utinydb/>`_ on Github,
   create a new branch off the `master` branch and start making your changes
   (known as `GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_)
3. Write a test which shows that the bug was fixed or that the feature works
   as expected
4. Send a pull request and bug the maintainer until it gets merged and
   published ☺

.. |Build Status| image:: https://img.shields.io/azure-devops/build/msiemens/3e5baa75-12ec-43ac-9728-89823ee8c7e2/2.svg?style=flat-square
   :target: https://dev.azure.com/msiemens/github/_build?definitionId=2
.. |Coverage| image:: http://img.shields.io/coveralls/msiemens/tinydb.svg?style=flat-square
   :target: https://coveralls.io/r/msiemens/tinydb
.. |Version| image:: http://img.shields.io/pypi/v/tinydb.svg?style=flat-square
   :target: https://pypi.python.org/pypi/tinydb/
.. _Buzhug: http://buzhug.sourceforge.net/
.. _CodernityDB: https://github.com/perchouli/codernitydb
.. _MongoDB: http://mongodb.org/
