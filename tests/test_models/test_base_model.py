#!/usr/bin/python3
"""A test class for the base_model module."""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A test class for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.my_model = BaseModel()

    def test_id_is_string(self):
        """Test that the 'id' attribute is a string."""
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at_is_datetime(self):
        """Test that the 'created_at' attribute is a datetime object."""
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """Test that the 'updated_at' attribute is a datetime object."""
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        """Test that calling 'save' updates the 'updated_at' attribute."""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        """Test that calling 'to_dict' returns a dictionary."""
        my_dict = self.my_model.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_to_dict_contains_keys(self):
        """Test that the keys 'id', 'created_at', 'updated_at', and '__class__' are in the dictionary."""
        my_dict = self.my_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, my_dict)

    def test_to_dict_datetime_format(self):
        """Test that 'created_at' and 'updated_at' are in ISO format in the dictionary."""
        my_dict = self.my_model.to_dict()
        self.assertTrue(isinstance(my_dict['created_at'], str))
        self.assertTrue(isinstance(my_dict['updated_at'], str))
