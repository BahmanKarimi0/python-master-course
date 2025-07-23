while not (num := input('Enter a number: ')).isdigit():
    print("⚠️  Please enter a positive integer greater than 0.")


def digit_info(numbers):
    sum_digits = 0
    count = 0
    for number in numbers:
        count += 1
        sum_digits += int(number)
    digit_infos = (count, sum_digits)
    return digit_infos


digit_count, total = digit_info(num)
print(f'→ Digit count: {digit_count}')
print(f'→ Sum of digits: {total}')
