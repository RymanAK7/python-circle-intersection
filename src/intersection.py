from circle_class import Circle
from typing import Type


def circle_intersections(circle1: Type[Circle], circle2: Type[Circle]) -> int:
    print(f"circle1 : {str(circle1)}")
    print(f"circle2 : {str(circle2)}")


circle1 = Circle(0, 0, 5)
circle2 = Circle(1, 1, 2)
circle_intersections(circle1, circle2)
