def input_reciver(target):
    try:
        while True:
            num = yield
            if not isinstance(num, int):
                print(f"⚠️ Invalid input type: expected int, got {type(num).__name__} ({repr(num)})")
            else:
                target.send(num)
    except GeneratorExit:
        print("📥 Input receiver closed.")
        target.close()


def even_filter(target):
    try:
        while True:
            num = yield
            if num % 2 == 0:
                target.send(num)
    except GeneratorExit:
        print("🔍 Even filter closed.")
        target.close()


def sum_accumulator():
    try:
        sum_acc = 0
        while True:
            num = yield
            if num >= 0:
                sum_acc += num
                print(f'Running sum: {sum_acc}')
            else:
                print(f'Negative number received, closing accumulator.')
                print(f'Final sum: {sum_acc}')
                break
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


acc = sum_accumulator()
next(acc)

ef = even_filter(acc)
next(ef)

ir = input_reciver(ef)
next(ir)

data = [2, 6, "oops", -4, 10]

for item in data:
    if isinstance(item, int) and item < 0:
        ir.close()
        break
    else:
        ir.send(item)
