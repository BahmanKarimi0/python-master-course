def char_stream(lst):
    for words in lst:
        for letter in words:
            yield letter


sentences = ["Hello", "Bye"]
gen = char_stream(sentences)
for word in gen:
    print(word, end=' ')
