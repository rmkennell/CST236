"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""


def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def get_quadrilateral_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given quadrilateral is square, rectangle

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b adjacent to line a
    :type b: float

    :param c: line c adjacent to line b
    :type c: float

    :param c: line d adjacent to line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"

    if a == b and b == c and c == d:
        return "square"

    if (a == c and b == d) and (a != b):
        return "rectangle"

    else:
        return "quadrilateral"

def get_quadrilateral_point_type(ab=0, bc=0, cd=0, da=0, p_a=0, p_b=0, p_c=0, p_d=0):
    if p_a[0] == p_b[0] and p_c[0] == p_d[0] and p_b[1] == p_c[1] and p_a[1] == p_d[1]:
        if ab == bc and bc == cd and cd == da:
            return "square"

        elif (ab == cd and bc == da) and (ab != bc):
            return "rectangle"

    if p_a[0] != p_b[0] and p_c[0] != p_d[0] and p_b[1] == p_c[1] and p_a[1] == p_d[1]:
        if (p_b[0] - p_a[0]) == (p_c[0] - p_d[0]):
            return "rhombus"

        else:
            return "other quadrilateral"



