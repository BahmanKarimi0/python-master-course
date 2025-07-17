"""
Exercise 05-24 – Sum of Inner Digits (Excluding First and Last)
"""
try:
    while not (num := input("Enter a number: ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    if len(num) < 3:
        print('Number must have at least 3 digits.')
    else:
        sum_digit = 0
        extract_num = ''
        for i in range(1, len(num) - 1):
            extract_num += num[i]
            sum_digit += int(num[i])
        extracted_num = ' + '.join(f'{i}' for i in extract_num)
        # extracted_num = ' + '.join(num[1:-1]) Recommended
        print(f'Sum: {sum_digit} ({extracted_num})')
except Exception as e:
    print(f'Error: {str(e)}')
