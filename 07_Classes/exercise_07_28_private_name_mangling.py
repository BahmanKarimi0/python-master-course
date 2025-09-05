class Car:
    """Class Car"""
    def __init__(self, number):
        """Class constructor"""
        if not isinstance(number, int):
            raise TypeError(f'Expected an int, got {type(number).__name__}')
        if number < 0:
            raise ValueError(f'Expected a non-negative number, got {number}')
        self.__engine_number = number

    def get_engine_number(self):
        """Returns the engine number"""
        return self.__engine_number


if __name__ == '__main__':
    car = Car(341252)
    print(car.get_engine_number())
    print(car._Car__engine_number)
    print(car.__engine_number)