#!/usr/bin/python3
"""
__init__ method for models directory
"""
from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()