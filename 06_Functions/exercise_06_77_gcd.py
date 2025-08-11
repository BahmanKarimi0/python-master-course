def gcd(a, b):
    if not isinstance(a, int):
        raise TypeError(f'a must be int, got {type(a).__name__}')
    if not isinstance(b, int):
        raise TypeError(f'b must be int, got {type(b).__name__}')
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(18, 48))
print(gcd(101, 103))
print(gcd(-48, 18))