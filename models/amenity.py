#!/usr/bin/python3
"""Amenity model."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity available in a place."""

    def __init__(self, *args, **kwargs):
        """Initialize a new amenity instance."""
        self.name = ""
        super().__init__(*args, **kwargs)
