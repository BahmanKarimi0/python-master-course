while True:
    nums = input('Enter list of numbers that separated by a space: ').strip().split()
    exist = True
    if nums:
        for num in nums:
            if not num.isdigit():
                print("⚠️  Please enter a integer number rather that 0.")
                exist = False
                break
    else:
        print('⚠️  List cannot be empty.')
        exist = False
    if exist:
        numbers = [int(num) for num in nums]
        break


def find_duplicates(lst):
    duplicat = {}
    for num in lst:
        duplicat[num] = duplicat.get(num, 0) + 1
    return duplicat


duplicate = find_duplicates(numbers)
has_duplicate = False
for number, count in duplicate.items():
    if count > 1:
        print(f'{number}: {count}')
        has_duplicate = True
if not has_duplicate:
    print('List is unique!')
