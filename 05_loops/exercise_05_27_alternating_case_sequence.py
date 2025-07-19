try:
    while not (string := input('Enter a string: ')).isalpha():
        print("⚠️  Please enter a string without space.")
    is_alternate = True
    for i in range(1, len(string)):
        if string[i].isupper() == string[i-1].isupper():
            is_alternate = False
            break
    if is_alternate:
        print(f'Input: {string}    → ✅ Alternating case')
    else:
        print(f'Input: {string}     → ❌ Not alternating')
except Exception as e:
    print(f'{e.__class__.__name__}: {str(e)}')