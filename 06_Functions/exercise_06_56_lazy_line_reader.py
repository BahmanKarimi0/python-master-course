def lazy_line_reader(lst):
    for line in lst:
        yield line
        if not line:
            break


lines = [
    "User: Alice",
    "Action: Login",
    "Status: Success",
    "",
    "This should not be printed"
]

for line in lazy_line_reader(lines):
    print(line)
