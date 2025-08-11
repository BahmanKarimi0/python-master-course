def is_palindrome(word, start=0, end=None):
    if not isinstance(word, str):
        raise TypeError(f'word must be str, got {type(word).__name__}')
    if end is None:
        end = len(word)-1
    if start >= end:
        return True
    if word[start] != word[end]:
        return False
    return is_palindrome(word, start+1, end-1)


print(is_palindrome('hello'))  # False
print(is_palindrome('madam'))  # True
print(is_palindrome('a'))      # True
print(is_palindrome(''))       # True
