class Car:
    def __init__(self, brand: str, year: int) -> None:
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string but got, {type(brand).__name__}')
        if not isinstance(year, int):
            raise TypeError(f'Expected an integer but got, {type(year).__name__}')
        if year < 1900 or year > 2100:
            raise ValueError(f'Expected a year between 1900 and 2100 but got, {year}')
        self.brand = brand
        self.year = year


car = Car('Lamborghini', 2000.2)
print(car.year)
print(car.brand)
