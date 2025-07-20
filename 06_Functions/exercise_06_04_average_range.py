while True:
    start_str = input('Enter start: ')
    end_str = input('Enter end: ')
    if not (start_str.isdigit() and end_str.isdigit()):
        print('⚠️  Please enter positive integers only.')
        continue
    if int(start_str) > int(end_str):
        print('⚠️  Start must be less than or equal to end.')
        continue
    break


start_int = int(start_str)
end_int = int(end_str)


def average_range(start, end):
    sum_range = 0
    count = 0
    for i in range(start, end + 1):
        sum_range += i
        count += 1
    average = sum_range / count
    return average


print(f'Average of numbers from {start_int} to {end_int} is {average_range(start_int, end_int)}')
