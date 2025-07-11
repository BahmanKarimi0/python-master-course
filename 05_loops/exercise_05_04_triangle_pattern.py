"""
Exercise 05‑04 – triangle pattern using nested for-loop
"""

try:
    while (n := int(input("Enter a positive number: "))) < 1:
        print("⚠️  Please enter a positive integer greater than 0.")
    # for star in range(1, n+1):
    #     space = n - star
    #     print('*' * star + space * " ")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
except ValueError:
    print('Invalid input!')
