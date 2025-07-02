from django.test import SimpleTestCase
from app import calc

""" Test cases"""


class CalTest(SimpleTestCase):
    """test the cal function"""

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.sub(5, 4)
        self.assertEqual(res, 1)

    def test_divide_numbers(self):
        """test divide numbers"""
        res = calc.divide(6, 3)
        self.assertEqual(res, 2)
