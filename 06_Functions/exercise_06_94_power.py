def recursive_power(base, exponent):
    if not isinstance(base, int|float):
        raise TypeError(f'Expected int or float, got {type(base)}')
    if not isinstance(exponent, int):
        raise TypeError(f'Expected int, got {type(exponent)}')
    if exponent < 0:
        raise ValueError(f'Expected positive integer, got {exponent}')

    if exponent == 0:
        if base == 0:
            raise ValueError (f'{base}^0 value is undefined')
        else:
            return 1

    return base * recursive_power(base, exponent - 1)


print(recursive_power(0, 0))