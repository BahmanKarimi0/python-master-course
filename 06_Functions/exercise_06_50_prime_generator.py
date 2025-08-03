while True:
    nums = input("Enter a number: ").strip()
    exist = True
    if not nums.isdigit():
        print("⚠️  Please enter a integer number")
        exist = False
    elif nums and int(nums) < 2:
        print('⚠️ Please enter a positive integer greater than 0.')
        exist = False
    if exist:
        numbers = int(nums)
        break


def prime_generator(n):
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            yield i


gen = prime_generator(numbers)
for i in gen:
    print(i)
