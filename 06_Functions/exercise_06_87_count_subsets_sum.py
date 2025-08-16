def count_subsets(lst, target, index=0):
    if not isinstance(lst, list):
        raise TypeError(f'Expected a list, got {type(lst).__name__!r}')
    if index == len(lst):
        return 1 if target == 0 else 0
    include = count_subsets(lst,target - lst[index], index + 1)
    exclude = count_subsets(lst, target, index + 1)
    return include + exclude


print(count_subsets([1, 2, 3, 4, 5], 7))