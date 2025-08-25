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
# Exercise 07_02 — Point Distance

**Filename:** `exercise_07_02_point_distance.py`

## Objective
Extend the `Point2D` class by adding an instance method to compute the **Euclidean distance** to another point.

## Requirements
1. Add a method:
   ```python
   def distance_to(self, other: "Point2D") -> float:
       ...
   ```
### Problem Statement (English)
Implement a method named `distance_to` inside the `Point2D` class that calculates the Euclidean distance between two points in a 2D plane.  
The method should accept another `Point2D` object as an argument and return the distance as a number.

The formula for the Euclidean distance between two points A(x₁, y₁) and B(x₂, y₂) is:

\[
distance = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

---
## Exercise 07-02: Circle Area and Circumference

### Description
Write a Python class called `Circle` that:
1. Initializes with a radius.
2. Has a method `area()` to calculate the area of the circle.
3. Has a method `circumference()` to calculate the circumference of the circle.
4. Raises a `ValueError` if the radius is not positive.

### Example
```python
circle = Circle(5)
print(circle.area())         # 78.54...
print(circle.circumference()) # 31.41...
```
---
# OOP Exercise 07-04 - Rectangle Area and Perimeter

## Task
Write a Python class called **`Rectangle`** that represents a rectangle.  
The class should:

1. Have two attributes: `length` and `width`.
2. Include a constructor (`__init__`) to initialize these attributes.
3. Implement a method **`area()`** that returns the area of the rectangle.
   - Formula (rendered as image):
   ![Area formula](https://latex.codecogs.com/png.latex?A%20%3D%20\text{length}%20\times%20\text{width})
4. Implement a method **`perimeter()`** that returns the perimeter of the rectangle.
   - Formula (rendered as image):
   ![Perimeter formula](https://latex.codecogs.com/png.latex?P%20%3D%202%20\times%20(\text{length}%20+%20\text{width}))

## Example
```python
rect = Rectangle(5, 3)
print("Area:", rect.area())         # Output: 15
print("Perimeter:", rect.perimeter())  # Output: 16
```
---
