"""
Exercise 05-14 – Most frequent digits and their indices (sorted descending)
"""
try:
    while not (num := input('Enter positive number (e.g. 123432): ')):
        print("⚠️  Please enter a positive integer greater than 1.")
    digit = {}
    for index, num in enumerate(num):
        digit[num] = digit.get(num, [0, []])
        digit[num][0] += 1
        digit[num][1].append(index)
    sorted_digit = dict(sorted(digit.items(), key=lambda x: x[1][0], reverse=True))
    for digit, (count, index) in sorted_digit.items():
        if count > 1:
            print(f'Digit: {digit} – Count: {count} – Indices: {index}')
except Exception as e:
    print(str(e))