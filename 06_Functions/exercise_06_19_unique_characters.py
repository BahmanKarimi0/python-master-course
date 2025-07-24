while (string := input("Enter a string: ")).strip() == '':
    print('⚠️  Your string cannot be empty.')


def is_unique(letters):
    temp = ''
    for letter in letters:
        if letter not in temp:
            temp += letter

    return len(temp) == len(letters)


print(f'Is unique characters: {is_unique(string)}')
