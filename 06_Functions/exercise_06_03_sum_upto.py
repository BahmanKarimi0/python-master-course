"""
Exercise 06-03 – Function that returns a value
"""
while not (num := input('Enter a number: ')).isdigit():
    print('Please enter only positive numbers.')
n = int(num)


def sum_upto(n):
    sum_up = 0
    for i in range(1, n+1):
        sum_up += i
    return sum_up


print(f'Sum from 1 to {n} is {sum_upto(n)}')