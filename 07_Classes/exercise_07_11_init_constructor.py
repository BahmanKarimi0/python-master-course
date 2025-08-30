class Car:
    def __init__(self, brand: str, year: int, color: str) -> None:
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string for brand, got {type(brand).__name__}')
        if not isinstance(year, int):
            raise TypeError(f'Expected an integer for year, got {type(year).__name__}')
        if not isinstance(color, str):
            raise TypeError(f'Expected a string for color, got {type(color).__name__}')
        if not year > 1900 or year < 2100:
            raise ValueError(f'Year must be between 1900 and 2100, got {year}')
        self.brand = brand
        self.year = year
        self.color = color

    def __str__(self) -> str:
        return f'Car brand: {self.brand}, year: {self.year}, color: {self.color}'


car = Car('BMW', 2025, color='blue')
print(car)
