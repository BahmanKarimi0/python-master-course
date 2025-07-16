"""
Exercise 05‑22 – Shifted Characters Using Unicode
"""
try:
    string = input("Enter a string: ")
    shifted_string = ''
    for letter in string:
        shifted_string += chr(ord(letter) + 1)

    print(f'Shifted string: {shifted_string}')
except Exception as e:
    print(f'Error: {str(e)}')
