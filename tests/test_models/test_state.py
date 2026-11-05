
#!/usr/bin/python3
"""Contains tests for the State class."""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests the State class."""

    def test_inheritance(self):
        """Checks State inheritance."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_name(self):
        """Checks the default name."""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
