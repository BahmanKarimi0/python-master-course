def command_generator():
    counter = 0
    while True:
        s = yield f'Message number {counter}'
        if s == 'reset':
            counter = 0
        elif s == 'stop':
            return 'Finish'
        else:
            counter += 1


gen = command_generator()

print(next(gen))
print(gen.send(None))
print(gen.send('reset'))
print(next(gen))
print(gen.send('stop'))
