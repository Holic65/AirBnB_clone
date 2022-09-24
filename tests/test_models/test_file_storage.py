#!/usr/bin/python3
import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class test_FileStorage(unittest.TestCase):
    """
    The unit test for the functions in the
    FileStorage class
    """

    def test_new(self):
        """
        Test that the new instance is stored
        """
        user = BaseModel()
        file_content1 = FileStorage.all(FileStorage)
        for key, value in file_content1.items():
            val = "{}.{}".format("BaseModel", user.id)
            if key == val:
                obj = (file_content1[key])
                self.assertEqual(obj, user)

    def test_all_returns_type(self):
        """Test that all returns the correct file"""
        file_content1 = FileStorage.all(FileStorage)
        self.assertIsNotNone(file_content1)
        self.assertIs(file_content1, FileStorage.all(FileStorage))
        self.assertEqual(type(file_content1), dict)

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        test to determine if the reload method is fine
        """
        FileStorage().reload()
        storage = FileStorage()
        initial_content = storage.all()
        initial_count = len(initial_content)
        # add a new baseModel
        new_basemodel = BaseModel()
        FileStorage().reload()
        new_storage_content = FileStorage().all()
        new_count = len(new_storage_content)
        self.assertNotEqual(initial_count, new_count)


if __name__ == "__main__":
    unittest.main()
