import math


def perfect_squares(lst):
    for num in lst:
        roots = math.isqrt(num)
        if roots ** 2 == num:
            yield num


nums = [2, 4, 8, 9, 10, 16, 18, 25, 30]
gen = perfect_squares(nums)
for num in gen:
    print(num, end=' ')
