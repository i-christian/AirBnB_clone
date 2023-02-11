#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB  project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict['__class__'] = type(self).__name__
        return obj_dict

    def __str__(self):
        """Returns a string representation of a BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
