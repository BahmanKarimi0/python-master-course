from functools import wraps


def debug_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)

    return wrapper


@debug_args
def greet(name, age=None):
    print(f'Hello {name}, age {age}')


greet("Alice")
greet("Bob", age=30)
