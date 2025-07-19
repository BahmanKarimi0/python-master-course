try:
    while not (num := input("Enter a number: ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    all_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    missing_digit = set()
    for i in all_num:
        if str(i) not in num:
            missing_digit.add(i)
            count += 1
    if not count:
        print('✅ All digits from 0 to 9 are present.')
    else:
        print(f'{count} digit {missing_digit} are missing from {num}.')
except Exception as e:
    print(f'Error: {e}')