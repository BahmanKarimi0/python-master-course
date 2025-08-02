from functools import wraps
import inspect


def validate_types(**type_hint):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = inspect.signature(func).bind(*args, **kwargs)
            bound_args.apply_defaults()
            is_valid = True
            for param, expected_type in type_hint.items():
                value = bound_args.arguments[param]
                if not isinstance(value, expected_type):
                    print(
                        f'❌ Invalid type for argument "{param}": expected {expected_type.__name__!r}, got {type(value).__name__!r}')
                    is_valid = False
            if is_valid:
                return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_types(name=str, age=int, active=bool)
def register(name, age, active=True):
    print(f"✅ Registered {name}, age {age}, active={active}")


register("Ali", 30, active=True)
register("Sara", "tirty", active=0)
