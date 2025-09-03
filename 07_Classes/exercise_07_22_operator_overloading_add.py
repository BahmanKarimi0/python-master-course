class Vector:
    """Class to represent a vector."""
    def __init__(self, x: int | float, y: int | float) -> None:
        """Constructor for Vector."""
        if not isinstance(x, (int, float)):
            raise TypeError(f'Expected type int or float but got {type(x).__name__}')
        if not isinstance(y, (int, float)):
            raise TypeError(f'Expected type int or float but got {type(y).__name__}')
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors together."""
        if not isinstance(other, Vector):
            raise TypeError(f'Expected type {Vector} but got {type(other).__name__}')
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        """Return string representation of Vector."""
        return f'Vector(x= {self.x}, y= {self.y})'


v1 = Vector(2, 2)
v2 = Vector(4, 5)
print(v1 + v2)
