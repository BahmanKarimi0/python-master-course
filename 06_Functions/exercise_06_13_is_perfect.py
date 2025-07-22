while not (num := input('Enter a number: ')).isdigit():
    print("⚠️  Please enter a positive integer greater than 0.")
number = int(num)


def is_perfect(n):
    sum_ = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum_ += i

    if sum_ == n:
        return True
    return False


print(f'✅ Is perfect? {is_perfect(number)}')

