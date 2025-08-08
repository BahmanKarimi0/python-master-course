def filter_by_length(min_length, target):
    try:
        while True:
            word = yield
            if not isinstance(word, str):
                print(f"⚠️ Invalid input type: expected str, got {type(word).__name__} ({word!r})")
            elif len(word) > min_length:
                target.send(word)
    except GeneratorExit:
        target.close()


def to_upper(target):
    try:
        while True:
            word = yield
            target.send(word.upper())
    except GeneratorExit:
        target.close()


def logger():
    try:
        while True:
            word = yield
            print(f'LOG: {word}')
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


log = logger()
next(log)
upper = to_upper(log)
next(upper)
fbl = filter_by_length(5, upper)
next(fbl)
fbl.send("hi")
fbl.send("coroutine")
fbl.send(123)
fbl.send("python")
