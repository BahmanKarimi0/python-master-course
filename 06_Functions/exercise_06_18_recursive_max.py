while True:
    nums = input('Enter list of numbers that separate with space: ').strip().split()
    is_digit = True
    if nums:
        for num in nums:
            if not num.isdigit():
                print("⚠️  Please enter a positive integer greater than 0.")
                is_digit = False
                break
    else:
        print('⚠️  list cannot be empty.')
        is_digit = False
    if is_digit:
        lst = [int(num) for num in nums]
        break


def recursive_max(number_list):
    if not number_list:
        return float('-inf')
    if len(number_list) == 1:
        return number_list[0]
    rest_max = recursive_max(number_list[1:])

    if number_list[0] > rest_max:
        return number_list[0]
    return rest_max


print(f'Max value: {recursive_max(lst)}')
