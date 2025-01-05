#!/usr/bin/python3
"""This module contains the command interpreter for the HBNB project"""

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
    """Command interpreter for the HBNB project"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        # Create a new instance
        new_instance = storage.classes()[class_name]()

        # Parse key=value pairs
        for param in args[1:]:
            if "=" not in param:
                continue
            key, value = param.split("=", 1)

            # Handle string values
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            elif "." in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue

            # Set the attribute
            setattr(new_instance, key, value)

        # Save the new instance
        new_instance.save()
        print(new_instance.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
