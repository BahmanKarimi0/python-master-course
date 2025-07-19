try:
    while not (string := input("Enter a string: ")).isalpha():
        print('Please enter a valid string containing only alphabetic letters.')

    max_substring = ''
    i = 0
    while i < len(string):
        j = i + 1
        temp = string[i]
        while j < len(string) and string[j] not in temp:
            temp += string[j]
            j += 1
        if len(temp) > len(max_substring):
            max_substring = temp
        i += 1
    print(f'✅ Longest substring without repeating characters: {max_substring} (length: {len(max_substring)})')
except Exception as e:
    print(f'Error: {e}')
