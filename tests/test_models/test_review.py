
#!/usr/bin/python3
"""Contains tests for the Review class."""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests the Review class."""

    def test_inheritance(self):
        """Checks Review inheritance."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Checks the default Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
