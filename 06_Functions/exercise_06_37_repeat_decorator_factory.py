from functools import wraps


def repeat(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper

    return decorator


@repeat(num_times=3)
def greet(name):
    return(f"Hello {name}")


print(greet("Alice"))
