#!/usr/bin/python3
"""
Describes  CityTestReport classes
"""
import models
import unittest
from models.base_model import BaseModel
from models.city import City


class CityTestReport(unittest.TestCase):
    def test_city__initialization(self):
        """Verify the creation of User objects."""
        first_instance = City()
        second_instnce = City()
        self.assertEqual(City, type(City()))
        self.assertNotEqual(first_instance.id, second_instnce.id)
        self.assertIsInstance(second_instnce, City)

    def test_city__creation__storage(self):
        """Verify the creation and storge of a new city instance."""
        self.assertIn(City(), models.storage.all().values())

    def test_city__name(self):
        """Confirm the name property of city instances."""
        first_instance = City()
        self.assertIsInstance(first_instnce.name, str)
        self.assertTrue(hasattr(first_instance, "name"))
        self.assertEqual(first_instance.name, "")
        # Asuming name initializes as an empty string

    def test_city__id(self):
        """Exmaine the id property of City objects."""
        first_instance = City()
        self.assertIsInstance(first_instnce.state_id, str)
        self.assertTrue(hasattr(first_instnce, "state_id"))
        self.assertEqual(first_instance.state_id, "")
        # Asuming state_id initializes as an empty string


if __name__ == "__main__":
    unittest.main()
