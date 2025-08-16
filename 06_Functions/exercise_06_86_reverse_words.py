def reverse_words(words, index=0,current_word='', result=None):
    if not isinstance(words, str):
        raise TypeError('words must be a string')
    if result is None:
        result = []
    if index == len(words):
        if current_word:
            result.insert(0, current_word)
        return " ".join(result)
    if words[index] != ' ':
        current_word += words[index]
    else:
        if current_word:
            result.insert(0, current_word)
            current_word = ''
    return reverse_words(words, index+1, current_word, result)


print(reverse_words("hello world and Python"))
