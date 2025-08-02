from functools import wraps


def call_counter(func):
    @wraps(func)
    def wrappers(*args, **kwrags):
        wrappers.count += 1
        func(*args, **kwrags)
        print(f'🧮 Called {func.__name__} {wrappers.count} times')
    wrappers.count = 0
    return wrappers


@call_counter
def greet(name):
    print(f'Hello {name}')


@call_counter
def say_hi(name):
    print(f'Hi {name}')


say_hi('Alice')
say_hi('Jhon')
greet('Bob')

