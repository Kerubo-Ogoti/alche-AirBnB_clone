
#!/usr/bin/python3
"""Contains tests for the User class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests the User class."""

    def test_inheritance(self):
        """Checks that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_default_attributes(self):
        """Checks the default User attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_update(self):
        """Checks that User attributes can be changed."""
        user = User()
        user.first_name = "Faith"
        user.last_name = "Ogoti"
        self.assertEqual(user.first_name, "Faith")
        self.assertEqual(user.last_name, "Ogoti")


if __name__ == "__main__":
    unittest.main()
