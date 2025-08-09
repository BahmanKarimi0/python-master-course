def keyword_filter(keyword, target):
    try:
        while True:
            line = yield
            if not isinstance(line, str):
                print(f"⚠️ Invalid input type: expected str, got {type(line).__name__}")
                continue
            if keyword.casefold() in line.casefold():
                target.send(line)
    except GeneratorExit:
        print("📥 Keyword filter closed.")
        target.close()


def length_filter(min_length, target):
    try:
        while True:
            line = yield
            if not isinstance(line, str):
                print(f"⚠️ Invalid input type: expected str, got {type(line).__name__}")
                continue
            if len(line) > min_length:
                target.send(line)
    except GeneratorExit:
        print("📥 Length filter closed.")
        target.close()


def uppercase_transformer(target):
    try:
        while True:
            line = yield
            if not isinstance(line, str):
                print(f"⚠️ Invalid input type: expected str, got {type(line).__name__}")
                continue
            target.send(line.upper())
    except GeneratorExit:
        print("📥 Uppercase transformer closed.")
        target.close()


def logger():
    try:
        while True:
            line = yield
            print(f"LOG: {line}")
    except GeneratorExit:
        print("📥 Logger closed.")



log = logger()
next(log)

upper = uppercase_transformer(log)
next(upper)

length_f = length_filter(10, upper)
next(length_f)

kw_filter = keyword_filter("critical", length_f)
next(kw_filter)

inputs = [
    "This is a critical message",
    "Minor error",
    "CRITICAL disk failure",
    "All good",
    "critical warning issued",
    "Short",
]

for line in inputs:
    kw_filter.send(line)

kw_filter.close()
