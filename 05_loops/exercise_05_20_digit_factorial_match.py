"""
Exercise 05‑20 – Digit Factorial Match (Weird Number)
"""
try:
    while not (num := input("Enter a number: ")).isdigit():
        print("⚠️  Please enter a positive integer greater than 1.")
    fact_list = []
    for i in num:
        fact = 1
        for j in range(1, int(i) + 1):
            fact *= j
        fact_list.append(fact)
    extracted_num = ' + '.join(f'{i}!' for i in num)
    if int(num) == sum(fact_list):
        print(f'✅ {num} is a Weird Number ({extracted_num} = {sum(fact_list)})')
    else:
        print(f'❌ {num} is NOT a Weird Number ({extracted_num} = {sum(fact_list)})')
except Exception as e:
    print(f'Error: {str(e)}')