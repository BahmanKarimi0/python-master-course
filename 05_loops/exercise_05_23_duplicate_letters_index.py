"""
Exercise 05‑23 – Count Duplicate Letters (Case-Insensitive)
"""
try:
    string = input("Enter a string: ")
    letter_count = {}
    for index, letter in enumerate(string.casefold()):
        letter_count[letter] = letter_count.get(letter, [0, []])
        letter_count[letter][0] += 1
        letter_count[letter][1].append(index)
    print('Found repeated letters:')
    found = False
    for letter, (count, index) in letter_count.items():
        if count > 1:
            print(f'Letter {letter!r} appears {count} times at indices: {index}')
            found = True
    if not found:
        print('❌ No repeated letters found.')
except Exception as e:
    print(f'Error: {str(e)}')
