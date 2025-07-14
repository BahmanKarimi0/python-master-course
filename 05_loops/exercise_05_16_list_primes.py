"""
Exercise 05-16 – List all prime numbers up to N
"""
try:
    while not (num := input('Enter a positive number (e.g. 17): ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    number = int(num)
    prime_lst = []
    for i in range(2, number + 1):
        is_prime = True
        if i == 2:
            is_prime = True
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_lst.append(str(i))
    print(f'Prime numbers up to {number}: {", ".join(prime_lst)}')
    print()
except Exception as e:
    print(f'Error: {str(e)}')
