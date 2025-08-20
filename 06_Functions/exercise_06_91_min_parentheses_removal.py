def min_parens_removal(string, index=0, open_count=0, remove_count=0):
    if not isinstance(string, str):
        raise TypeError(f'Expected a string, got {type(string)}')
    if index == len(string):
        return open_count + remove_count
    char = string[index]
    if char == '(':
        return min_parens_removal(string, index + 1, open_count + 1, remove_count)
    if char == ')':
        if open_count > 0:
            return min_parens_removal(string, index +1, open_count - 1, remove_count)
        else:
            return min_parens_removal(string, index + 1, open_count, remove_count + 1)
    return min_parens_removal(string, index + 1, open_count, remove_count)


print(min_parens_removal('a(a)a'))