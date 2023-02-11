#!/usr/bin/python3
"""A unittest file for the base model"""

import unittest
import models
from  models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Sets up the test environment before each test."""
        self.base_model = BaseModel()

    def test_instance(self):
        """Tests if the instance is of the correct type."""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_uuid(self):
        """Tests if the id of the instance is a UUID."""
        self.assertIsInstance(uuid.UUID(self.base_model.id), uuid.UUID)

    def test_created_at(self):
        """Tests if the created_at field is a datetime instance."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Tests if the updated_at field is a datetime instance."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """Tests the save method updates the updated_at field correctly."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method returns a dictionary with the correct keys."""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIn("__class__", obj_dict)

    def test_str(self):
        """Tests the string representation of the BaseModel instance."""
        expected_str = f"{self.base_model}"
        self.assertEqual(str(self.base_model), expected_str)

if __name__ == '__main__':
    unittest.main()
