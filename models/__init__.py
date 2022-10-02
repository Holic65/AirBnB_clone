#!/usr/bin/python3
'''init module importing storage'''
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
