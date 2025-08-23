def remove_digit(number, digit):
    if not isinstance(number, int):
        raise TypeError(f'Expect in but got {type(number)}')
    if not isinstance(digit, int):
        raise TypeError(f'Expect in but got {type(digit)}')
    if not 0 <= digit <= 9:
        raise ValueError(f'digit must be between 0 and 9')

    negative = number < 0
    number = abs(number)
    if number == 0:
        return 0
    last = number % 10
    rest = remove_digit(number // 10, digit)
    if last == digit:
        return rest
    else:
        return rest * 10 + last if not negative else -(rest * 10 + last)


print(remove_digit(12234334, 2))
