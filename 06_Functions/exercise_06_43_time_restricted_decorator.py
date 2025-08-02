from functools import wraps
from datetime import datetime


def only_during(start_time=8, end_time=18):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.now().hour
            if start_time <= now <= end_time:
                func(*args, **kwargs)
            else:
                print(f'❌ Access denied: only available from {start_time} to {end_time}')
        return wrapper
    return decorator


@only_during(start_time=8, end_time=18)
def access_data():
    print("🔓 Access granted!")


access_data()
