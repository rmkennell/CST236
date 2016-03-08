"""
Test for source.shape_checker
"""
from unittest import TestCase

from source.shape_checker import get_quadrilateral_point_type
from source.shape_checker import get_quadrilateral_type
from source.shape_checker import get_triangle_type
from test.plugins.ReqTracer import requirements





class TestGetTriangleType(TestCase):

# 1. Tests that check each type of triangle
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        """

        :return:
        """
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_dictionary(self):
        dict = {'a': 2, 'b': 2, 'c': 2}
        result = get_triangle_type(dict)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(2, 2, 3)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0002'])
    def test_get_triangle_invalid_all_int(self):
        result = get_triangle_type(-1, 2, 3)
        self.assertEqual(result, 'invalid')

    @requirements(['#0002'])
    def test_get_triangle_invalid_char_all_int(self):
        result = get_triangle_type("A", 2, 3)
        self.assertEqual(result, 'invalid')

class TestGetSquareType(TestCase):

    @requirements(['#0003', '#0004'])
    def test_get_quadrilateral_square_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_quadrilateral_square_dictionary(self):
        dict = {'a': 2, 'b': 2, 'c': 2, 'd': 2}
        result = get_quadrilateral_type(dict)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_quadrilateral_invalid(self):
        result = get_quadrilateral_type(3, 'a', 3, 4)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_quadrilateral_rectangle_all_int(self):
        result = get_quadrilateral_type(3, 4, 3, 4)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004'])
    def test_get_quadrilateral_quadrilateral_all_int(self):
        result = get_quadrilateral_type(1, 4, 3, 5)
        self.assertEqual(result, 'quadrilateral')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_square_with_point(self):
        result = get_quadrilateral_point_type(5, 5, 5, 5, [0, 0], [0, 5], [5, 5], [5, 0])
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_rectangle_with_point(self):
        result = get_quadrilateral_point_type(2, 5, 2, 5, [0, 0], [0, 2], [5, 2], [5, 0])
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_rhombus_with_point(self):
        result = get_quadrilateral_point_type(2, 5, 2, 5, [0, 0], [1, 2], [6, 2], [5, 0])
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quadrilateral_other_with_point(self):
        result = get_quadrilateral_point_type(2, 5, 2, 5, [0, 0], [-1, 5], [6, 5], [5, 0])
        self.assertEqual(result, 'other quadrilateral')

