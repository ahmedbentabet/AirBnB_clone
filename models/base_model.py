#!/usr/bin/python3
"""Define the Module base_module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Define BaseModel class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance with a unique ID,
        and sets the creation and update times.
        """

        # convert "created_at" and "updated_at" : str -> datetime
        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"]
                )
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"]
                )

            # Initializes a new instance with the values from kwargs
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

        else:
            # New instance with default values for id, created_at & updated_at.
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # add this new instance to the FileStorage __objects
            from models import storage  # Import here to avoid circular imports
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        Calls the save method of the associated FileStorage instance to
        serialize and store the current instance's state.
        """

        self.updated_at = datetime.now()
        from models import storage  # Import here to avoid circular imports
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance,
        with 'created_at' and 'updated_at' converted to ISO format,
        and includes the class name.
        """

        my_dict = self.__dict__.copy()
        # convert "created_at" and "updated_at" : datetime -> str
        # convert "created_at" and "updated_at" : datetime -> str
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        # add the class name to my_dict
        my_dict['__class__'] = self.__class__.__name__

        return my_dict
