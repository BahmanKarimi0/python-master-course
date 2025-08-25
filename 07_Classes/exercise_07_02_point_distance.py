from math import hypot


class Point2D:
    """
         A 2D point with numeric x and y coordinates.

         Requirements:
           - x and y must be int or float
           - __repr__ should be unambiguous
           - __eq__ compares component-wise
           - distance_to for distance calculation
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        """Initialize a Point2D, validating numeric inputs."""
        if not isinstance(x, (int, float)):
            raise TypeError(f'Expected int or float, got {type(x).__namne__}')
        if not isinstance(y, (int, float)):
            raise TypeError(f'Expected int or float, got {type(y).__name__}')
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        """Return True if other is a Point2D with equal coordinates."""
        if not isinstance(other, Point2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        """Return an unambiguous string representation."""
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def distance_to(self, other: 'Point2D') -> float:
        """Calculate Euclidean distance to another Point2D."""
        if not isinstance(other, Point2D):
            raise TypeError(f'Expected Point2D, got {type(other).__name__}')
        return hypot(other.y - self.y, other.x - self.x)


if __name__ == '__main__':
    p1 = Point2D(1, 2)
    p2 = Point2D(4, 6)
    print(p1.distance_to(p2))

