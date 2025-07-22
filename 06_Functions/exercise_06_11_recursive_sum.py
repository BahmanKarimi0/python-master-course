try:
    while True:
        nums = input('Enter list of number separate with space (e.g. 1 2 3): ').strip().split()
        is_digit = True
        if nums:
            for num in nums:
                if not num.isdigit():
                    print('⚠️  Please enter positive integers only that separate with space.')
                    is_digit = False
                    break
            if is_digit:
                numbers = [int(num) for num in nums]
                break
        else:
            print('⚠️  Numbers cannot be empty.')


    def recursive_sum(num_list):
        if len(num_list) == 0:
            return 0
        return num_list[0] + recursive_sum(num_list[1:])


    print(f'Sum of digits: {recursive_sum(numbers)}')
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
