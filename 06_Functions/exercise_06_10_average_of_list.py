try:
    while True:
        num = input('Enter list of number separate with space (e.g. 1 2 3): ').strip().split()

        is_digit = True
        if num:
            for i in num:
                if not i.isdigit():
                    print('⚠️  Please enter positive integers only that separate with space.')
                    is_digit = False
                    break
            if is_digit:
                numbers = [int(i) for i in num]
                break
        else:
            print('⚠️  Numbers cannot be empty.')


    def calculate_average(num_list):
        sum_digits = 0
        counter = 0
        for number in num_list:
            counter += 1
            sum_digits += number
        average = sum_digits / counter
        return average

    print(f'Average = {calculate_average(numbers)}')
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')