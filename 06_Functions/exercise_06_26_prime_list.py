while True:
    nums = input('Enter list of numbers: ').strip().split()
    exist = True
    if nums:
        for num in nums:
            if num.isalpha():
                print("⚠️  Please enter a integer number")
                exist = False
                break
    else:
        print('⚠️  list cannot be empty')
        exist = False
    if exist:
        numbers = [int(num) for num in nums]
        break


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


prime_number = [num for num in numbers if is_prime(num)]
print(f'Prime numbers: {prime_number}')

