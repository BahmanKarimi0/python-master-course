try:
    while not (num := input('Enter a number:')).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    found = True
    for i in range(1, len(num)):
        if int(num[i]) % 2 == int(num[i - 1]) % 2:
            found = False
            break
    if found:
        print('✅ Digits alternate between odd and even.')
    else:
        print('❌ Digits do not alternate.')
except Exception as e:
    print(f'Error: {str(e)}')
