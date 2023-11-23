from src.circle_class import Circle
from src.intersection import calculate_distance, circle_intersections
from math import inf


def test_calculate_distance_function():
    c1 = Circle(0, 0, 2)
    c2 = Circle(5, 0, 3)
    assert round(calculate_distance(c1, c2)) == 5

    c3 = Circle(1, 1, 3)
    c4 = Circle(7, 4, 3)
    assert round(calculate_distance(c3, c4), 2) == 6.71


def test_circle_intersection_returns_one_for_externally_tangent_circles():
    c1 = Circle(0, 0, 3)
    c2 = Circle(5, 0, 2)
    assert circle_intersections(c1, c2) == 1


def test_circle_intersection_returns_one_for_internally_tangent_cirlces():
    c1 = Circle(0, 0, 5)
    c2 = Circle(0, 2, 3)
    assert circle_intersections(c1, c2) == 1


def test_circle_intersection_returns_inf_for_identical_circles():
    c1 = Circle(0, 0, 3)
    c2 = Circle(0, 0, 3)
    assert circle_intersections(c1, c2) == inf


def test_circle_intersection_returns_two_for_secant_cirlces():
    c1 = Circle(0, -1, 3)
    c2 = Circle(0, 1, 3)
    assert circle_intersections(c1, c2) == 2


def test_circle_intersection_returns_zero_for_non_intersecting_circles():
    c1 = Circle(0, 0, 3)
    c2 = Circle(10, 10, 3)
    assert circle_intersections(c1, c2) == 0

    c3 = Circle(0, 0, 6)
    c4 = Circle(0, 0, 1)
    assert circle_intersections(c3, c4) == 0
