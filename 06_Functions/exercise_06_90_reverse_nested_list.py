def reverse_nested(lst, index=None, result=None):
    if not isinstance(lst, list):
        raise TypeError(f'Expected list to be a list, got {type(lst)}')
    if result is None:
        result = []
    if index is None:
        index = len(lst) - 1
    if index < 0:
        return result
    element = lst[index]
    if isinstance(element, list):
        element = reverse_nested(element)
    result.append(element)
    return reverse_nested(lst, index - 1, result)


lst = [1, [2, 3], [4, [5, 6]], 7]
reverse_nested(lst)
print(reverse_nested(lst))

