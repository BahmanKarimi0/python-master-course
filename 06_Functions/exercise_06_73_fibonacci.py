def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be an integer greater than 0")
    else:
        if n == 0 or n == 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(-10))
