# Object-Oriented Programming (OOP) in Python — Exercise Series

This repository is a structured journey through **100 OOP exercises in Python**, starting from the simplest fundamentals and gradually moving toward complex, interview-level challenges.  
The goal is to practice and deeply understand Python’s object-oriented features by building from **basic class design** to **advanced topics** like descriptors, metaclasses, and design patterns.

Each exercise:
- Is focused on a specific concept.
- Requires clean, professional, and Pythonic code.
- Must include docstrings in **English**.
- Will be reviewed and refactored if necessary to align with **best practices**.

---

## Exercise 07_01 — Point Basics

**Filename:** `exercise_07_01_point_basics.py`

### Objective
Create a simple yet professional Python class that represents a 2D point.  
This exercise introduces:
- Class construction
- Input validation
- Magic methods (`__init__`, `__repr__`, `__eq__`)

### Requirements
1. Define a class `Point2D`.
2. Attributes: `x` and `y`, both must be of type `int` or `float`.
3. In `__init__`, validate that both arguments are numeric; otherwise raise `TypeError`.
4. Implement `__repr__` so it returns an **unambiguous** string (e.g. `Point2D(x=1, y=2)`).
5. Implement `__eq__` so two points are equal if both `x` and `y` are equal.
6. All docstrings must be written in **English**.

### Acceptance Criteria
- `repr(Point2D(1, 2))` → `"Point2D(x=1, y=2)"`
- `Point2D(1, 2) == Point2D(1, 2)` → `True`
- `Point2D(1, 2) == Point2D(2, 1)` → `False`
- `Point2D("3", 4)` → raises `TypeError`

---
