try:
    while not (num := input('Enter a number: ')).isdigit():
        print('⚠️  Please enter positive integers only.')


    def sum_of_evens(number):
        sum_even = 0
        for i in range(1, int(number) + 1):
            if i % 2 == 0:
                sum_even += i
        return sum_even
    print(f'Sum of even numbers from 1 to {num} is {sum_of_evens(num)}')
except Exception as e:
    print(f'Error: {e}')