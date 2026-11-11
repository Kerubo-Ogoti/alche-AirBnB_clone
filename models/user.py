#!/usr/bin/python3
"""User model."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user account in the application."""

    def __init__(self, *args, **kwargs):
        """Initialize a new user instance."""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
