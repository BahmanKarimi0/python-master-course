class NonNegative:
    """Descriptor to ensure a numeric attribute is always non-negative."""

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Automatically called to set the attribute name in the owner class.

        Args:
            owner (type): The class where the descriptor is used.
            name (str): The name of the attribute.
        """
        self.name: str = name
        self.owner: type = owner

    def __get__(self, instance: object, owner: type) -> float | int:
        """
        Retrieve the value of the attribute from the instance.

        Args:
            instance (object): The instance from which to get the attribute.
            owner (type): The owner class of the instance.

        Returns:
            float | int: The current value of the attribute.
        """
        return instance.__dict__[self.name]

    def __set__(self, instance: object, value: float | int) -> None:
        """
        Set the value of the attribute, ensuring it is non-negative.

        Args:
            instance (object): The instance to which the attribute belongs.
            value (float | int): The value to assign.

        Raises:
            ValueError: If the value is negative.
        """
        if value < 0:
            raise ValueError(f'{self.name} cannot be negative')
        instance.__dict__[self.name] = value


class Product:
    """Class representing a product with price and quantity."""

    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, price: float | int, quantity: int) -> None:
        """
        Initialize a Product instance.

        Args:
            price (float | int): The price of the product (non-negative).
            quantity (int): The quantity of the product (non-negative).
        """
        self.price = price
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer')
        self.quantity = quantity


if __name__ == '__main__':
    # Example usage
    try:
        p1 = Product(-10, 5)
    except ValueError as e:
        print(e)

    p2 = Product(20.3, 5)
    print(p2.price)     # 20.3
    print(p2.quantity)  # 5
