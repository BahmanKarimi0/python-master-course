class Car:
    """Class representing a car."""
    wheel = 4

    def __init__(self, color: str) -> None:
        """Class Car constructor."""
        if not isinstance(color, str):
            raise TypeError(f'Expected a string, got {type(color).__name__}')
        self.color = color


if __name__ == '__main__':
    try:
        car1 = Car('red')
        car2 = Car('blue')
        print(car1.color)
        print(car2.color)
        print(Car.wheel)
        print(car1.wheel)
        print(car2.wheel)
        car1.wheel = 8
        print(car1.wheel)
        print(car2.wheel)
        car3 = Car(345)
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
