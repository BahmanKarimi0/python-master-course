def count_digit_occurrences(numbers, digit):
    if not isinstance(numbers, int):
        raise TypeError(f'Expected an int, got {type(numbers)}')
    if not isinstance(digit, int):
        raise TypeError(f'Expected an int, got {type(digit)}')
    if not 0 <= digit <= 9:
        raise ValueError('digit must be between 0 and 9')
    numbers = abs(numbers)
    if numbers == 0:
        return 0
    return (numbers % 10 == digit) + count_digit_occurrences(numbers // 10, digit)


print(count_digit_occurrences(-73373, 3))


