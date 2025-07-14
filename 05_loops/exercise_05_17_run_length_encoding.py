"""
Exercise 05-17 – Run-Length Encoding of Repeated Digits
"""
try:
    while not (num := input('Enter a number: ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")

    lst = []
    i = 0
    while i < len(num):
        count = 1
        j = i + 1
        while j < len(num) and num[i] == num[j]:
            count += 1
            j += 1
        lst.append((num[i], count))
        i = j
    for num in lst:
        print(num[0] + str(num[1]), end='')
except Exception as e:
    print(f'Error: {e}')

