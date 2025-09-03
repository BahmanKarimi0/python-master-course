import math


class Vector:
    """Class to represent a vector."""

    def __init__(self, x: (int, float), y: (int, float)) -> None:
        """Constructor for Vector."""
        if not isinstance(x, (int, float)):
            raise TypeError(f'Expected type int or float, got {type(x).__name__}')
        if not isinstance(y, (int, float)):
            raise TypeError(f'Expected type int or float, got {type(y).__name__}')
        self.x = x
        self.y = y

    def __len__(self) -> int:
        """Return the length of the vector."""
        return int(round(math.sqrt(self.x ** 2 + self.y ** 2), 0))

    def __str__(self) -> str:
        """Return a string representation of the vector."""
        return f'{self.__class__.__name__}(x= {self.x}, y= {self.y})'


v = Vector(2, 3)
print(len(v))
print(v)
