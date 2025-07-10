"""
Exercise 05‑01 – counting with a for‑loop and summing integers
"""

try:
    while (num := int(input("Enter a number: "))) < 1:
        print('Please enter integer number rather than 1')
    sum_num = 0
    for i in range(1, num + 1):
        sum_num += i
        print(i, end=" ")
    print()
    print(f'Sum: {sum_num}')

except Exception as e:
    print(f'ERROR: {e}')
