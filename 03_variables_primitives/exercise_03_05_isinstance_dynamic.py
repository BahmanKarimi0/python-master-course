value = None
history: list[tuple[any, type]] = []
value = '123'
history.append((value, type(value)))
print(f'step 1 → value = {value!r}      ({type(value).__name__})')
try:
    value = int(value)
except ValueError:
    pass
finally:
    history.append((value, type(value)))
    print(f'step 2 → value = {value!r}      ({type(value).__name__})')
value = list(str(value))
history.append((value, type(value)))
print(f'step 3 → value = {value!r}      ({type(value).__name__})')
print('History:', history)
