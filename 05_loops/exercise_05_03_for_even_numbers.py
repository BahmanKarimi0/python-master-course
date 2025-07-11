"""
Exercise 05‑03 – printing even numbers using for and if
"""
try:
    while (num := int(input("Enter a positive number: "))) < 1:
        print("⚠️  Please enter a positive integer greater than 0.")
    even_numbers_count = 0
    for i in range(1, num + 1):
        if i & 1 == 0:  # Or if i % 2 == 0
            even_numbers_count += 1
            print(i, end=" ")
    print()
    print(f'Total even numbers: {even_numbers_count}')
except ValueError:
    print('Invalid input!')
except Exception as e:
    print(e.__class__.__name__)
