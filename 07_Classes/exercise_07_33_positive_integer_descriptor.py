class PositiveInteger:
    """Descriptor to ensure a positive integer."""
    def __set_name__(self, owner: type, name: str) -> None:
        """
               Automatically called to set the attribute name in the owner class.

               Args:
                   owner (type): The class where the descriptor is used.
                   name (str): The name of the attribute.
               """
        self.name = name
        self.owner = owner

    def __get__(self, instance: object, owner: type) -> int:
        """
                Retrieve the value of the attribute from the instance.

                Args:
                    instance (object): The instance from which to get the attribute.
                    owner (type): The owner class of the instance.

                Returns:
                    int: The current value of the attribute.
                """
        return instance.__dict__[self.name]

    def __set__(self, instance: object, value: int) -> None:
        """
                Set the value of the attribute, ensuring it is non-negative.

                Args:
                    instance (object): The instance to which the attribute belongs.
                    value (int): The value to assign.

                Raises:
                    TypeError: If the value is not a integer.
                    ValueError: If the value is negative.
                """
        if not isinstance(value, int):
            raise TypeError(f'Expected an integer, got {type(value).__name__}')
        if value < 0:
            raise ValueError(f'Expected a positive integer, got {value}')
        instance.__dict__[self.name] = value


class Item:
    """Class used to represent an item in a list."""
    stock = PositiveInteger()

    def __init__(self, stock: int):
        """
                Initialize a Item instance.

                Args:
                    stock (int): The number of the items (non-negative).
                """
        self.stock = stock


if __name__ == '__main__':
    item = Item(1)
    print(item.stock)
    try:
        item.stock = -5
    except Exception as e:
        print(e)
    try:
        item2 = Item('sdfg')
    except Exception as e:
        print(e)
