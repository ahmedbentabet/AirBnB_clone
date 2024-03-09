#!/usr/bin/python3
"""Print a class Review that inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """class attributes."""

    place_id = ""
    user_id = ""
    text = ""
