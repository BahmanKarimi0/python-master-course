"""
Exercise 05-18 – Most Consecutive Repeated Digit
"""
try:
    while not (num := input("Enter a number: ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    list_count = []
    i = 0
    while i < len(num):
        count = 1
        j = i + 1
        while j < len(num) and num[i] == num[j]:
            count += 1
            j += 1
        list_count.append((num[i], count))
        i = j
    max_digit = (max(list_count, key= lambda x: x[1]))
    print(f'Digit {max_digit[0]!r} appears the most consecutively ({max_digit[1]} times).')
except Exception as e:
    print(f'Error: {str(e)}')

