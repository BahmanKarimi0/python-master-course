def accumulator_and_print():
    total = 0
    msg = ''
    try:
        while True:
            num = yield msg
            if not isinstance(num, (int, float)) and num != 'reset':
                msg = f'⚠️ Invalid input: {num!r}'
            elif num == 'reset':
                total = 0
                msg = f'🔄 Total reset to {total}'
            else:
                total += num
                msg = f'📈 Running total: {total}'
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


acc = accumulator_and_print()
next(acc)
print(acc.send(10))
print(acc.send(20))
print(acc.send('reset'))
print(acc.send(5))
print(acc.send('oops'))


