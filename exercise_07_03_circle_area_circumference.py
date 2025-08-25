import math


class Circle:
    """A circle defined by its radius."""
    def __init__(self, radius: int | float) -> None:
        """Initialize a Circle with a non-negative numeric radius."""
        if not isinstance(radius, (int, float)):
            raise TypeError(f'Expected type int or float, got {type(radius).__name__}')
        if radius < 0:
            raise ValueError(f'Expected radius to be non-negative, got {radius}')
        self.radius = radius

    def area(self) -> float:
        """Return the area of a circle"""
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """Return the circumference (perimeter) of the circle."""
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    circle = Circle(1)
    print(repr(circle.area()))
    print(circle.circumference())
