#!/usr/bin/python3
"""Define a class FileStorage for serializing and deserializing JSON file."""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Manage serialization and deserialization of JSON file."""

    __file_path = "file.json"
    # dict to store all objects : key/value = <class name>.id / <obj_name>
    __objects = {}

    def all(self):
        """Return the dict __objects ."""
        return self.__objects

    def new(self, obj):
        """Add " obj_class_name.obj_id" = obj " to the dict '__objects'."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                loaded_objs = json.load(file)
                for key, obj_to_dict in loaded_objs.items():
                    # get class_name as a string
                    class_name = obj_to_dict["__class__"]
                    if class_name:
                        # Evaluate the class name and assign it to obj_class
                        obj_class = eval(class_name)
                        if obj_class:
                            # create a new_instance
                            # and initialize its attributs with "obj_to_dict"
                            new_instance = obj_class(**obj_to_dict)
                            self.__objects[key] = new_instance
