class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError(f'Expected int or float, got {type(x).__name__}')
        if not isinstance(y, (int, float)):
            raise TypeError(f'Expected int or float, got {type(y).__name__}')
        self.x = x
        self.y = y

    def __lt__(self, other: 'Vector') -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(x= {self.x}, y= {self.y})'


v1 = Vector(2, 4)
v2 = Vector(3, 4)
print(v1)
print(v1 < v2)