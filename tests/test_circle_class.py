from src.circle_class import Circle
import pytest


def test_circle_creation():
    circle = Circle(0, 0, 5.25)
    assert circle.x == 0
    assert circle.y == 0
    assert circle.radius == 5.25


def test_non_numeric_properties_raises_type_error():
    with pytest.raises(TypeError):
        Circle('1', 2, 3)


def test_negative_radius_raises_value_error():
    with pytest.raises(ValueError):
        Circle(1, 2, -3)


def test_attempt_to_modify_property_raises_attribute_error():
    c1 = Circle(1, 2, 3)
    with pytest.raises(AttributeError):
        c1.x += 1
    with pytest.raises(AttributeError):
        c1.y = 5
    with pytest.raises(AttributeError):
        c1.radius = 3


def test_circle_str_representation():
    circle = Circle(1, 2, 3)
    expected_output = "Circle(x=1, y=2, radius=3)"
    assert str(circle) == expected_output
