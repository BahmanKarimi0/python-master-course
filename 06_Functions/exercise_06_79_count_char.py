def count_char(word, char, index=0):
    if not isinstance(word, str):
        raise TypeError(f'word must be str, got {type(word).__name__}')
    if not isinstance(char, str):
        raise TypeError(f'char must be str, got {type(char).__name__}')
    if len(char) > 1:
        raise ValueError(f'char must have length 1, got {len(char)}')
    if index == len(word):
        return 0
    return (char == word[index]) + count_char(word, char, index + 1)


print(count_char('bhmnjahytfc','a'))