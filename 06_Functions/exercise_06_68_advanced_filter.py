def advanced_filter(keyword, min_length, target):
    msg_count = 0
    passed_count = 0
    try:
        while True:
            msg = yield
            msg_count += 1
            if not isinstance(msg, str):
                print(f"⚠️ Invalid input type: expected str, got {type(msg).__name__} ({msg!r})")
            elif msg.casefold().find(keyword.casefold()) != -1 and len(msg) > min_length:
                passed_count += 1
                target.send(msg)
    except GeneratorExit:
        print(f'Total messages received: {msg_count}')
        print(f'Messages passed filter: {passed_count}')
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

filterer = advanced_filter('error', 10, log)
next(filterer)


messages = [
    "Error 404",           
    "Critical error found",
    "Warning: Disk full",  
    "Major error detected" 
]

for msg in messages:
    filterer.send(msg)

filterer.close()


