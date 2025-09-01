class Car:
    """Class Car"""
    wheels: int = 4

    @classmethod
    def get_wheels(cls) -> int:
        """Return number of wheels"""
        return cls.wheels


car = Car()
print(car.get_wheels())
print(Car.get_wheels())
