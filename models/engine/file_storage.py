#!/usr/bin/python3
"""Serializes instances to a JSON file and reloads them."""

import json
import os


class FileStorage:
    """Store objects in memory and persist them to file.json."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize all objects to JSON."""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """Load objects from the JSON file if it exists."""
        if not os.path.exists(self.__file_path):
            return
        if os.path.getsize(self.__file_path) == 0:
            return

        with open(self.__file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.__objects.clear()
        for key, value in data.items():
            class_name = value.get("__class__")
            if class_name is None:
                continue

            if class_name == "BaseModel":
                from models.base_model import BaseModel

                obj = BaseModel(**value)
            elif class_name == "User":
                from models.user import User

                obj = User(**value)
            elif class_name == "State":
                from models.state import State

                obj = State(**value)
            elif class_name == "City":
                from models.city import City

                obj = City(**value)
            elif class_name == "Amenity":
                from models.amenity import Amenity

                obj = Amenity(**value)
            elif class_name == "Place":
                from models.place import Place

                obj = Place(**value)
            elif class_name == "Review":
                from models.review import Review

                obj = Review(**value)
            else:
                continue

            self.__objects[key] = obj
