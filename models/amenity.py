#!/usr/bin/python3

""" I am Defining the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

