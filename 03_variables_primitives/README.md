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
