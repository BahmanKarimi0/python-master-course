"""
Exercise 05‑19 – Check if Digits Are in Ascending or Descending Order (with loops)
"""
try:
    while not (num := input("Enter a number: ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    is_ascending = True
    is_descending = True
    for i in range(len(num) - 1):
        if num[i] < num[i + 1]:
            is_descending = False
        elif num[i] > num[i + 1]:
            is_ascending = False

    if is_ascending:
        print("✅ The digits are in ascending order.")
    elif is_descending:
        print("✅ The digits are in descending order.")
    else:
        print("❌ The digits are not in a consecutive order.")

except Exception as e:
    print(f'Error: {str(e)}')
