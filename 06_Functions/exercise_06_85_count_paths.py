def count_paths(n, m, row, col, memo=None):
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")
    if m < 0:
        raise ValueError("m must be greater than or equal to 0")
    if memo is None:
        memo = {}
    if row >= n or col >= 0:
        return 0
    if row == n - 1 and col == m - 1:
        return 1
    if (row, col) not in memo:
        memo[(row, col)] = count_paths(n, m, row + 1, col, memo) + count_paths(n, m, row, col + 1, memo)
    return memo[(row, col)]


