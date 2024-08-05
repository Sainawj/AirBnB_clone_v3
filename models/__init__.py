#!/usr/bin/python3
"""Create a storage instance based on the environment."""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

# Initialize storage based on the environment
def get_storage():
    """Return the storage instance."""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        return DBStorage()
    else:
        return FileStorage()

storage = get_storage()
storage.reload()
