#!/usr/bin/python3
"""
Describes  AmenityTestReport classes
"""
import models
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTestReport(unittest.TestCase):
    def test_Amenity__initialization(self):
        """Verify the creation of Amenity objects."""
        first_instance = Amenity()
        self.assertEqual(Amenity, type(Amenity()))
        self.assertNotEqual(first_instance.id, Amenity().id)
        self.assertIsInstance(second_instance, Amenity)

    def test_amenity__creation__storage(self):
        """Verify the creation and storge of a new Amenity instance."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_amenity__name(self):
        """confirm the name property of Amenity instances."""
        first_instance = Amenity()
        self.assertIsInstance(first_instance.name, str)
        self.assertTrue(hasattr(first_instance, "name"))
        self.assertEqual(first_instance.name, "")
        # Asuming name initializes as an empty string


if __name__ == "__main__":
    unittest.main()
