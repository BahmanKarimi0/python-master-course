"""
Exercise 05-15 – Finding repeated characters and their positions in a string
"""
try:
    while (word := input('Enter a string (e.g. Python): ')).strip() == "":
        print("⚠️  Input cannot be empty.")
    words = {}
    for index, letter in enumerate(word):
        words[letter] = words.get(letter, [0, []])
        words[letter][0] += 1
        words[letter][1].append(index)
    for letters, (count, indexes) in words.items():
        if count > 1:
            print(f'Character {letters!r} occurs {count} times at positions: {indexes}')
except Exception as e:
    print(str(e))
