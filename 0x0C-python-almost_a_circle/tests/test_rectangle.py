#!/usr/bin/python3

"""Unittests for rectangle.py"""

from unittest.mock import patch
from unittest import TestCase
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """ Rectangle class tests"""

    def setUp(self):
        """ Resets nb_objects to 0 """
        Base._Base__nb_objects = 0

    def is_subclass(self):
        """ Test if Rectangle is subclass of Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle(self):
        """ tests new rectangle """

        new = Rectangle(1, 2)
        self.assertEqual(new.id, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)

    def test_rectangle2(self):
        """ Test triangles with custom values """
        new2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(new2.id, 5)
        self.assertEqual(new2.width, 1)
        self.assertEqual(new2.height, 2)
        self.assertEqual(new2.x, 3)
        self.assertEqual(new2.y, 4)

    def test_rectangle3(self):
        "Test triangles with same values"
        new3 = Rectangle(1, 1, 1, 1)
        new4 = Rectangle(1, 1, 1, 1)
        self.assertEqual(False, new3 is new4)
        self.assertEqual(False, new3 == new4)

    def test_incorrect_att(self):
        """ Test for width as string """
        with self.assertRaises(TypeError):
            new5 = Rectangle("string", 1)

    def test_incorrect_att1(self):
        """ Test for height as string """
        with self.assertRaises(TypeError):
            new6 = Rectangle(1, "string")

    def test_incorrect_att4(self):
        """ Test for width as negative """
        with self.assertRaises(ValueError):
            new9 = Rectangle(-1, 1)

    def test_incorrect_att5(self):
        """ Test for height as negative """
        with self.assertRaises(ValueError):
            new10 = Rectangle(1, -1)

    def test_incorrect_att7(self):
        """ Test for width as zero """
        with self.assertRaises(ValueError):
            new13 = Rectangle(0, 1)

    def test_incorrect_att8(self):
        """ Test for height as zero """
        with self.assertRaises(ValueError):
            new14 = Rectangle(1, 0)

    def test_wrong_amount_of_att(self):
        """ Test for wrong amount of attributes """
        with self.assertRaises(TypeError):
            new17 = Rectangle(1, 1, 1, 1, 1, 1)

    def test_wrong_amount_of_att2(self):
        """ Test for wrong amount of attributes """
        with self.assertRaises(TypeError):
            new18 = Rectangle(1)

    def test_wrong_amount_of_att4(self):
        """ Test for wrong amount of attributes """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_area(self):
        """ Test for area """
        new19 = Rectangle(2, 3)
        self.assertEqual(new19.area(), 6)

    def test_area2(self):
        """ Test for area """
        new20 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(new20.area(), 6)
        new20.width = 10
        self.assertEqual(new20.area(), 30)
        new20.height = 10
        self.assertEqual(new20.area(), 100)
        new20.x = 10
        self.assertEqual(new20.area(), 100)
        new20.y = 10
        self.assertEqual(new20.area(), 100)

    def test_display(self):
        """ Test for display """
        new21 = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            new21.display()
            self.assertEqual(fakeOutput.getvalue(), "##\n##\n##\n")

    def test_display2(self):
        """ Test for display """
        new22 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            new22.display()
            self.assertEqual(fakeOutput.getvalue(), "##\n##\n##\n")
        new22.width = 5
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            new22.display()
            res = "#####\n#####\n#####\n"
            self.assertEqual(fakeOutput.getvalue(), res)

        new22.x = 4
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            new22.display()
            res = "#####\n#####\n#####\n"
            self.assertEqual(fakeOutput.getvalue(), res)
        new22.y = 4
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            new22.display()
            res = "#####\n#####\n#####\n"
            self.assertEqual(fakeOutput.getvalue(), res)

    def test_str(self):
        """ Test for str """
        new23 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(new23.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_str2(self):
        """ Test for str """
        new24 = Rectangle(4, 6, 2, 1)
        self.assertEqual(new24.__str__(), "[Rectangle] (1) 2/1 - 4/6")

    def test_update(self):
        """ Test for update """
        new25 = Rectangle(10, 10, 10, 10)
        new25.update(89)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 10/10 - 10/10") 
        new25.update(89, 2)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        new25.update(89, 2, 3)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        new25.update(89, 2, 3, 4)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        new25.update(89, 2, 3, 4, 5)
        self.assertEqual(new25.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update2(self):
        """ Test for update """
        new26 = Rectangle(10, 10, 10, 10)
        new26.update(89, 2, 3, 4, 5)
        self.assertEqual(new26.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        new26.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(new26.____str____(), "[Rectangle] (89) 4/5 - 2/3")

    def test_dictionary(self):
        """ Test for dictionary """
        new27 = Rectangle(3, 5, 1, 2, 3)
        res = {'x': 1, 'y': 2, 'id': 3, 'height': 5, 'width': 3}
        self.assertEqual(new27.to_dictionary(), res)

    def test_dictionary2(self):
        """ Test for dictionary """
        new28 = Rectangle(3, 5, 1, 2, 3)
        new28.update(89, 2, 3, 4, 5)
        res = {'x': 4, 'y': 5, 'id': 89, 'height': 3, 'width': 2}
        self.assertEqual(new28.to_dictionary(), res)

    def test_dict_to_json(self):
        """ Test for dictionary to json """
        new27 = Rectangle(3, 5, 1, 2, 3)
        res = new27.to_dictionary()
        self.assertEqual(type(Base.to_json_string([res])), str)

    def test_create(self):
        """ Test for create """
        new27 = Rectangle(3, 5, 1, 2, 3)
        new28 = Rectangle.create(**new27.to_dictionary())
        self.assertEqual(new27.__str__(), new28.__str__())
        self.assertFalse(new27 is new28)
        self.assertFalse(new27 == new28)

    def test_create2(self):
        """ Test for create """
        new27 = Rectangle(3, 5, 1, 2, 3)
        dict1 = new27.to_dictionary()
        new28 = Rectangle.create(**dict1)
        self.assertEqual(new28.id, 3)
        self.assertEqual(new28.width, 3)
        self.assertEqual(new28.height, 5)
        self.assertEqual(new28.x, 1)
        self.assertEqual(new28.y, 2)
        self.assertEqual(new27.__str__(), new28.__str__())
        self.assertFalse(new27 is new28)
        self.assertFalse(new27 == new28)

    def test_load_from_file(self):
        """ Test for load from file """
        new29 = Rectangle(3, 5, 1, 2, 3)
        new30 = Rectangle(4, 6, 2, 3, 4)
        list1 = [new29, new30]
        Rectangle.save_to_file(list1)
        list2 = Rectangle.load_from_file()
        self.assertEqual(list2[0].__str__(), "[Rectangle] (3) 1/2 - 3/5")
        self.assertEqual(list2[1].__str__(), "[Rectangle] (4) 2/3 - 4/6")
        self.assertFalse(list1 is list2)
        self.assertFalse(list1 == list2)

    def test_load_from_file2(self):
        """ Test for load from file """
        new31 = Rectangle(3, 5, 1, 2, 3)
        new32 = Rectangle(4, 6, 2, 3, 4)
        list1 = [new31, new32]
        Rectangle.save_to_file(list1)
        list2 = Rectangle.load_from_file()
        self.assertEqual(type(list2), list)
        self.assertEqual(type(list2[0]), Rectangle)
        self.assertEqual(type(list2[1]), Rectangle)
        self.assertFalse(list1 is list2)
        self.assertFalse(list1 == list2)
