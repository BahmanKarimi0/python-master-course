while not ((start := input("Enter a positive number: ")).isdigit() and (
end := input("Enter a positive number: ")).isdigit()):
    print("⚠️  Please enter a integer number rather that 0.")


def prefect_number(start, end):
    prefect_lst = []
    for i in range(int(start), int(end) + 1):
        sum_number = 0
        for j in range(1, int(i / 2) + 1):
            if i % j == 0:
                sum_number += j
        if sum_number == i:
            prefect_lst.append(i)

    return prefect_lst


content = prefect_number(start, end)
if not content:
    print(f'In range {start} to {end}, no prefect number was found.')
else:
    print(f'In range {start} to {end}, prefect number was found: {content}')

