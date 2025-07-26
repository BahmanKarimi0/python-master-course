while True:
    nums = input('Enter list of numbers that separate with space: ').strip().split()
    exist = True
    if nums:
        for num in nums:
            if not num.isdigit():
                print("⚠️  Please enter a integer number rather that 0.")
                exist = False
                break
    else:
        print('⚠️  list cannot be empty')
        exist = False
    if exist:
        numbers = [int(num) for num in nums]
        break


def frequency_count(lst):
    count_number = {}
    for num in lst:
        count_number[num] = count_number.get(num, 0) + 1
    return count_number


print(frequency_count(numbers))