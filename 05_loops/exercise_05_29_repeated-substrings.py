try:
    while not (string := input("Enter a string: ")).isalpha():
        print('Please enter a valid string containing only alphabetic letters.')
    sub_strings = {}

    i= 0
    while i < len(string):
        j = i + 1
        temp = string[i]
        while j < len(string):
            temp += string[j]
            if len(temp) >= 2:
                sub_strings[temp] = sub_strings.get(temp, 0) + 1
            j += 1
        i += 1
    if sub_strings:
        print('Found repeated substrings:')
        for sub, count in sub_strings.items():
            if count > 1:
                print(f'{sub!r} → {count} times')
    else:
        print('No repeated substrings')
except Exception as e:
    print(e)