try:
    while (text := input('Enter a string: ')).strip() == "":
        print('Please enter a valid string.')
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_count = 0
    non_vowels_count = 0
    vowels_indices = []
    for index, letter in enumerate(text):
        if letter in vowels:
            vowels_count += 1
            vowels_indices.append(index)
        else:
            non_vowels_count += 1
    print(f'Vowel characters: {vowels}')
    print(f'Vowel count: {vowels_count}')
    print(f'Indices of vowels: {vowels_indices}')
    print(f'Non-vowel count: {non_vowels_count}')
except Exception as e:
    print(f'Error: {e}')
