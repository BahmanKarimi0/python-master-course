while not (num := input('Enter a number: ')).isdigit():
    print("⚠️  Please enter a positive integer greater than 0.")

num_int = int(num)


def is_happy_number(n, sum_number=None):
    if sum_number is None:
        sum_number = []
    sum_number.append(n)
    if n == 1:
        return True
    sum_ = sum(int(number) ** 2 for number in str(n))
    if sum_ in sum_number:
        return False
    return is_happy_number(sum_, sum_number)


print(f'{num!r} is happy number? {is_happy_number(num_int)}')
