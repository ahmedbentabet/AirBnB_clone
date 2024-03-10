#!/usr/bin/python3
"""
Describes  UserStateReport classes
"""
import models
import unittest
from models.base_model import BaseModel
from models.state import State


class StateTestReport(unittest.TestCase):
    def test_state_initialization(self):
        """Verify the creation of State objects."""
        first_instance = State()
        self.assertEqual(State, type(State()))
        self.assertNotEqual(first_instance.id, State().id)
        self.assertIsInstance(second_instnce, State)

    def test_state_creation_storage(self):
        """Verify the creation and storge of a new State instance."""
        self.assertIn(State(), models.storage.all().values())

    def test_state_name(self):
        """Exmaine the name property of State objects."""
        first_instance = State()
        self.assertIsInstance(first_instnce.name, str)
        self.assertTrue(hasattr(first_instnce, "name"))
        self.assertEqual(first_instance.name, "")
        # Asuming name initializes as an empty string


if __name__ == "__main__":
    unittest.main()
