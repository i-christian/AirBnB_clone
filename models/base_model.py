#!/usr/bin/python3
"""Base model of the project"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Represent the basemodel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """initialise a new basemodel
        Args:
            *args: unused
            *kwargs: key/value pairs of attributes
        """
        self.id = str(uuid.uuid4())
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Updates the public instance attribute (updated_at) with the current
        datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns a string representation of the basemodel instance"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")
