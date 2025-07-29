from functools import wraps


def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs).upper()
        return value

    return wrapper


def add_exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs) + '!'
        return value

    return wrapper


@add_exclamation
@uppercase
def say_hello(name):
    return f'Hello {name}'


print(say_hello('Alice'))
