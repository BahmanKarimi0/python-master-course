while True:
    nums = input("Enter list of number that separate with space: ").strip().split()
    exist = True
    if nums:
        for num in nums:
            if num.isalpha():
                print("⚠️  Please enter a integer number")
                exist = False
                break
    else:
        print('⚠️  list cannot be empty')
        exist = False
    if exist:
        numbers = [int(num) for num in nums]
        break


def positive_average(numbers):
    positive_sum = 0
    count = 0
    for number in numbers:
        if number > 0:
            positive_sum += number
            count += 1
    if count > 0:
        return positive_sum / count
    return None


print(f'Sum of average numbers: {positive_average(numbers)}')
