"""
Exercise 05-12 – Digits that occur only once and their indices
"""
try:
    while not (num := input('Enter a number (e.g. 123543421): ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    digit_count = {}
    for index, num in enumerate(num):
        digit_count[num] = digit_count.get(num, [0, []])
        digit_count[num][0] += 1
        digit_count[num][1].append(index)
    print(digit_count)
    print('🔍 Digits that appear only once:')
    for digit, (count, position) in digit_count.items():
        if count == 1:
            print(f" - Digit '{digit}' at index {position[0]}")
except Exception as e:
    print(str(e))
