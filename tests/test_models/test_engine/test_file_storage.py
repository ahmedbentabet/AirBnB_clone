#!/usr/bin/python3
"""Test FileStorage class."""
import os
import unittest
import json
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test__FileStorage(unittest.TestCase):
    """Test FileStorage class."""

    @classmethod
    def setUp(self):
        """Prepare the environment before each individual test."""
        try:
            os.rename("file.json", "new_file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDown(self):
        """Perform cleanup after each individual test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("new_file.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage_objects = {}

    def test__FileStorage_instance_creation(self):
        """Verify that a FileStorage instance is created."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test__FileStorage_with_argument_raises_type_error(self):
        """Ensure TypeError is raised when a n-empty
        arg is passed to FileStorage."""
        self.assertRaises(TypeError, FileStorage, "non_empty_argument")

    def test__FileStorage_file_path_is_string(self):
        """Verify that the file_path attribute is a string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test__FileStorage_objects_is_dictionary(self):
        """Verify that the objects attribute is a dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test__ModelsStorage_instance_creation(self):
        """Verify that models.storage is an instance of FileStorage."""
        self.assertIsInstance(models.storage, FileStorage)

    def test__all_rd(self):
        """Verify that the all method returns a dictionary."""
        self.assertEqual(dict, type(models.storage.all()))

    def test__all_raises_type_error_with_argument(self):
        """Verify that TypeError is raised when an arg to all method."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test__new_ss(self):
        """Verify that new method success adds instances to storage saved."""
        instance_base_model = BaseModel()
        instance_user = User()
        instance_state = State()
        instance_place = Place()
        instance_city = City()
        instance_amenity = Amenity()
        instance_review = Review()

        # Add storage
        models.storage.new(instance_base_model)
        models.storage.new(instance_user)
        models.storage.new(instance_state)
        models.storage.new(instance_place)
        models.storage.new(instance_city)
        models.storage.new(instance_amenity)
        models.storage.new(instance_review)

        # Verify if add storage
        self.assertIn("BaseModel." + instance_base_model.id,
                      models.storage.all().keys())
        self.assertIn(instance_base_model, models.storage.all().values())
        self.assertIn(instance_base_model, models.storage.all().values())
        self.assertIn("User." + instance_user.id, models.storage.all().keys())
        self.assertIn(instance_user, models.storage.all().values())
        self.assertIn("State." + instance_state.id,
                      models.storage.all().keys())
        self.assertIn(instance_state, models.storage.all().values())
        self.assertIn("Place." + instance_place.id,
                      models.storage.all().keys())
        self.assertIn(instance_place, models.storage.all().values())
        self.assertIn("City." + instance_city.id,
                      models.storage.all().keys())
        self.assertIn(instance_city, models.storage.all().values())
        self.assertIn("Amenity." + instance_amenity.id,
                      models.storage.all().keys())
        self.assertIn(instance_amenity, models.storage.all().values())
        self.assertIn("Review." + instance_review.id,
                      models.storage.all().keys())
        self.assertIn(instance_review, models.storage.all().values())

    def test__new_method_with_args_raises_type_error(self):
        """Verify that TypeError is raised when an arg to new method."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test__save_sf(self):
        """Verify that instances are saved in the file."""
        instance_base_model = BaseModel()
        instance_user = User()
        instance_state = State()
        instance_place = Place()
        instance_city = City()
        instance_amenity = Amenity()
        instance_review = Review()

        # Add storage and save
        models.storage.new(instance_base_model)
        models.storage.new(instance_user)
        models.storage.new(instance_state)
        models.storage.new(instance_place)
        models.storage.new(instance_city)
        models.storage.new(instance_amenity)
        models.storage.new(instance_review)
        models.storage.save()

        # Verify if file saved
        file_contents = ""
        with open("file.json", "r") as file:
            file_contents = file.read()
            self.assertIn("BaseModel." + instance_base_model.id, file_contents)
            self.assertIn("User." + instance_user.id, file_contents)
            self.assertIn("State." + instance_state.id, file_contents)
            self.assertIn("Place." + instance_place.id, file_contents)
            self.assertIn("City." + instance_city.id, file_contents)
            self.assertIn("Amenity." + instance_amenity.id, file_contents)
            self.assertIn("Review." + instance_review.id, file_contents)

    def test__save_raises_type_error_with_argument(self):
        """Verify that TypeError is raised when an arg is passed to save."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test__reload_rs(self):
        """Verify that instances are reloaded in the storage."""
        instance_base_model = BaseModel()
        instance_user = User()
        instance_state = State()
        instance_place = Place()
        instance_city = City()
        instance_amenity = Amenity()
        instance_review = Review()

        # Add storage and save
        models.storage.new(instance_base_model)
        models.storage.new(instance_user)
        models.storage.new(instance_state)
        models.storage.new(instance_place)
        models.storage.new(instance_city)
        models.storage.new(instance_amenity)
        models.storage.new(instance_review)
        models.storage.save()
        models.storage.reload()

        # Verify that the inst are reloaded into the  storage
        reloaded_obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + instance_base_model.id, reloaded_obj)
        self.assertIn("User." + instance_user.id, reloaded_obj)
        self.assertIn("State." + instance_state.id, reloaded_obj)
        self.assertIn("Place." + instance_place.id, reloaded_obj)
        self.assertIn("City." + instance_city.id, reloaded_obj)
        self.assertIn("Amenity." + instance_amenity.id, reloaded_obj)
        self.assertIn("Review." + instance_review.id, reloaded_obj)

    def test__reload_raises_type_error_with_argument(self):
        """Verify that TypeError is raised when an arg is passed to reload."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
