#!/usr/bin/python3
"""Print a class User that inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class attributes."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
