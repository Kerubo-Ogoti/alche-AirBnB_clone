
#!/usr/bin/python3
"""Defines the BaseModel class for all project models."""

import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """Defines common attributes and methods for all project models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance or recreate one from a dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        try:
                            value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f"
                            )
                        except ValueError:
                            value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S"
                            )
                setattr(self, key, value)
            self.id = getattr(self, "id", str(uuid.uuid4()))
            self.created_at = getattr(
                self,
                "created_at",
                datetime.now(),
            )
            self.updated_at = getattr(
                self,
                "updated_at",
                self.created_at,
            )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the printable representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update the modification time and save the instance."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
