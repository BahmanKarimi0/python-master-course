def can_form_palindrome(string, index=0, count=None, odd_count=0):
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    if count is None:
        count = {}

    if index == len(string):
        return odd_count <= 1

    char = string[index]
    count[char] = count.get(char, 0) + 1

    # بروزرسانی تعداد حروف با تکرار فرد
    if count[char] % 2 == 0:
        odd_count -= 1
    else:
        odd_count += 1

    return can_form_palindrome(string, index + 1, count, odd_count)


# تست‌ها
print(can_form_palindrome("civic"))   # True
print(can_form_palindrome("ivicc"))   # True
print(can_form_palindrome("hello"))   # False
print(can_form_palindrome("racecar")) # True
