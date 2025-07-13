"""
Exercise 05-13 – Most Frequent Digit (with First Appearance Priority)
"""
try:
    while not (num := input("Enter a number(e.g. 1223111): ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    digit_count = {}
    for num in num:
        digit_count[num] = digit_count.get(num, 0) + 1
    max_digit = max(digit_count.items(), key=lambda x: x[1])
    if max_digit[1] > 1:
        print(f'Most frequent digit: {max_digit[0]} ({max_digit[1]} times)')
    else:
        print('No repeated digits found.')
except Exception as e:
    print(str(e))
