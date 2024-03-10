#!/usr/bin/python3
"""
Describes  PlaceTestReport classes
"""
import models
import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class PlaceTestReport(unittest.TestCase):
    def test_place__initialization(self):
        """Verify the creation of Place objects."""
        first_instance = Place()
        second_instnce = Place()
        self.assertEqual(Place, type(Place()))
        self.assertNotEqual(first_instance.id, second_instnce.id)
        self.assertIsInstance(second_instnce, Place)

    def test_place__creation__storage(self):
        """Verify the creation and storge of a new Place instance."""
        self.assertIn(Place(), models.storage.all().values())

    def test_place__city_id(self):
        """Exmaine the city_id property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.city_id, str)
        self.assertTrue(hasattr(first_instnce, "city_id"))
        self.assertEqual(first_instance.city_id, "")
        # Asuming city_id initializes as an empty string

    def test_place__user_id(self):
        """Exmaine the user_id property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.user_id, str)
        self.assertTrue(hasattr(first_instnce, "user_id"))
        self.assertEqual(first_instance.user_id, "")
        # Asuming user_id initializes as an empty string

    def test_place__name(self):
        """confirm the name property of Place instances."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.name, str)
        self.assertTrue(hasattr(first_instance, "name"))
        self.assertEqual(first_instance.name, "")
        # Asuming name initializes as an empty string

    def test_place__description(self):
        """Confirm the description property of Place instances."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.description, str)
        self.assertTrue(hasattr(first_instance, "description"))
        self.assertEqual(first_instance.description, "")
        # Asuming description initializes as an empty string

    def test_place__number_rooms(self):
        """Exmaine the number_rooms property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.number_rooms, int)
        self.assertTrue(hasattr(first_instnce, "number_rooms"))
        self.assertEqual(first_instance.number_rooms, 0)
        # Asuming number_rooms initializes to 0

    def test_place__number_bathrooms(self):
        """Exmaine the number_bathrooms property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.number_bathrooms, int)
        self.assertTrue(hasattr(first_instnce, "number_bathrooms"))
        self.assertEqual(first_instance.number_bathrooms, 0)
        # Asuming number_bathrooms initializes to 0

    def test_place__max_guest(self):
        """Exmaine the max_guest property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.max_guest, int)
        self.assertTrue(hasattr(first_instnce, "max_guest"))
        self.assertEqual(first_instance.max_guest, 0)
        # Asuming max_guest initializes to 0

    def test_place__price_by_night(self):
        """Exmaine the price_by_night property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.price_by_night, int)
        self.assertTrue(hasattr(first_instnce, "price_by_night"))
        self.assertEqual(first_instance.price_by_night, 0)
        # Asuming price_by_night initializes to 0

    def test_place__latitude(self):
        """Confirm the latitude property of Place instances."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.latitude, float)
        self.assertTrue(hasattr(first_instance, "latitude"))
        self.assertEqual(first_instance.latitude, 0.0)
        # Asuming latitude initializes to 0.0

    def test_place__longitude(self):
        """Confirm the longitude property of Place instances."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.longitude, float)
        self.assertTrue(hasattr(first_instance, "longitude"))
        self.assertEqual(first_instance.longitude, 0.0)
        # Asuming longitude initializes to 0.0

    def test_place__amenity_ids(self):
        """Exmaine the amenity_ids property of Place objects."""
        first_instance = Place()
        self.assertIsInstance(first_instnce.amenity_ids, list)
        self.assertTrue(hasattr(first_instnce, "amenity_ids"))
        self.assertEqual(first_instance.amenity_ids, [])
        # Asuming  amenity_ids initializes as an empty list


if __name__ == "__main__":
    unittest.main()
