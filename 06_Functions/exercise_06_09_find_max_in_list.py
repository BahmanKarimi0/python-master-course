try:
    while True:
        num = input("Enter list of number separate with space (e.g. 1 2 3): ").strip().split()
        is_digit = True
        for i in num:
            if not i.isdigit():
                print('⚠️  Please enter positive integers only that separate with space.')
                is_digit = False
                break
        if is_digit:
            num_lst = [int(i) for i in num]
            break


    def find_max(lst):
        max_num = lst[0]
        for i in lst:
            if i > max_num:
                max_num = i
        return max_num


    print(f'Max number is {find_max(num_lst)}')
except Exception as e:
    print(f'Error: {e}')
