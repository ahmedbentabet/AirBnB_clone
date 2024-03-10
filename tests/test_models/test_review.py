#!/usr/bin/python3
"""
Describes  ReviewTestReport classes
"""
import models
import unittest
from models.base_model import BaseModel
from models.review import Review


class ReviewTestReport(unittest.TestCase):
    def test_Review__initialization(self):
        """Verify the creation of Review objects."""
        first_instance = Review()
        second_instnce = Review()
        self.assertEqual(Review, type(Review()))
        self.assertNotEqual(first_instance.id, second_instnce.id)
        self.assertIsInstance(second_instnce, Review())

    def test_review__creation__storage(self):
        """Verify the creation and storge of a new Review instance."""
        self.assertIn(Review(), models.storage.all().values())

    def test_review__user_id(self):
        """Exmaine the user_id property of Review objects."""
        first_instance = Review()
        self.assertIsInstance(first_instnce.user_id, str)
        self.assertTrue(hasattr(first_instnce, "user_id"))
        self.assertEqual(first_instance.user_id, "")
        # Asuming user_id initializes as an empty string

    def test_review__place_id(self):
        """Exmaine the place_id property of Review objects."""
        first_instance = Review()
        self.assertIsInstance(first_instnce.place_id, str)
        self.assertTrue(hasattr(first_instnce, "place_id"))
        self.assertEqual(first_instance.place_id, "")
        # Asuming place_id initializes as an empty string

    def test_review__text(self):
        """Exmaine the text property of Review objects."""
        first_instance = Review()
        self.assertIsInstance(first_instnce.text, str)
        self.assertTrue(hasattr(first_instnce, "text"))
        self.assertEqual(first_instance.text, "")
        # Asuming text initializes as an empty string


if __name__ == "__main__":
    unittest.main()
