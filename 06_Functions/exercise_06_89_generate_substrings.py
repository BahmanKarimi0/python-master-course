def generate_substrings(strings, start_index=0, end_index=0, result=None):
    if not isinstance(strings, str):
        raise TypeError('strings is not a str')
    if result is None:
        result = []
    if start_index == len(strings):
        return result
    if end_index == len(strings):
        return generate_substrings(strings, start_index + 1, start_index + 1, result)
    result.append(strings[start_index:end_index + 1])
    return generate_substrings(strings, start_index, end_index + 1, result)


print(generate_substrings('hello'))
