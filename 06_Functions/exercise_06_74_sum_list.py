def recursive_sum(lst, index=0):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if index == len(lst):
        return 0
    if not isinstance(lst[index], (int, float)):
        raise ValueError("Input must be a number.")
    return lst[index] + recursive_sum(lst, index + 1)


print(recursive_sum([1, 2, 3]))
