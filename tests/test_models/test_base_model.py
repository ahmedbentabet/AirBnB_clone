#!/usr/bin/python3
"""A test class for the base_model module."""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A test class for the BaseModel class."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_initialization(self):
        """Test proper initialization of BaseModel instance"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_string_representation(self):
        """Test the __str__ method for BaseModel instance"""
        expected_str = f"[BaseModel] ({self.base_model.id}) {
            self.base_model.__dict__
            }"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """Test the save method for updating 'updated_at' attribute"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertGreater(new_updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method for dictionary representation"""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_from_dict_method(self):
        """Test creating an instance from a dictionary"""
        model_dict = self.base_model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.created_at, self.base_model.created_at)
        self.assertEqual(new_model.id, self.base_model.id)
        self.assertEqual(new_model.updated_at, self.base_model.updated_at)
