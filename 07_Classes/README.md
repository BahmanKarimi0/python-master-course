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
# Exercise 07_05 - Class Creation

## Objective
Learn how to define a simple **class** in Python and create an **object** from it.

## Code
```python
# 07_05_class_creation.py

# Define a simple empty class
class Car:
    pass

# Create an object (instance) of the Car class
car1 = Car()
```
---
# Exercise 07_06 - Multiple Objects

## Objective
Understand how to create multiple **objects** (instances) from the same **class** in Python.

## Code
```python
# 07_06_multiple_objects.py

class Car:
    pass

# Create two objects from the Car class
car1 = Car()
car2 = Car()

# Check their type
print(type(car1))
print(type(car2))
```
---
# Exercise 07_07 - Add Attributes to Class

## Objective
Learn how to add **attributes** to a Python class and initialize them using the constructor (`__init__`).

## Code
```python
# 07_07_add_attributes.py

class Car:
    def __init__(self, brand: str, year: int) -> None:
        # Type validation
        if not isinstance(brand, str):
            raise TypeError(f'Expected a string but got {self.__class__.__name__}')
        if not isinstance(year, int):
            raise TypeError(f'Expected an integer but got {self.__class__.__name__}')
        # Value validation
        if year < 1900 or year > 2100:
            raise ValueError(f'Expected a year between 1900 and 2100 but got {year}')
        self.brand = brand
        self.year = year

# Create a car object
car = Car('Lamborghini', 2000)

# Accessing attributes
print(car.year)
print(car.brand)
```
#### Output:
```python
2000
Lamborghini
```
---
# Exercise 07_08 - Multiple Car Objects with Attributes

## Objective
Practice creating **multiple objects** from the same class in Python and assigning **different attribute values** to each object.

## Exercise
- Define a class `Car` with attributes `brand` and `year`.  
- Create three different objects (`car1`, `car2`, `car3`) with unique brands and years.  
- Print the attributes of each object to verify that they hold different values.

## Key Takeaways
- Each object can have its own unique attribute values even if they are created from the same class.  
- Validating data during object creation ensures robustness.  
- Using `__init__` allows you to initialize object attributes efficiently.

## Output:
```python
BMW - 2021
Mercedes - 2022
Ford - 2023
```
---
# Exercise 07_09 - Object vs Class

## Objective
Understand the difference between a **class** and an **object** in Python.

## Exercise
- Define a class `Car`.  
- Create an object `car` from this class.  
- Verify that `car` is an instance of `Car` using `isinstance()`.  
- Verify that `Car` itself is a class using `isinstance()` with `type`.  

## Key Takeaways
- `isinstance(object, Class)` checks if an object is an instance of a class.  
- Classes themselves are instances of the `type` class in Python.  
- Understanding the difference between objects and classes is fundamental in Python OOP.
---
# Exercise 07_10 - Using the self Keyword

## Objective
Learn how to use the **self** keyword in Python classes to access object attributes within methods.

## Exercise
- Define a class `Car` with an attribute `brand`.  
- Add a method `display_brand` that returns the value of `brand` using `self`.  
- Create an object `car` with a specific brand.  
- Call `display_brand` to access and display the brand of the car.

## Key Takeaways
- `self` refers to the **current object** and is required to access attributes and methods within the class.  
- Always use `self` for instance attributes to differentiate between local variables and object properties.  
- Returning values from methods instead of printing directly allows more flexible use of the data.
---
# Exercise 07_11 - __init__ Constructor with Multiple Attributes

## Objective
Learn how to use the **constructor (`__init__`)** to initialize multiple attributes in a Python class.

## Exercise
- Define a class `Car` with attributes `brand`, `year`, and `color`.  
- Use `__init__` to initialize these attributes.  
- Include type and value validation for each attribute.  
- Implement `__str__` to provide a readable representation of the object.  
- Create an object `car` with specific values and print it.

## Key Takeaways
- `__init__` allows initializing multiple attributes when creating an object.  
- Use type checking and value validation for robust and error-proof classes.  
- Implementing `__str__` provides a clean, human-readable output for objects.
---
