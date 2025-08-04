while True:
    range_input = input('Enter start, end, step: ').strip().split(',')
    found = True
    if range_input:
        for num in range_input:
            if num.isalpha():
                print('Please enter integer number.')
                found = False
                break
    else:
        print('\'Start\' and \'End\' range cannot be empty.')
    if found:
        if len(range_input) == 3:
            start, end, step = range_input
            if start > end and int(step) > 0 and step != '0':
                break
            else:
                print('\'Start\' must be greater than \'End\' and \'Step\' must be greater than 0.')
        elif len(range_input) == 2:
            start, end = range_input
            step = 1
            if start > end:
                break
            else:
                print('\'Start\' must be greater than \'End\'.')
        else:
            print('Please enter \'Start\' and \'End\' range numbers.')


def reverse_range(start, end, step=1):
    start = int(start)
    end = int(end)
    step = int(step)
    while start > end:
        yield start
        start -= step


gen = reverse_range(start, end, step)
for num in gen:
    print(num)
