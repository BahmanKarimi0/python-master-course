"""
Exercise 05-08 – Finding indices of zero and non-zero digits using enumerate()
"""
try:
    while not (num := input('Enter a number (e.g. 1100023012): ')).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    zero_Indices_index = []
    non_zero_Indices_index = []
    for index, digit in enumerate(num):
        if digit == '0':
            zero_Indices_index.append(index)
        else:
            non_zero_Indices_index.append(index)
    print(f'Indices of zeros: {zero_Indices_index}\nIndices of non-zero digits: {non_zero_Indices_index}')
except Exception as e:
    print(f'Error: {e}')
