#!/usr/bin/python3
"""Review model."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review left for a listing."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new review instance."""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
