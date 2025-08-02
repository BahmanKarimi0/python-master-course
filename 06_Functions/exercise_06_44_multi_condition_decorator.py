from functools import wraps
from datetime import datetime
import inspect


def access_controlled(allowed_users, start_hour, end_hour, max_calls):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = inspect.signature(func).bind(*args, **kwargs)
            bound_args.apply_defaults()
            user = bound_args.arguments.get('user')
            wrapper.call_count[user] = wrapper.call_count.get(user, 0) + 1
            now = datetime.now().hour
            if user not in allowed_users:
                print(f'❌ Access denied for user {user!r}')
            elif not start_hour <= now <= end_hour:
                print(f'❌ Access denied: available from {start_hour} to {end_hour} only')
            elif wrapper.call_count[user] > max_calls:
                print(f'❌ Max call limit reached for user {user!r}')
            else:
                return func(*args, **kwargs)

        wrapper.call_count = {}
        return wrapper

    return decorator


@access_controlled(allowed_users=["admin", "root"], start_hour=7, end_hour=18, max_calls=2)
def access_dashboard(user):
    print(f"✅ Welcome {user!r}, here is your dashboard")


access_dashboard("admin")
access_dashboard("admin")
access_dashboard("admin")  # ❌ max call admin user
access_dashboard("root")   # ✅ root
access_dashboard("root")
access_dashboard("root")   # ❌ max call root user
access_dashboard("guest")  # ❌
