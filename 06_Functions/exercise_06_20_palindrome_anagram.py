while (string := input('Enter a string: ').strip()) == '':
    print('⚠️  Your string cannot be empty.')


def is_palindrome_anagram(letters):
    counter = 0
    count_letter = {}
    for letter in letters:
        count_letter[letter] = count_letter.get(letter, 0) + 1
    for count in count_letter.values():
        if count % 2 != 0:
            counter += 1
    return not counter > 1


if is_palindrome_anagram(string.lower()):
    print(f'✅ "{string}" can be rearranged into a palindrome.')
else:
    print(f'❌ "{string}" cannot form a palindrome via rearrangement.')
