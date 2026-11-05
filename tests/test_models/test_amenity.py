
#!/usr/bin/python3
"""Contains tests for the Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def test_inheritance(self):
        """Checks Amenity inheritance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name(self):
        """Checks the default name."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
