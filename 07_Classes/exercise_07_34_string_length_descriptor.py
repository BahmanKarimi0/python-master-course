class StringLength:
    """Descriptor to ensure a consistent string length."""
    def __init__(self, max_length=10):
        """Initialise the descriptor."""
        if not isinstance(max_length, int):
            raise TypeError(f'Expected an int, got {type(max_length).__name__}')
        if max_length < 0:
            raise ValueError(f'max_length must be greater than or equal to zero')
        self.max_length = max_length

    def __set_name__(self, owner, name):
        """
        Automatically called to set the attribute name in the owner class.

               Args:
                   owner (type): The class where the descriptor is used.
                   name (str): The name of the attribute.
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Retrieve the value of the attribute from the instance.

                Args:
                    instance (object): The instance from which to get the attribute.
                    owner (type): The owner class of the instance.

                Returns:
                    str: The current value of the attribute.
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
                Set the value of the attribute, ensuring it is non-negative.

                Args:
                    instance (object): The instance to which the attribute belongs.
                    value (int): The value to assign.

                Raises:
                    TypeError: If the value is not a stringr.
                    ValueError: If the value is negative.
        """
        if not isinstance(value, str):
            raise TypeError(f'Expected a string, got {type(value).__name__}')
        if self.max_length < len(value) or len(value) < 0:
            raise ValueError(f'Length must be between 0 and {self.max_length}')
        instance.__dict__[self.name] = value


class User:
    """Class representing a user."""
    username = StringLength(max_length=10)

    def __init__(self, username):
        """Initialise the user."""
        self.username = username


if __name__ == '__main__':
    user1 = User('Alex')
    print(user1.username)
    try:
        user2 = User('Tolongusername')
        print(user2.username)
    except Exception as e:
        print(e)
    try:
        user3 = User(123)
    except Exception as e:
        print(e)
