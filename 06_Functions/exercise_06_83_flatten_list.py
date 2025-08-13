def flatten(nested, index=0, result=None):
    if not isinstance(nested, list):
        raise TypeError(f'Expected a list, got {type(nested).__name__!r}')
    if result is None:
        result = []
    if not nested or index == len(nested):
        return result
    if isinstance(nested[index], list):
        flatten(nested[index], 0, result)
    else:
        result.append(nested[index])
    return flatten(nested, index + 1, result)


print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(flatten([]))  # Output: []
print(flatten([[['a']], ['b', ['c']]]))  # Output: ['a', 'b', 'c']
