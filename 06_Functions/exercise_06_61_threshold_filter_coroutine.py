def filter_above(threshold):
    try:
        msg = ''
        while True:
            temp = yield msg
            if not isinstance(temp, (int, float)):
                msg = f'⚠️ Invalid input: {temp}'
            elif temp > threshold:
                msg = f'✅ Accepted: {temp}'
            else:
                msg = f'❌ Rejected: {temp}'
    except GeneratorExit:
        print('🔒 Coroutine closed gracefully.')


f = filter_above(50)
next(f)
print(f.send(42))
print(f.send(75))
print(f.send('ytsdfg'))
f.close()

