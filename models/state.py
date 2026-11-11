#!/usr/bin/python3
"""State model."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state in the application."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new state instance."""
        self.name = ""
        super().__init__(*args, **kwargs)
