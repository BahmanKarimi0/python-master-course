while not (string := input('Enter a string: ').strip()):
    print('String cannot be empty.')


def consecutive_unicode_chars(letters):
    for i in range(1, len(letters)):
        if chr(ord(letters[i - 1]) + 1) != letters[i]:
            return False
    return True


print(f'{string!r} consecutive unicode characters: {"✅ Valid" if consecutive_unicode_chars(string) else "❌ Invalid"}')