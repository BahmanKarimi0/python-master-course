"""
Exercise 05-11 – Repeated Digits and Their Positions
"""
try:
    while not (num := input('Enter a number (e.g. 123543421): ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    digit_count = {}
    for index, num in enumerate(num):
        digit_count[num] = digit_count.get(num, [0, []])
        digit_count[num][0] += 1
        digit_count[num][1].append(index)
    repeated_digit_found = False
    print('🔁 Repeated digits found:')
    for key, value in digit_count.items():
        if value[0] > 1:
            print(f' Digit {key!r} occurs again at position{"s" if len(value[1][1:]) > 1 else ""}: {value[1][1:]}')
except Exception as e:
    print(str(e))
