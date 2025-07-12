"""
Exercise 05‑10 – Split numbers into even and odd lists and calculate their sums

This program asks the user to enter a positive integer N.
It then iterates from 1 to N (inclusive), separates even and odd numbers
into separate lists, and prints both lists along with the sum of each group.

Example:
    Enter a number: 7
    Even numbers: [2, 4, 6]
    Sum of evens: 12
    Odd numbers: [1, 3, 5, 7]
    Sum of odds: 16
"""

try:
    while not (num_str := input("Enter a number: ").strip()).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    num = int(num_str)
    even_list = []
    odd_list = []
    for i in range(1, num + 1):
        if i & 1 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    even_sum = sum(even_list)
    odd_sum = sum(odd_list)
    print(f'Even numbers: {even_list}')
    print(f'Sum of evens: {even_sum}')
    print()
    print(f'Odd numbers: {odd_list}')
    print(f'Sum of odds: {odd_sum}')
except Exception as e:
    print(f'Error: {e}')
