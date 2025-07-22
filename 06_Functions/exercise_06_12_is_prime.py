while not (num := input('Enter a number: ')).isnumeric():
    print("⚠️  Please enter a positive integer greater than 0.")
number = int(num)


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


print(f'✅ Is prime? {is_prime(number)}')
