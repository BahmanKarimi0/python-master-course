"""
Exercise 03‑07 – Truthy/Falsy values and conditional execution
"""

values = [0, 1, -1, "", "Hello", [], [0], None, {}, {"a": 1}, False, True]
for val in values:
    is_truthy = bool(val)
    result = "Will run in if" if is_truthy else "Skipped in if"
    print(f'Value: {val!r:<9}        '
          f'| Type: {type(val).__name__:<9}     '
          f'| bool(): {is_truthy!r:<7}'
          f'  → {result:<9}')
