class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError(f'Expected int or float, got {type(x).__name__}')
        if not isinstance(y, (int, float)):
            raise TypeError(f'Expected int or float, got {type(y).__name__}')
        self.x = x
        self.y = y

    def __eq__(self, other: 'Vector') -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.__class__.__name__}(x= {self.x}, y= {self.y})'


if __name__ == '__main__':
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    print(v1 == v2)
    print(v1)
