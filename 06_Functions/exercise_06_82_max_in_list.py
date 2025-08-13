def find_max(lst, index=0, current_max=None):
    if not isinstance(lst, list):
        raise TypeError(f'Expected a list, got {type(lst).__name__!r}')
    if not lst:
        raise ValueError('List cannot be empty')
    if current_max is None:
        current_max = lst[0]
    if index == len(lst):
        return current_max
    if not isinstance(lst[index], (int, float)):
        raise ValueError(f'Expected a int or float number, got {type(lst[index]).__name__!r}')
    if lst[index] > current_max:
        current_max = lst[index]
    return find_max(lst, index + 1, current_max)


print(find_max([3, 9, 23, 12, 5]))  # Output: 12
print(find_max([1]))  # Output: -1
