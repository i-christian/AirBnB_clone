#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class that serializes/deserializes instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            to_json = {key: obj.to_dict() for key,
                       obj in FileStorage.__objects.items()}
            f.write(json.dumps(to_json))

    def reload(self):
        """reloads JSON file)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                to_json = json.loads(f.read())
                for key, value in to_json.items():
                    class_name, obj_id = key.split(".")
                    value = eval(class_name)(**value)
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            return
