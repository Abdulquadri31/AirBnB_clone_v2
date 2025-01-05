#!/usr/bin/python3
"""Unittest for State model with file storage"""

import unittest
import os
from models.state import State
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Test only for file storage")
class TestStateFileStorage(unittest.TestCase):
    """Test cases for State model with file storage"""

    def test_create_state(self):
        """Test that a new State is correctly added to storage"""
        initial_count = len(storage.all(State))

        new_state = State(name="California")
        storage.new(new_state)
        storage.save()

        final_count = len(storage.all(State))

        self.assertEqual(final_count, initial_count + 1)
