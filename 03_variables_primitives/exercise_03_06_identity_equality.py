"""
Exercise 03‑06 – identity (`is`) vs equality (`==`) and the singleton None
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = None

print(f"a == b  → {a == b}")
print(f"a is b  → {a is b}")
print(f"c == None  → {c == None}")  # Not recommended
print(f"c is None  → {c is None}")  # Recommended
a = b
print(f"a == b  → {a == b}")
print(f"a is b  → {a is b}")
history = [{"step": 3,
            "a_id": id(a),
            "b_id": id(b),
            "a==b": a == b,
            "a is b": a is b}]
print('History:', history)
