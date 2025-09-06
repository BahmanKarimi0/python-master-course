class Person:
    """Class representing a person."""
    def __init__(self, name, age):
        """Initialise a person."""
        if not isinstance(name, str):
            raise TypeError(f'Expected a string, got {type(name).__name__}')
        if not isinstance(age, int):
            raise TypeError(f'Expected an integer, got {type(age).__name__}')
        if age < 0:
            raise ValueError(f'Expected a positive integer, got {age}')
        self.name = name
        self.age = age

    def display_info(self):
        """Print a person's name, age'"""
        print(f'Name: {self.name}\nAge: {self.age}')


if __name__ == '__main__':
    p = Person('Joe', 25)
    p.display_info()
