def even_numbers_up_to(n):
    for num in range(2, n + 1, 2):
        yield num


gen = even_numbers_up_to(10)
for num in gen:
    print(num)
