while True:
    lst_str = input('Enter list of number that separate with space: ').strip().split()
    is_digit = True
    if lst_str:
        for num in lst_str:
            if not num.isdigit():
                print("⚠️  Please enter a positive integer greater than 0.")
                is_digit = False
                break
    else:
        print('⚠️  list cannot be empty.')
        is_digit = False
    if is_digit:
        lst_int = [int(num) for num in lst_str]
        break


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


filter_prime = filter(is_prime, lst_int)
print(list(filter_prime))