#!/usr/bin/python3
"""City model."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city that belongs to a state."""

    def __init__(self, *args, **kwargs):
        """Initialize a new city instance."""
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
