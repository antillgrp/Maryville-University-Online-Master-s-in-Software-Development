# THIS HIERARCHY EXAMPLE IS INSPIRED IN ONE OF THE TOPICS FROM THE INTRO TO PROGRAMMING CLASS (GRAPHICS)
# WITH THIS "SHAPE" HIERARCHY I WANTED TO SHOW HOW INHERITANCE IS REPRESENTED IN PYTHON,
# ALSO I SHOW HOW ABSTRACT CLASS AND METHOD OVERRIDING WORKS

#  _________       ____________        _________       _______________       _______________
# |         |     | (Abstract) |      |         |     |               |     |               |
# | Object  | <-- |    Shape   | <--  | Polygon | <-- | Quadrilateral | <-- | Parallelogram | <-- (Continues)
# |_________|     |____________|      |_________|     |_______________|     |_______________|
#
#  ___________       ________
# |           |     |        |
# | Rectangle | <-- | Square |
# |___________|     |________|

from abc import ABC
from typing import Sequence


class Point(object):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distanceToPoint(self, pOther: 'Point') -> float:
        # https://www.mathsisfun.com/algebra/distance-2-points.html
        # https://www.tutorialspoint.com/How-to-perform-square-root-without-using-math-module-in-Python
        return ((self.x - pOther.x) ** 2 + (self.y - pOther.y) ** 2) ** 0.5


class Shape(ABC):
    """a abstract plane figure."""
    pass


class Polygon(Shape):
    """a plane figure with at least three straight sides and angles, and typically five or more."""

    def __init__(self, points: Sequence[Point]):
        if not Polygon.pointsAreValidPolygon(points):
            raise ValueError("Could not create a valid Polygon with points: {}".format(points))
        self.points = points

    @classmethod
    def pointsAreValidPolygon(cls, points):
        # validation see: http://hera.ugr.es/doi/15026760.pdf
        # https://www.academia.edu/4739584/Test_for_Simplicity_of_a_Polygon_in_C
        # https://www.toptal.com/python/computational-geometry-in-python-from-theory-to-implementation
        return len(points) >= 3


class Quadrilateral(Polygon):
    """a four-sided figure."""

    def __init__(self, points):
        # proofs is a polygon
        super().__init__(points)

        # proofs is a quadrilateral
        if len(points) != 4:
            raise ValueError("Could not create a valid Quadrilateral with points: {}".format(points))


class Parallelogram(Quadrilateral):
    """a four-sided plane rectilinear figure with opposite sides parallel."""

    def __init__(self, points):
        # proofs is a quadrilateral
        super().__init__(points)

        # proofs is a parallelogram: prove that opposite sides are congruent or equals
        sides_1_3_diff = points[0].distanceToPoint(points[1]) != points[2].distanceToPoint(points[3])
        sides_2_4_diff = points[1].distanceToPoint(points[2]) != points[3].distanceToPoint(points[0])
        if sides_1_3_diff or sides_2_4_diff:
            raise ValueError("Could not create a valid Parallelogram with points: {}".format(points))


class Rectangle(Parallelogram):
    """a four-sided plane rectilinear figure with opposite sides parallel."""

    def __init__(self, points):
        # proofs is a Parallelogram
        super().__init__(points)

        # proofs is a Rectangle: prove that both diagonal are congruent or equals
        if points[0].distanceToPoint(points[2]) != points[1].distanceToPoint(points[3]):
            raise ValueError("Could not create a valid Rectangle with points: {}".format(points))


class Square(Rectangle):
    """a four-sided plane rectilinear figure with opposite sides parallel."""

    def __init__(self, points):
        # proofs is a Rectangle
        super().__init__(points)

        # proofs is a Square: two consecutive side are congruent or equals
        if points[0].distanceToPoint(points[1]) != points[1].distanceToPoint(points[2]):
            raise ValueError("Could not create a valid Square with points: {}".format(points))
