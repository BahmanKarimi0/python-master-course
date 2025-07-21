while not (num := input('Enter a number: ')).isdigit():
    print('⚠️  Please enter positive integers only.')


def sum_of_digits(number):
    digit_sum = 0
    for i in number:
        digit_sum += int(i)
    return digit_sum


print(f'Sum of digits: {sum_of_digits(num)}')
