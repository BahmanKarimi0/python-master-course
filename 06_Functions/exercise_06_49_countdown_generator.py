while not (num := input('Enter a number: ')).isdigit():
    print('⚠️ Please enter a positive integer greater than 0.')


numbers = int(num)


def countdown_generator(n):
    for number in range(n, 0, -1):
        yield number


gen = countdown_generator(numbers)
for n in gen:
    print(n)
