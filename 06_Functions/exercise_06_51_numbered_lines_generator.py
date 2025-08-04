def numbered_lines(lst):
    for i in range(len(lst)):
        yield f'{i + 1}: {lst[i]}'


lines = ["Hello", "This is a test", "Goodbye"]
gen = numbered_lines(lines)
for line in gen:
    print(line)
