"""
uTinyDB is a tiny, document oriented database optimized for your happiness :)

uTinyDB stores differrent types of Python data types using a configurable
storage mechanism. It comes with a syntax for querying data and storing
data in multiple tables.

.. codeauthor:: Markus Siemens <markus@m-siemens.de>
.. codeauthor:: José Ricardo Borba <jrborba@betterdays.app>
Usage example:

>>> from utinydb import uTinyDB, where
>>> from utinydb.storages import MemoryStorage
>>> db = TinyDB(storage=MemoryStorage)
>>> db.insert({'data': 5})  # Insert into '_default' table
>>> db.search(where('data') == 5)
[{'data': 5, '_id': 1}]
>>> # Now let's create a new table
>>> tbl = db.table('our_table')
>>> for i in range(10):
...     tbl.insert({'data': i})
...
>>> len(tbl.search(where('data') < 5))
5
"""

from .queries import Query, where
from .storages import Storage, JSONStorage
from .database import TinyDB
from .version import __version__

__all__ = ("uTinyDB", "Storage", "JSONStorage", "Query", "where")
