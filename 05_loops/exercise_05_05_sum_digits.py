"""
Exercise 05‑05 – summing digits of a number using for-loop
"""
try:
    while not (num := input('Enter a number: ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 0.")
    sum_digit = 0
    for i in num:
        sum_digit += int(i)
    print(' + '.join(num) + f' = {sum_digit}')
except ValueError:
    print('Invalid input!')
