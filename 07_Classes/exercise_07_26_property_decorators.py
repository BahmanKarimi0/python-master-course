class Car:
    """Class Car for show speed"""
    def __init__(self, speed: int | float = 0) -> None:
        """Class car constructor"""
        self.speed = speed

    @property
    def speed(self):
        """Return speed of car"""
        return self.__speed

    @speed.setter
    def speed(self, speed):
        """Set speed of car"""
        if not isinstance(speed, int | float):
            raise TypeError(f'Expected type int or float, got {type(speed).__name__}')
        if speed < 0:
            raise ValueError('Speed cannot be negative')
        self.__speed = speed


car = Car()
print(car.speed)
car.speed = 6
print(car.speed)
try:
    car.speed = -3
    print(car.speed)
except ValueError as e:
    print(f'{e.__class__.__name__}: {e}')
