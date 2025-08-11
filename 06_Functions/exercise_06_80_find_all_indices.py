def find_all_indices(word, char, index=0, result=None):
    if not isinstance(word, str):
        raise TypeError(f'word must be str, got {type(word).__name__}')
    if not isinstance(char, str):
        raise TypeError(f'char must be str, got {type(char).__name__}')
    if len(char) > 1:
        raise TypeError(f'char must have length 1, got {len(char)}')
    if result is None:
        result = []
    if index == len(word):
        return result
    if char == word[index]:
        result.append(index)
    return find_all_indices(word, char, index + 1, result)


print(find_all_indices("abracadabra", "a"))
