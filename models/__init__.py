#!/usr/bin/python3
"""This script create a unique FileStorage instance for our application."""
from models.engine.file_storage import FileStorage

storage = FileStorage()

# Call the reload() method on this variable
storage.reload()
