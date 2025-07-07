## 🧠 Chapter 04 – Conditional Statements in Python

This chapter introduces one of the most fundamental tools in programming: **decision-making**.

> Conditions allow your program to **choose different paths** based on input, values, or logic.

### 💡 What You'll Learn:

- Basic structure: `if`, `elif`, `else`
- Combining conditions with logical operators: `and`, `or`, `not`
- Truthy and Falsy values and how Python interprets them
- One-line conditionals using **ternary expressions**
- Nested `if` statements and clean formatting
- Membership (`in`) and identity (`is`) in conditions
- Common pitfalls and syntax mistakes (e.g., `=` vs `==`)
- Real-world mini-projects to test your understanding

---

### 🎯 Goal of this chapter:
By the end of this chapter, you'll be able to write **smart, flexible, and readable code** that reacts intelligently to different situations and data inputs.

Each exercise is carefully designed to build your confidence step-by-step — from basic conditions to more complex decision structures.

> Start slow, think logically, and don’t rush. This chapter is not about speed — it’s about learning to **think like a developer**.

---
### Exercise 04‑01 – Basic `if`/`elif`/`else` with Temperature Units

**Description:**  
This script takes two inputs from the user:
- A temperature (float)
- A unit (`C` for Celsius or `F` for Fahrenheit)

Then it classifies the temperature:

- If unit is Celsius (`C`) and temperature > 30 → prints `"Hot in Celsius!"`
- If unit is Fahrenheit (`F`) and temperature > 86 → prints `"Hot in Fahrenheit!"`
- Otherwise → prints `"Moderate"`
- If the unit is invalid or input is missing → prints an error message

**Sample Input/Output:**
```python
Enter temperature (e.g. 30): 50
Enter units (e.g. 'C' for Centigrade of 'F' for Fahrenheit ): c
Hot in celsius
```
---
### Exercise 04‑02 – Nested and Combined Conditions

**Description:**

A simple access control program that checks:
- Username (must not be empty)
- Age (must be a positive integer)
- Admin status (`yes/no`)

**Rules:**
- If age < 13 → Access denied (too young)
- If age ≥ 13 and admin → Access granted with admin privileges
- If age ≥ 13 and not admin → Access granted
- If any input is invalid → Show appropriate error message

**Sample Run:**
```python
Enter your username (e.g. 'Reza'): Ali
Enter your age (e.g. 30): 14
Are you admin user (e.g. 'yes'/'no'): yes
Access granted with admin privileges
```
---
### Exercise 04‑03 – Ternary Conditional and Input Validation

**Description:**

This program asks the user for their name and prints a welcome message.

- If the name is empty or contains only spaces, it assigns `"Guest"` as default.
- Then it checks the length of the name:
  - If it's longer than 5 characters → prints `"Welcome, long-name user!"`
  - Otherwise → prints `"Welcome!"`

**Python Concepts Used:**
- Ternary conditional expressions
- `if ... else` in a single line
- Input sanitization using `.strip()`

**Sample Run:**
```pyhton
What is your name?
Welcome!

What is your name? Katherine
Welcome, long-name user!
```
---
### Exercise 04‑04 – Boolean Logic with `and`, `or`, `not`

**Description:**

A simple login simulation that checks:
- Username and password (must not be empty)
- Password must be at least 8 characters long
- If the user didn't choose "remember me", they must enter a valid OTP code (6 digits)
- Short-circuit evaluation is used to avoid unnecessary checks

**Login rules:**
- If any of the required inputs are missing → login fails
- If "remember me" is checked → OTP is not required
- If "remember me" is not checked → OTP must be 6-digit number

**Sample Run:**
```python
Enter your username: Ali
Enter your password: 12345678
Remember me? (yes/no): no
Enter your OTP code: 325481
✅ Login successful
```
---
