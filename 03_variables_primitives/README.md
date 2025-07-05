## 03 – Variables & Primitive Data Types

In this chapter we lay the bedrock for every Python program:

* **Dynamic variables** – how Python binds names to objects at runtime.
* **Primitive data types** – `int`, `float`, `str`, `bool`, `NoneType` and when to use each one.
* **Basic operators** – arithmetic, comparison and simple casting between types.
* **f‑strings** – Python’s modern, readable way to build formatted text.
* **Type‑introspection** – using `type()`, `isinstance()` and small debugging tricks.

Mastering these tiny building blocks early prevents countless bugs later, so take your time and make sure every concept feels intuitive before moving on.

---
### Exercise 03‑01 – Basic variables & f-string

**Description:**  
Define three variables — a name (`str`), age (`int`), and height (`float`).  
Use an `f-string` to display a sentence like:  
> My name is Ali, I am 25 years old and 1.75 meters tall.

**Goal:**  
Practice defining basic variables, using type annotations, and formatting output with f-strings.

---
### Exercise 03‑02 – Type conversion and basic arithmetic

**Description:**  
Define variables for a person's name (`str`), age in years (`int`), and height in meters (`float`).  
Then compute and store:

- `age_months`: age × 12 as an `int`
- `height_cm`: height × 100 as a `float`, rounded to 1 decimal place

Finally, print:
```python
Ali is 25 years old (300 months).
Ali is 1.75 m tall (175.0 cm).
```

**Goal:**  
Practice type conversion, arithmetic operations, and f‑string formatting.

---
### Exercise 03‑03 – type(), safe str→int/float conversion, error handling

**Description:**  
Convert three string variables to numeric types, handling errors safely.

| input variable | value      | desired conversion | output variable |
|----------------|------------|--------------------|-----------------|
| `s_int`        | `"42"`     | `int()`            | `n_int`         |
| `s_float`      | `"3.14159"`| `float()`          | `n_float`       |
| `s_word`       | `"Python"` | `int()` → *error*  | `n_word = None` |

Print a report like:

```python
'42' → 42 (type: <class 'int'>)
'3.14159' → 3.14159 (type: <class 'float'>)
'Python' → could not convert, stored None
Results list: [42, 3.14159, None]
```

**Goal:**  
• Practise `type()` and `isinstance()`  
• Perform safe `str → int/float` conversions with `try/except`  
• Understand how to handle conversion errors and use `None` as a placeholder.

---
### Exercise 03‑04 – Arithmetic operations, rounding, formatted output

**Description:**  
Given a rectangle with the following values:

- `length = 5.6789` meters
- `width = 2.3456` meters
- `price_per_m2 = 850,000` Rials

Perform the following:

- Compute `area`, `perimeter`, and a `rounded` version of area.
- Compute the `cost` in Rials and in millions (rounded to 2 decimals).
- Compute the side of a square with the same area, and convert it to centimeters with one decimal.
- Print all results using properly formatted output with `f-strings`.

**Sample Output:**
```python
Area : 13.3235 m² (rounded: 13.324 m²)
Perimeter : 16.048998 m
Cost : 11,325,004.8 Rials ≈ 11.32 million Rials
Equivalent square side: 3.65 m (365.2 cm)
```

**Goal:**  
Practice using arithmetic operators, `round()`, formatted floats, and readable output formatting.

---
### Exercise 03‑05 – `isinstance()`, runtime type inspection, dynamic typing

**Description:**  
Track changes in the type and value of a dynamic variable `value` through three transformation steps:

1. Assign a string: `"123"`
2. Try to convert it to integer using `int()`, handle failure with `try/except`
3. Convert to a list of characters using `list(str(...))`

After each step:
- Print the value and its current type
- Append a tuple `(value, type)` to a list called `history`

**Sample Output:**
```python
step 1 → value = '123' (type: str)
step 2 → value = 123 (type: int)
step 3 → value = ['1', '2', '3'] (type: list)
History: [('123', <class 'str'>), (123, <class 'int'>), (['1', '2', '3'], <class 'list'>)]

```

**Goal:**  
• Understand Python's dynamic typing  
• Use `type()` and `isinstance()` effectively  
• Track runtime transformations in a readable way

---
