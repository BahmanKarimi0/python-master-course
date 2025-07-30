from functools import wraps


def log_status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'--> Starting function {func.__name__}')
        func(*args, **kwargs)
        print(f'<-- Finished function {func.__name__}')

    return wrapper


@log_status
def process_data():
    print("Processing data...")


process_data()