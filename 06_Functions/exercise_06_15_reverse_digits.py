while not (num := input('Enter a number: ')).isdigit():
    print("⚠️  Please enter a positive integer greater than 0.")


def reverse_digit(number):
    return number[::-1]


print(f'Reversed number: {reverse_digit(num)}')
