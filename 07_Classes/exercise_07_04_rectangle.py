class Rectangle:
    """A rectangle with a width and height """

    def __init__(self, width: int | float, height: int | float) -> None:
        """Initialize a Rectangle with positive numeric width and height."""
        if not isinstance(width, int | float):
            raise TypeError(f'Expected int or float, got {type(width).__name__}')
        if not isinstance(height, int | float):
            raise TypeError(f'Expected int or float, got {type(height).__name__}')
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and height must be > 0, got width={width}, height={height}")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle """
        return self.width * self.height

    def perimeter(self) -> float:
        """"Return the perimeter of the rectangle """
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(width={self.width}, height={self.height}, area={self.area()}, perimeter={self.perimeter()})'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'


if __name__ == '__main__':
    r = Rectangle(5, 5)
    print(r.area())
    print(r.perimeter())
    print(r)
    print(repr(r))
