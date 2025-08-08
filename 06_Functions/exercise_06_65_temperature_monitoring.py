def temperature_monitoring():
    sum_temp = 0
    count = 0
    sma = 0
    msg = ''
    try:
        while True:
            temp = yield msg
            if not isinstance(temp, int|float) and temp != 'reset':
                print(f"⚠️ Invalid input type: expected int or float, got {type(temp).__name__} ({temp!r})")

            elif temp == 'reset':
                sum_temp = 0
                count = 0
                msg = f'🔄 SMA values have been reset. Starting fresh from next input.'
            else:
                count += 1
                sum_temp  += temp
                sma = sum_temp / count
                msg = f'SMA: {sma:.2f}'
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


tsma = temperature_monitoring()
next(tsma)
print(tsma.send(10))
print(tsma.send(20))
print(tsma.send(30))
print(tsma.send('reset'))
print(tsma.send(30))
