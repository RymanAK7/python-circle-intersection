from .circle_class import Circle
from typing import Type
from math import inf, sqrt
# from .plotting import circle_plotter


def calculate_distance(c1, c2): return sqrt(
    (c1.x - c2.x)**2 + (c1.y - c2.y)**2)


'''Calculate the distance between the centers of two circles

Parameters:
- c1: Circle, the first circle object
- c2: Circle, the second circle object

Returns:
- float, the distance between the centers of the two circles
'''


def circle_intersections(c1: Type[Circle], c2: Type[Circle]) -> int:
    """
    Determine the number of intersections between two circles.

    Parameters:
    - c1 (Circle): The first circle.
    - c2 (Circle): The second circle.

    Returns:
    int: The number of intersections, where:
        - 0: Circles do not intersect.
        - 1: Circles intersect at exactly one point.
        - 2: Circles intersect at two points.
        - inf: Circles are identical,
        they intersect at infinite number of points.

    Note:
    The function assumes valid Circle objects and calculates intersections
    based on the distances between circle centers and the sum of their radii.
    """
    d = calculate_distance(c1, c2)
    sum_radii = c1.radius + c2.radius
    if sum_radii == d:
        return 1
    elif sum_radii < d:
        return 0
    else:
        if abs(c1.radius - c2.radius) > d:
            return 0
        elif abs(c1.radius - c2.radius) < d:
            return 2
        else:
            if d == 0:
                return inf
            else:
                return 1
