#!/usr/bin/python3
"""Print a class FileStorage that serializes instand deserializes JSON file."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class attributes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects saved in a dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Include a new object to the repository."""
        ky = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({ky: obj})

    def save(self):
        """Serializes __objects to the JSON file."""
        serial_objects = {}
        for val_obj, ky in FileStorage.__objects.items():
            serial_objects[val_obj] = ky.to_dict()
        with open(FileStorage.__file_path, "w") as file_js:
            json.dump(serial_objects, file_js, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file_js:
                filled_data = json.load(file_js)
                for key_obj, dictionary_obj in filled_data.items():
                    clas_nam = dictionary_obj["__class__"]
                    dictionary_obj.pop('id', None)  # Remove the 'id' attribute
                    FileStorage.__objects[key_obj] = eval(clas_nam)(**dictionary_obj)
