def reverse_string(string, index=0):
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    if index == len(string):
        return ''
    return reverse_string(string, index + 1) + string[index]


print(reverse_string('hello world'))