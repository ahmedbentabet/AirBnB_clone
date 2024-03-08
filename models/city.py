#!/usr/bin/python3
"""Print a class city that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class attributes."""

    state_id = ""
    name = ""
