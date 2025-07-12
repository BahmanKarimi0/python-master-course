"""
Exercise 05‑06 – reversing a number using for or while loop
"""

try:
    while not (num := input('Enter a positive number (e.g. 234): ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 0.")
    reverse_str = ''
    for digit in num:
        reverse_str = digit + reverse_str
        reverse_number = int(reverse_str)
    print(f'Reversed: {reverse_number} (type: {type(reverse_number)})')
except ValueError:
    print('Invalid input!')