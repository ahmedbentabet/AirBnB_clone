#!/usr/bin/python3
"""Define the Module base_module"""
import uuid
import datetime


class BaseModel:
    """Define BaseModel class"""

    def __init__(self):
        """
        Initializes the BaseModel instance with a unique ID,
        and sets the creation and update times.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attribute to the current datetime."""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance,
        with 'created_at' and 'updated_at' converted to ISO format,
        and includes the class name.
        """

        my_dict = self.__dict__.copy()
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
