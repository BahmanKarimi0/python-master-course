def binary_search(input_list, item, low=None, high=None):
    if not isinstance(input_list, list):
        raise TypeError(f'Expected a list, got {type(input_list).__name__!r}')
    if not input_list:
        raise ValueError('Input list cannot be empty.')
    input_list.sort()
    if low is None and high is None:
        low = 0
        high = len(input_list) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if input_list[mid] == item:
        return mid
    elif item > input_list[mid]:
        return binary_search(input_list, item, mid + 1, high)
    else:
        return binary_search(input_list, item, low, mid - 1)


print(binary_search([1, 3, 5, 7, 9], 9))
print(binary_search([1, 3, 5, 7, 9], 2))
