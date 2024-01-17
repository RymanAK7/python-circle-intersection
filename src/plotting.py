import matplotlib.pyplot as plt
from circle_class import Circle
from typing import Type, List
import numpy as np


def circle_plotter(circles: List[Type[Circle]]) -> None:
    '''"""
    Plots circles on a 2D plane.

    Parameters:
    - circles (List[Type[Circle]]): A list of Circle objects to be plotted.

    Returns:
    None

    Each circle in the list is plotted on the
    same graph using polar coordinates.
    The function sets the aspect ratio to be
    equal to ensure that the circles are
    visually represented accurately.
    The circles are drawn with different colors,
    and the legend labels indicate the radius of
    each circle.

    Example:
    --------
    circle_plotter([Circle(0, 0, 5), Circle(0, 0, 2)])
    """'''
    colours = ['blue', 'red']
    for index, circle in enumerate(circles):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = circle.radius * np.cos(theta) + circle.x
        y = circle.radius * np.sin(theta) + circle.y
        plt.plot(
            x,
            y,
            color=colours[index],
            label=f'Circle with center\
                ({circle.x},{circle.y}) and radius {circle.radius}')
    plt.axis('equal')
    plt.legend()
    plt.show()


# circle_plotter([Circle(0, 0, 3), Circle(5, 0, 2)])

# circle_plotter([Circle(0, 0, 5), Circle(0, 2, 3)])

# circle_plotter([Circle(0, 0, 3), Circle(0, 0, 3)])

# circle_plotter([Circle(0, -1, 3), Circle(0, 1, 3)])

# circle_plotter([Circle(0, 0, 3), Circle(10, 10, 3)])

# circle_plotter([Circle(0, 0, 4), Circle(0, 0, 1)])
