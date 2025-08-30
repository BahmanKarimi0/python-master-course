class Car:
    def __init__(self, brand: str, year: int):
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string, got {type(brand).__name__}')
        if not isinstance(year, int):
            raise TypeError(f'Expected an integer, got {type(year).__name__}')
        if year < 1900 or year > 2100:
            raise ValueError(f'Expected a year between 1900 and 2100, got {year}')
        self.brand = brand
        self.year = year

    def __str__(self) -> str:
        return f'{self.brand} - {self.year}'


car1 = Car('BMW', 2021)
car2 = Car('Mercedes', 2022)
car3 = Car('Ford', 2023)

print(car1)
print(car2)
print(car3)
