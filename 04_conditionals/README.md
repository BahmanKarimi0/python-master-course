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
