#!/usr/bin/python3
"""Print a class FileStorage that serializes instances to a JSON file and deserializes JSON file."""
import os
import json
from models.base_model import BaseModel

class FileStorage:
    """class attributes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects saved in a dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Include a new object to the repository."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects.update({key: obj})

    def save(self):
    """Serializes __objects to the JSON file."""
    serial_objects = {key_obj: value_obj.to_dict() for key_obj, value_obj in FileStorage.__objects.items()}
    with open(FileStorage.__file_path, "w") as file_js:
        json.dump(serial_objects, file_js, delimiter=2)
    
     def reload(self):
    """deserializes the JSON file to __objects."""
    with open(FileStorage.__file_path, "r") as file_js:
        filled_data = json.load(file_js)
        for key_obj, id_obj in filled_data.items():
            family_class = id_obj["__class__"]
            FileStorage.__objects[key_obj] = eval(family_class)(**id_obj)
