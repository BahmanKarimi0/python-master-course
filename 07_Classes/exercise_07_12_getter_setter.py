class Car:
    """Class for define car """
    def __init__(self, brand):
        """Constructor for car class"""
        self.brand = brand

    @property
    def brand(self):
        """Getter for brand"""
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Setter for brand"""
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string for brand, got {type(brand).__name__}')
        if brand:
            self._brand = brand
        else:
            raise ValueError('Brand cannot be empty')


car = Car('BMW')
print(car.brand)