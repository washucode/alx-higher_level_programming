#!/usr/bin/python3

"""Unittests for square.py"""

from unittest.mock import patch
from unittest import TestCase
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(TestCase):
    """ Square class tests"""

    def setUp(self):
        """ Resets nb_objects to 0 """
        Base._Base__nb_objects = 0

    def is_subclass(self):
        """ Test if Square is subclass of Base """
        self.assertTrue(issubclass(Square, Base))

    def test_is_rectangle_subclass(self):
        """ Test if Square is subclass of Rectangle """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square(self):
        """ tests new square """
        new = Square(1)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)

    def test_square2(self):
        """ Test squares with custom values """
        new2 = Square(1, 2, 3, 4)
        self.assertEqual(new2.id, 4)
        self.assertEqual(new2.size, 1)
        self.assertEqual(new2.x, 2)
        self.assertEqual(new2.y, 3)

    def test_square3(self):
        """ Test squares with same values """
        new3 = Square(1, 1, 1, 1)
        new4 = Square(1, 1, 1, 1)
        self.assertEqual(False, new3 is new4)
        self.assertEqual(False, new3 == new4)

    def test_incorrect_att(self):
        """ Test for size as string """
        with self.assertRaises(TypeError):
            new5 = Square("string")

    def test_incorrect_att3(self):
        """ Test for size as negative """
        with self.assertRaises(ValueError):
            new8 = Square(-1)

    def test_incorrect_att6(self):
        """ Test for size as zero """
        with self.assertRaises(ValueError):
            new11 = Square(0)

    def test_incorrect_att6(self):
        """ Test for size string """
        with self.assertRaises(ValueError):
            new11 = Square(1, "string")

    def test_incorrect_att7(self):
        """ Test for size string """
        with self.assertRaises(ValueError):
            new12 = Square(1, 1, "string")

    def test_incorrect_att8(self):
        """ Test for negative string """
        with self.assertRaises(ValueError):
            new13 = Square(1, -1)

        with self.assertRaises(ValueError):
            new14 = Square(1, 1, -1)

    def test_update(self):
        """ Test update """
        new14 = Square(1, 1, 1, 1)
        new14.update(2, 2, 2, 2)
        self.assertEqual(new14.id, 2)
        self.assertEqual(new14.size, 2)
        self.assertEqual(new14.x, 2)
        self.assertEqual(new14.y, 2)

    def test_update1(self):
        """ Test update with kwargs """
        new15 = Square(1, 1, 1, 1)
        new15.update(size=2, x=2, y=2, id=2)
        self.assertEqual(new15.id, 2)
        self.assertEqual(new15.size, 2)
        self.assertEqual(new15.x, 2)
        self.assertEqual(new15.y, 2)

    def test_update2(self):
        """ Test update with kwargs """
        new16 = Square(1, 1, 1, 1)
        new16.update(size=2, x=2, y=2)
        self.assertEqual(new16.id, 1)
        self.assertEqual(new16.size, 2)
        self.assertEqual(new16.x, 2)
        self.assertEqual(new16.y, 2)

    def incorrect_amt_attrs(self):
        """ Test for incorrect amount of attributes """
        with self.assertRaises(TypeError):
            new17 = Square(1, 1, 1, 1, 1, 1)

    def incorrect_amt_attrs(self):
        """ Test for incorrect amount of attributes """
        with self.assertRaises(TypeError):
            new17 = Square()

    def test_to_dict(self):
        """ Test to_dict """
        new18 = Square(1, 1, 1, 1)
        new18_dict = new18.to_dictionary()
        self.assertEqual(new18_dict, {'id': 1, 'size': 1, 'x': 1, 'y': 1})

    def test_to_dict1(self):
        """ Test to_dict """
        new19 = Square(1, 1, 1, 1)
        new19_dict = new19.to_dictionary()
        self.assertEqual(type(new19_dict), dict)

    def test_access_private_attrs(self):
        """ Test access private attributes """
        new20 = Square(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            new20.__width
        with self.assertRaises(AttributeError):
            new20.__height
        with self.assertRaises(AttributeError):
            new20.__x
        with self.assertRaises(AttributeError):
            new20.__y

    def test_area(self):
        """ Test area """
        new21 = Square(1, 1, 1, 1)
        self.assertEqual(new21.area(), 1)

    def test_area1(self):
        """ Test area """
        new22 = Square(2, 2, 2, 2)
        self.assertEqual(new22.area(), 4)

    def test_display(self):
        """ Test display """
        new23 = Square(1, 1, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            new23.display()
            self.assertEqual(fake_out.getvalue(), '\n #\n')

    def test_display1(self):
        """ Test display """
        new24 = Square(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            new24.display()
            self.assertEqual(fake_out.getvalue(), '\n\n  ##\n  ##\n')

    def test_str(self):
        """ Test __str__ """
        new25 = Square(1, 1, 1, 1)
        self.assertEqual(new25.__str__(), '[Square] (1) 1/1 - 1')

    def test_str1(self):
        """ Test __str__ """
        new26 = Square(2, 2, 2, 2)
        self.assertEqual(new26.__str__(), '[Square] (2) 2/2 - 2')

    def test_str2(self):
        """ Test __str__ """
        new27 = Square(1, 1, 1, 1)
        self.assertEqual(type(new27.__str__()), str)

    def test_json_file(self):
        """ Test json file """
        new28 = Square(1, 1, 1, 1)
        Square.save_to_file([new28])
        with open("Square.json", "r") as file:
            self.assertEqual(json.dumps([new28.to_dictionary()]), file.read())

    def test_create(self):
        """ Test create """
        new29 = Square(1, 1, 1, 1)
        new30 = Square.create(**new29.to_dictionary())
        self.assertEqual(new29.__str__(), new30.__str__())

    def test_load_from_file(self):
        """ Test load from file """
        new31 = Square(1, 1, 1, 1)
        Square.save_to_file([new31])
        new32 = Square.load_from_file()
        self.assertEqual(new31.__str__(), new32[0].__str__())

    def test_save_to_file(self):
        """ Test save to file """
        new33 = Square(1, 1, 1, 1)
        Square.save_to_file([new33])
        with open("Square.json", "r") as file:
            self.assertEqual(json.dumps([new33.to_dictionary()]), file.read())

    def test_save_to_file1(self):
        """ Test save to file """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file2(self):
        """ Test save to file """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
