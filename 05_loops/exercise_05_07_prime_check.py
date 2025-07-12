"""
Exercise 05‑07 – checking if a number is prime using loop
"""

try:
    while not (num := input("Enter a number greater 1 (e.g. 23): ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    number = int(num)
    is_prime = True
    if number <= 1:
        is_prime = False
    elif number == 2:
        is_prime = True
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        print(f'✅ {number} is a prime number.')
    else:
        print(f'❌ {number} is not a prime number.')
except Exception as e:
    print(f'Error: {e}')