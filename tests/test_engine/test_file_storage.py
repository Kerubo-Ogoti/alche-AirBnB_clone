
#!/usr/bin/python3
"""Contains tests for the FileStorage class."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class."""

    def setUp(self):
        """Creates a storage instance for testing."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Checks that all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Checks that new adds an object."""
        model = BaseModel()
        self.storage.new(model)
        key = "BaseModel." + model.id
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Checks that objects can be saved and reloaded."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = "BaseModel." + model.id
        self.assertIn(key, new_storage.all())

    def tearDown(self):
        """Cleans up the test JSON file."""
        self.storage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
