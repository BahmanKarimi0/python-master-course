def power(base, exp):
    if not isinstance(base, (int, float)):
        raise TypeError(f'Base must be int or float, got {type(base).__name__}')
    if not isinstance(exp, int):
        raise TypeError(f'Exp must be int, got {type(exp).__name__}')
    if exp < 0:
        raise ValueError(f'Exp must be >= 0, got {exp}')
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


print(power(2, -3))
print(power(2, 0))