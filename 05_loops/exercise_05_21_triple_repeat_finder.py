try:
    while (string := input('Enter a string: ').strip()).isdigit() or string == '':
        print("⚠️  Please enter a valid string.")
    i = 0
    str_count = []
    while i < len(string):
        j = i + 1
        count = 1
        while j < len(string) and string[i] == string[j]:
            count += 1
            j += 1
        str_count.append((string[i], count, i))
        i = j
    found = False
    for string, count, index in str_count:
        if count == 3:
            found = True
            print(f'Found: character {string!r} repeats {count} times starting at index {index}')
    if not found:
        print("❌ No character repeated exactly 3 times in a row.")
except Exception as e:
    print(f'Error: {str(e)}')
