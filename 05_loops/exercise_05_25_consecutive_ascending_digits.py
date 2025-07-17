"""
Exercise 05-25 – Detecting Consecutive Ascending Digits
"""
try:
    while not (num := input("Enter a number: ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    i = 0
    found = False
    number = ''
    while i < len(num) - 2:
        j = i + 1
        number = num[i]
        while j < len(num) and int(num[j-1]) + 1 == int(num[j]):
            number += num[j]
            j += 1
        if len(number) >= 3:
            found = True
            break
        i += 1
    if found:
        print(f'✅ Found ascending number: {number}')
    else:
        print('❌ No ascending digits were found.')

except Exception as e:
    print(f'Error: {(e)}')
