class Vehicle:
    """The Vehicle class inherits from BaseVehicle"""
    def __init__(self, brand: str) -> None:
        """ Constructor for Vehicle"""
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string, got {type(brand).__name__}')
        self.brand = brand

    def display_info(self) -> str:
        """ Display information about the vehicle"""
        return f'Brand: {self.brand}'


class Car(Vehicle):
    def __init__(self, brand: str, year: int) -> None:
        super().__init__(brand)
        if not isinstance(year, int):
            raise TypeError(f'Expected an integer, got {type(year).__name__}')
        self.year = year

    def display_info(self) -> str:
        return f'Brand: {self.brand}, Year: {self.year}'


car = Car('Ford', 2021)
print(car.display_info())
