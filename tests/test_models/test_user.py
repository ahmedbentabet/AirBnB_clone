#!/usr/bin/python3
"""
Describes  UserTestReport classes
"""
import models
import unittest
from models.base_model import BaseModel
from models.user import User


class UserTestReport(unittest.TestCase):
    def test_user_initialization(self):
        """Verify the creation of User objects."""
        first_instance = User()
        second_instance = User()
        self.assertEqual(User, type(User()))
        self.assertNotEqual(first_instance.id, second_instance.id)
        self.assertIsInstance(second_instance, User)

    def test_user_creation_storage(self):
        """Verify the creation and storge of a new User instance."""
        self.assertIn(User(), models.storage.all().values())

    def test_user_email_atrribute(self):
        """Confirm the email feature of User objects."""
        first_instance = User()
        self.assertIsInstance(first_instance.email, str)
        self.assertTrue(hasattr(first_instance, "email"))
        self.assertEqual(first_instance.email, "")
        # Asuming email initializes as an empty string

    def test_user_password(self):
        """Inspect the password of User entities."""
        first_instance = User()
        self.assertIsInstance(first_instance.password, str)
        self.assertTrue(hasattr(first_instance, "password"))
        self.assertEqual(first_instance.password, "")
        # Asuming password initializes as an empty string

    def test_user_id(self):
        """Exmaine the id property of User objects."""
        first_instance = User()
        self.assertIsInstance(first_instance.id, str)
        self.assertTrue(hasattr(first_instance, "id"))
        self.assertEqual(first_instance.id, "")
        # Asuming id initializes as an empty string

    def test_user_last_name(self):
        """confirm the last_name property of User instances."""
        first_instance = User()
        self.assertIsInstance(first_instance.last_name, str)
        self.assertTrue(hasattr(first_instance, "last_name"))
        self.assertEqual(first_instance.last_name, "")
        # Asuming last_name initializes as an empty string

    def test_user_first_name(self):
        """Confirm the first_name property of User instances."""
        first_instance = User()
        self.assertIsInstance(first_instance.first_name, str)
        self.assertTrue(hasattr(first_instance, "first_name"))
        self.assertEqual(first_instance.first_name, "")
        # Asuming first_name initializes as an empty string


if __name__ == "__main__":
    unittest.main()
