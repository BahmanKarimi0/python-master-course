while not (num := input("Enter a number: ")).isdigit():
    print("⚠️  Please enter a positive integer greater than 0.")


def is_palindrome(n):
    return n == n[::-1]


print(f'✅ Is palindrome: {is_palindrome(num)}')
