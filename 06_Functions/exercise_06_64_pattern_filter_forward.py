def filter_by_keyword(keyword, target):
        try:
            while True:
                line = yield
                if not isinstance(line, str):
                    print(f'⚠️ Invalid input (not string): {line}')
                elif line.find(keyword) != -1:
                    target.send(line)
        except GeneratorExit:
            target.close()


def logger():
        try:
            while True:
                msg = yield
                print(f"📝 Log: {msg}")
        except GeneratorExit:
            print("📕 Logger closed.")


sink = logger()
next(sink)

fwd = filter_by_keyword(keyword='ERROR', target=sink)
next(fwd)
fwd.send("System started")
fwd.send("ERROR: Disk failure")
fwd.send("User logged in")
fwd.send(123)
fwd.send("ERROR: Overheating")
fwd.close()