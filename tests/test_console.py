#!/usr/bin/python3
"""Unittests for the console (command interpreter)"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import os
import MySQLdb

class TestConsole(unittest.TestCase):
    """Unit tests for the console"""

    @classmethod
    def setUpClass(cls):
        """Setup for MySQL tests"""
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            cls.db = MySQLdb.connect(
                host=os.getenv("HBNB_MYSQL_HOST"),
                user=os.getenv("HBNB_MYSQL_USER"),
                passwd=os.getenv("HBNB_MYSQL_PWD"),
                db=os.getenv("HBNB_MYSQL_DB")
            )
            cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        """Tear down for MySQL tests"""
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            cls.cursor.close()
            cls.db.close()

    def test_create_state_db(self):
        """Test creating a State in DB storage"""
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            self.skipTest("Test only for DB storage")

        # Get the initial number of states
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        # Execute the create command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')

        # Get the new number of states
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        new_count = self.cursor.fetchone()[0]

        self.assertEqual(new_count, initial_count + 1)

    def test_show_nonexistent_id(self):
        """Test show with a non-existent ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show State 12345')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    # Add more tests here for both file storage and DB storage...

if __name__ == "__main__":
    unittest.main()
