while (string := input("Enter a string: ").strip()) == '':
    print('String can not be empty!')


def toggle_case(letters):
    swapped = ''
    for letter in letters:
        if letter.isupper():
            swapped += letter.lower()
        elif letter.islower():
            swapped += letter.upper()
        else:
            swapped += letter
    return swapped


print(toggle_case(string))
