"""
Exercise 04‑03 – ternary conditional, default values, and input validation
"""

name = input("What is your name? ").strip()
name = name if name else 'Guest'
message = f"Welcome, long-name user" if len(name) > 5 else "Welcome!"
print(message)
