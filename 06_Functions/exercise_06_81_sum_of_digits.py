def sum_of_digits(num, total=0):
    if not isinstance(num, int):
        raise TypeError('num must be an integer')
    num = abs(num)
    if num == 0:
        return total
    total += num % 10
    return sum_of_digits(num // 10, total)


print(sum_of_digits(12345))   # 15
print(sum_of_digits(-987))    # 24
print(sum_of_digits(0))       # 0

