#!/usr/bin/python3
"""Tests for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class functionality."""

    def test_instance_creation(self):
        """Tests that a BaseModel instance is created."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_exists(self):
        """Tests that every instance has a unique ID."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertIsNotNone(obj1.id)
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at(self):
        """Tests that created_at is a datetime."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at(self):
        """Tests that updated_at is a datetime."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        """Tests dictionary serialization."""
        obj = BaseModel()
        result = obj.to_dict()
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertIn("id", result)
        self.assertIsInstance(result["created_at"], str)

    def test_save(self):
        """Tests that save updates updated_at."""
        obj = BaseModel()
        old_time = obj.updated_at
        obj.save()
        self.assertGreaterEqual(obj.updated_at, old_time)

    def test_str(self):
        """Tests the string representation of BaseModel."""
        obj = BaseModel()
        self.assertIn("[BaseModel]", str(obj))
        self.assertIn(obj.id, str(obj))

    def test_kwargs(self):
        """Tests instance creation from a dictionary."""
        obj = BaseModel()
        new_obj = BaseModel(**obj.to_dict())
        self.assertEqual(obj.id, new_obj.id)
        self.assertIsNot(obj, new_obj)


if __name__ == "__main__":
    unittest.main()