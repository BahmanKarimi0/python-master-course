class Car:
    """Class Car"""
    def __init__(self, color, speed=0):
        """Initialize Car"""
        if not isinstance(color, str):
            raise TypeError(f'Expected a string, got {type(color).__name__}')
        if not color:
            raise ValueError(f'Either color or speed must be provided')
        self._color = color
        self.__speed = speed

    def get_speed(self):
        """Get speed"""
        return self.__speed

    def set_speed(self, speed):
        """Set speed"""
        if not isinstance(speed, int):
            raise TypeError(f'Expected an integer, got {type(speed).__name__}')
        if not speed:
            raise ValueError(f'Either color or speed must be provided')
        if speed < 0:
            raise ValueError(f'Speed must be greater than or equal to zero')
        self.__speed = speed


car = Car('red')
car.set_speed(100)
print(car.get_speed())
print(car._color)
print(car._Car__speed)
