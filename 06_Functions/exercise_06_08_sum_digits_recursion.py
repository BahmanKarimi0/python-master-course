try:
    while not (num := input('Enter a number: ')).isdigit():
        print('⚠️  Please enter positive integers only.')


    def sum_digits_recursion(number):
        if not number:
            return 0
        return int(number[0]) + sum_digits_recursion(number[1:])

    print(f'Sum of digits: {sum_digits_recursion(num)}')

except Exception as e:
    print(f'Error: {e}')