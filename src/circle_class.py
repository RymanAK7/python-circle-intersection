class Circle():
    """
    A class representing a circle in a 2D plane.

    Attributes:
    - x (float or int): The x-coordinate of the center of the circle.
    - y (float or int): The y-coordinate of the center of the circle.
    - radius (float or int): The radius of the circle.

    Methods:
    - __init__(x, y, radius): Initializes a new Circle instance.
      Raises a TypeError if the radius, x-coordinate or y-coordinate is not numeric.
      Raises a ValueError if the radius is negative.

    - x: Read-only property for accessing the x-coordinate of the circle's center.
    - y: Read-only property for accessing the y-coordinate of the circle's center.
    - radius: Read-only property for accessing the radius of the circle.

    - __str__(): Human-readable string representation of the circle.

    Example:
    ```
    # Creating a Circle instance
    c1 = Circle(3.0, 5, 7.0)

    # Accessing attributes
    print(c1.x)       # Output: 3.0
    print(c1.y)       # Output: 5
    print(c1.radius)  # Output: 7.0

    # Printing the string representation
    print(c1)         # Output: Circle(x=3.0, y=5.0, radius=7.0)
    ```
    """
    def __init__(self, x, y, radius):
        for property in [x,y,radius]:
            if not isinstance(property,(float,int)):
                raise TypeError("x,y and radius must be of type float or int.")
        if radius < 0:
            raise ValueError("Radius must be on-negative")
        
        self._x = x
        self._y = y
        self._radius = radius
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def radius(self):
        return self._radius
    
    def __str__(self):
        return f"Circle(x={self._x}, y={self._y}, radius={self._radius})"