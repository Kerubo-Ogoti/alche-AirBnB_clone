#!/usr/bin/python3
"""Tests for the FileStorage class."""

import os
import tempfile
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage object management and persistence."""

    def setUp(self):
        """Create isolated in-memory and on-disk storage for each test."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = os.path.join(
            self.temp_dir.name, "file.json"
        )
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Remove the temporary storage file."""
        self.temp_dir.cleanup()

    def test_private_attributes(self):
        """Check storage path and object collection types."""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage.all(), dict)

    def test_all(self):
        """Return the storage object's dictionary."""
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """Add an object under its class and identifier."""
        obj = BaseModel(id="sample", created_at=datetime.now(),
                        updated_at=datetime.now())
        self.storage.new(obj)
        self.assertIs(self.storage.all()["BaseModel.sample"], obj)

    def test_save_reload(self):
        """Persist objects and recreate them from the JSON file."""
        obj = BaseModel(id="sample", created_at=datetime.now(),
                        updated_at=datetime.now())
        self.storage.new(obj)
        self.storage.save()

        self.storage.all().clear()
        self.storage.reload()

        restored = self.storage.all()["BaseModel.sample"]
        self.assertEqual(restored.id, obj.id)
        self.assertEqual(restored.created_at, obj.created_at)
        self.assertEqual(restored.updated_at, obj.updated_at)

    def test_reload_without_file(self):
        """Leave storage unchanged when the JSON file does not exist."""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
