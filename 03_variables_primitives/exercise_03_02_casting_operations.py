"""
Exercise 03‑02 – Type conversion and basic arithmetic
"""
name: str = 'Ali'
age: int = 25
height: float = 1.75
age_month: int = age * 12
height_cm: float = height * 100
print(f'{name!r} is {age} years old ({age_month} months).\n{name!r} is {height}m tall ({round(height_cm,1)})cm.')
