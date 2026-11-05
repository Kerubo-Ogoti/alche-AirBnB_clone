
#!/usr/bin/python3
"""Contains tests for the City class."""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests the City class."""

    def test_inheritance(self):
        """Checks City inheritance."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Checks the default City attributes."""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()
