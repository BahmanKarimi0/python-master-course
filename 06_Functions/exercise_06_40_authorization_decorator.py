from functools import wraps


def authorize(allowed_users):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] in allowed_users:
                return func(*args, **kwargs)
            else:
                print(f'❌ Access denied for user {args[0]!r}')

        return wrapper

    return decorator


@authorize(allowed_users=["admin", "root"])
def delete_all_data(user):
    print("🚨 All data deleted!")


delete_all_data("root")
