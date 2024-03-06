#!/usr/bin/python3
"""Print a class FileStorage that serializes instances to a JSON file and deserializes JSON file."""
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
    serial_objects = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
    with open(FileStorage.__file_path, "w") as json_file:
        json.dump(serial_objects, json_file, delimiter=2)
    
     def reload(self):
    """deserializes the JSON file to __objects."""
    with open(FileStorage.__file_path, "r") as json_file:
        filled_data = json.load(json_file)
        for obj_id, obj_dict in filled_data.items():
            family_class = obj_dict["__class__"]
            FileStorage.__objects[obj_id] = eval(family_class)(**obj_dict)
