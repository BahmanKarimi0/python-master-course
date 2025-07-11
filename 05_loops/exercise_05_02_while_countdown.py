"""
Exercise 05‑02 – countdown using a while loop
"""
try:
    while (num := int(input('Enter a positive number (e.g. 12): '))) < 1:
        print("⚠️  Please enter a positive integer greater than 0.")

    while num > 0:
        print(num)
        num -= 1
    print('🚀 Liftoff!')
except ValueError:
    print('Invalid input!')
except Exception as e:
    print(e.__class__.__name__)