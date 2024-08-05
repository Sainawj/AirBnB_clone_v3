#!/usr/bin/python3
"""Create a storage instance based on the environment."""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
