from functools import wraps
from time import perf_counter, sleep


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        time_taken = end_time - start_time
        print(f'Time taken for {func.__name__!r} is {time_taken:.4f} seconds')
        return value

    return wrapper


@timer
def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n -= 1


countdown(5)
