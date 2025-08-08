import time


def delayed_sender(delay, target):
    try:
        while True:
            msg = yield
            time.sleep(delay)
            target.send(msg)
    except GeneratorExit:
        target.close()


def sink_printer():
    try:
        while True:
            msg = yield
            print(f'Received: {msg}')
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


sink = sink_printer()
next(sink)

delayed = delayed_sender(1, sink)
next(delayed)

messages = ["first", "second", "third"]
start = time.time()

for msg in messages:
    delayed.send(msg)

end = time.time()
print(f"Total elapsed time: {end - start:.2f} seconds")
