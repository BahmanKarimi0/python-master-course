total = 100


def outer():
    count = 0

    def inner():
        nonlocal count
        global total
        count += 1
        total -= 2
        print(f'Inner Call {count}: count = {count}, total = {total}')
    inner()
    inner()
    inner()


outer()
print(f'Final total = {total}')
