#!/usr/bin/python3
"""Test FileStorage class."""

import os
import unittest
import models

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

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

class Test_FileStorage(unittest.TestCase):
    """Test FileStorage class."""

    def test_FileStorage_instance_creation(self):
        """Verify that a FileStorage instance is created."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_argument_raises_type_error(self):
        """Ensure TypeError is raised when a non-empty argument is passed to FileStorage."""
        self.assertRaises(TypeError, FileStorage, "non_empty_argument")

    def test_FileStorage_without_argument_raises_type_error(self):
        """Ensure TypeError is raised when no argument is passed to FileStorage."""
        self.assertRaises(TypeError, FileStorage)

    def test_FileStorage_file_path_is_string(self):
        """Verify that the file_path attribute is a string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    
    def test_FileStorage_objects_is_dictionary(self):
        """Verify that the objects attribute is a dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    
    def test_ModelsStorage_instance_creation(self):
        """Verify that models.storage is an instance of FileStorage."""
        self.assertIsInstance(models.storage, FileStorage)

    def test_all(self):
        """Verify that the all method returns a dictionary."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_raises_type_error_with_argument(self):
        """Verify that TypeError is raised when an argument is passed to the all method."""
        with self.assertRaises(TypeError):
           models.storage.all(None)

    def test_new(self):
        """Verify that the new method successfully adds instances to the storage and ensures they are saved."""
        instance_base_model = BaseModel()
        

        # Add storage
        models.storage.new(instance_base_model)
        
        # Verify if add storage
        self.assertIn("BaseModel." + instance_base_model.id, models.storage.all().keys())
        self.assertIn(instance_base_model, models.storage.all().values())

    def test_new_method_with_args_raises_type_error(self):
        """Verify that TypeError is raised when an argument is passed to new method."""
        with self.assertRaises(TypeError):
           models.storage.new(BaseModel(), 1)


    def test_save(self):
        """Verify that instances are saved in the file."""
        instance_base_model = BaseModel()
        
        # Add storage and save
        models.storage.new(instance_base_model)

        # Verify if file saved
        file_contents = ""
        with open("file.json", "r") as file_obj:
            file_contents = file_obj.read()
            self.assertIn("BaseModel." + instance_base_model.id, file_contents)

    def test_save_raises_type_error_with_argument(self):
        """Verify that TypeError is raised when an argument is passed to save."""
        with self.assertRaises(TypeError):
           models.storage.save(None)

    def test_reload(self):
        """Verify that instances are reloaded in the storage."""
        instance_base_model = BaseModel()

        # Add storage and save
        models.storage.new(instance_base_model)

        # Verify that the inst are reloaded into the  storage
        reloaded_obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + instance_base_model.id, reloaded_obj)

    def test_reload_raises_type_error_with_argument(self):
        """Verify that TypeError is raised when an argument is passed to reload."""
        with self.assertRaises(TypeError):
           models.storage.reload(None)

    if __name__ == "__main__":
      unittest.main()
