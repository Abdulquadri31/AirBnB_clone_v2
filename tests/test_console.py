#!/usr/bin/python3
"""Unittest for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.state import State


class TestHBNBCommandCreate(unittest.TestCase):
    """Test cases for the create command in console.py"""

    def test_create_with_params(self):
        """Test create command with parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            state_id = f.getvalue().strip()
            self.assertTrue(state_id in storage.all())

            obj = storage.all()[f'State.{state_id}']
            self.assertEqual(obj.name, "California")

    def test_create_with_multiple_params(self):
        """Test create command with multiple parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                'create Place city_id="0001" user_id="0001" name="My_little_house" '
                'number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 '
                'latitude=37.773972 longitude=-122.431297'
            )
            place_id = f.getvalue().strip()
            self.assertTrue(place_id in storage.all())

            obj = storage.all()[f'Place.{place_id}']
            self.assertEqual(obj.city_id, "0001")
            self.assertEqual(obj.user_id, "0001")
            self.assertEqual(obj.name, "My little house")
            self.assertEqual(obj.number_rooms, 4)
            self.assertEqual(obj.number_bathrooms, 2)
            self.assertEqual(obj.max_guest, 10)
            self.assertEqual(obj.price_by_night, 300)
            self.assertAlmostEqual(obj.latitude, 37.773972)
            self.assertAlmostEqual(obj.longitude, -122.431297)

    def test_create_with_invalid_class(self):
        """Test create command with an invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create InvalidClass name="Test"')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_with_invalid_params(self):
        """Test create command with invalid parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California" invalid_param')
            state_id = f.getvalue().strip()
            self.assertTrue(state_id in storage.all())

            obj = storage.all()[f'State.{state_id}']
            self.assertEqual(obj.name, "California")
            self.assertFalse(hasattr(obj, "invalid_param"))


if __name__ == "__main__":
    unittest.main()
