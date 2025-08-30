class Car:
    def __init__(self, brand: str):
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string, got {type(brand).__name__}')
        self.brand = brand

    def display_brand(self) -> str:
        return self.brand


car = Car('BMW')
print(car.display_brand())