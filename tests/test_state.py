#!/usr/bin/python3
"""Unittest for State model with database storage"""

import unittest
import MySQLdb
import os
from models.state import State
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Test only for DB storage")
class TestStateDB(unittest.TestCase):
    """Test cases for State model with MySQL database"""

    def setUp(self):
        """Set up a connection to the test database"""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close the database connection"""
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        """Test that a new State is correctly added to the database"""
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        new_state = State(name="California")
        storage.new(new_state)
        storage.save()

        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        self.assertEqual(final_count, initial_count + 1)
