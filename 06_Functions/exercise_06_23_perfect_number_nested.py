while not (num := input("Enter a number: ")).isdigit():
    print("⚠️  Please enter a positive integer greater than 0.")

number = int(num)


def perfect_number(n):
    divs = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def is_perfect_number(n):
    return sum(perfect_number(n)) == n


print(f'{num!r} is prefect number? {is_perfect_number(number)}')
