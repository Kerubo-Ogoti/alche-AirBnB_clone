#!/usr/bin/python3
"""Command interpreter entry point for the AirBnB clone."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """Do nothing when the user enters an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF."""
        return True

    def do_create(self, arg):
        """Create a new instance of a class and save it."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[class_name]()
        print(instance.id)
        storage.save()

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Delete an instance and save the change."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all stored instances or all of a specific class."""
        args = shlex.split(arg)
        objects = storage.all().values()
        if args:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            objects = [obj for obj in objects if obj.__class__.__name__ == args[0]]
        print([str(obj) for obj in objects])

    def do_update(self, arg):
        """Update an instance attribute and save the change."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return

        attr_name = args[2]
        attr_value = args[3]
        if attr_value.lower() == "true":
            attr_value = True
        elif attr_value.lower() == "false":
            attr_value = False
        else:
            try:
                if "." in attr_value:
                    attr_value = float(attr_value)
                else:
                    attr_value = int(attr_value)
            except ValueError:
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg):
        """Count the number of instances of a class."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        count = sum(
            1 for obj in storage.all().values()
            if obj.__class__.__name__ == args[0]
        )
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
