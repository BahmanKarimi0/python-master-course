"""
Exercise 03‑03 – type(), safe str→int/float conversion, error handling
"""
from typing import Optional
s_int: str = "42"
s_float: str = "3.14159"
s_word: str = "python"

n_int: int = int(s_int)
print(f'"{s_int}"  →  {n_int}        (type: {type(n_int)})')
n_float: float = float(s_float)
print(f'"{s_float}"  →  {n_float}        (type: {type(n_float)})')
try:
    n_word: Optional[int] = int(s_word)
except ValueError:
    n_word: None = None
    print(f'"{s_word}"  →  could not convert, stored {n_word}')

results = [n_int, n_float, n_word]
print("Results list:", results)