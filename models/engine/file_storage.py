#!/usr/bin/python3
"""FileStorage class module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary of objects, optionally filtered by class."""
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
