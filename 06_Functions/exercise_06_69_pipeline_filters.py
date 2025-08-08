def keyword_filter(keyword, target):
    try:
        while True:
            msg = yield
            if msg.casefold().find(keyword.casefold()) != -1:
                target.send(msg)
    except GeneratorExit:
        target.close()


def length_filter(min_length, target):
    try:
        while True:
            msg = yield
            if len(msg) > min_length:
                target.send(msg)
    except GeneratorExit:
        target.close()


def message_logger():
    try:
        while True:
            msg = yield
            print(f'Logged: {msg}')
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


log = message_logger()
next(log)
lf = length_filter(5, log)
next(lf)
kw = keyword_filter('error', lf)
next(kw)

messages = [
    "Error 404",
    "Critical error found",
    "Warning: Disk full",
    "Major error detected"
]

for msg in messages:
    kw.send(msg)
kw.close()
