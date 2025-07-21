while not (num := input('Enter a number: ')).isdigit():
    print('⚠️  Please enter positive integers only.')


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(f'Factorial of {num} is {factorial(int(num))}')
