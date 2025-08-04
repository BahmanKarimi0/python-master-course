def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_generator()
for _ in range(15):
    print(next(gen), end=' ')
