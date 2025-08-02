from functools import wraps
import inspect


def memoize(func):
    memo = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal memo
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()
        key = tuple(bound_args.arguments.values())
        if key not in memo:
            memo[key] = memo[key[::-1]] = func(*args, **kwargs)
            return memo[key]
        else:
            print(f'✅ Returned cached result for args: {key}')
            return memo[key]

    return wrapper


@memoize
def show_add(a, b):
    print(f"Calculating {a} + {b}...")
    return a + b


print(show_add(1, 2))
print(show_add(2, 1))
