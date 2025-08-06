def printer():
    try:
        while True:
            msg = yield
            print(f'📥 Received in sink: {msg}')
    except GeneratorExit:
        print('🔚 Printer closed.')


sink = printer()
next(sink)


def filter_and_forward(threshold, target_coroutine):
    try:
        while True:
            temp = yield
            if not isinstance(temp, (int, float)):
                print(f'⚠️ Invalid input: {temp}')
            elif temp > threshold:
                target_coroutine.send(temp)
    except GeneratorExit:
        target_coroutine.close()


stage = filter_and_forward(threshold=10, target_coroutine=sink)
next(stage)
stage.send(5)
stage.send(20)
stage.send('jahfh')
stage.send(12)
