Of# Object-Oriented Programming (OOP) in Python — Exercise Series

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
# Exercise 07_12 - Getter and Setter with @property

## Objective
Learn how to implement **getter** and **setter** in Python classes using the `@property` decorator.

## Exercise
- Define a class `Car` with a private attribute `_brand`.  
- Create a **getter** using `@property` to access `_brand`.  
- Create a **setter** using `@brand.setter` to validate and set a new value.  
- Ensure the setter checks that the value is a non-empty string.  
- Create an object `car` and demonstrate setting and getting the `brand`.

## Key Takeaways
- `@property` allows controlled access to private attributes.  
- Setter methods can include validation logic to ensure data integrity.  
- Using private attributes with getter/setter promotes encapsulation in Python OOP.
---
# Exercise 07_13 - Inheritance in Python

## Objective
Learn how to implement **inheritance** and **method overriding** in Python classes.

## Exercise
- Define a parent class `Vehicle` with an attribute `brand` and a method `display_info`.  
- Define a child class `Car` that inherits from `Vehicle` and adds a new attribute `year`.  
- Override the `display_info` method in the child class to display both `brand` and `year`.  
- Create an object of `Car` and call the overridden method.

## Key Takeaways
- Inheritance allows a child class to reuse attributes and methods from a parent class.  
- Method overriding enables customizing behavior in child classes.  
- Proper use of `super()` ensures that the parent class is correctly initialized.
---
# Exercise 07_14 - Polymorphism in Python

## Objective
Understand **polymorphism** and how different classes can share the same interface in Python.

## Exercise
- Create two separate classes: `Car` and `Bike`.  
- Each class must implement a method `display_info`.  
- Write a function that accepts a list of objects (`Car` and `Bike`) and calls `display_info` for each object.  
- Demonstrate **polymorphism** by passing objects of different classes to the same function.

## Key Takeaways
- **Polymorphism** allows different object types to respond to the same method call.  
- **Duck typing** in Python means that "if it looks like a duck and quacks like a duck, it’s a duck."  
- This approach makes code flexible and extensible.
---
# Exercise 07_15 - Abstract Classes in Python

## Objective
Learn how to use **abstract base classes (ABC)** to enforce a common interface for all subclasses.

## Exercise
- Define an abstract base class `Vehicle` that inherits from `abc.ABC`.  
- Inside `Vehicle`, create an abstract method `display_info`.  
- Implement two concrete classes `Car` and `Bike` that inherit from `Vehicle` and override the `display_info` method.  
- Create objects of both classes and call `display_info` for each.

## Key Takeaways
- Abstract classes define a **contract** that subclasses must follow.  
- Abstract methods ensure that all subclasses implement the required methods.  
- This is useful for building scalable and maintainable object-oriented systems.
---
# Exercise 07_16 - Method Overriding with super()

## Objective
Learn how to **override methods** in subclasses while still using the parent class functionality with `super()`.

## Exercise
- Create a base class `Vehicle` with a method `display_info` that prints `"This is vehicle"`.  
- Create a subclass `Car` that overrides `display_info`.  
- Inside `Car.display_info`, first call `super().display_info()`, then print `"This is car"`.  
- Create an instance of `Car` and call `display_info` on it.

## Key Takeaways
- Method overriding allows subclasses to **extend or modify** the behavior of parent class methods.  
- The `super()` function enables calling the parent method before or after adding new logic.  
- Useful when maintaining hierarchical class designs.
---
# Exercise 07_17 - Class Methods (`@classmethod`)

## Objective
Understand how to define and use **class methods** with `@classmethod`.

## Exercise
- Define a class `Car` with a class attribute `wheels = 4`.  
- Implement a class method `get_wheels` that returns the number of wheels.  
- Create an instance of `Car` and call `get_wheels` using both the instance and the class itself.  

## Key Takeaways
- `@classmethod` methods take `cls` as the first parameter, which refers to the class itself.  
- Useful when methods need to **access or modify class-level data**.  
- Class methods can be called from both the class and its instances.
---
## Exercise 07_18 — Static Methods

**Task:**  
- Create a class `Car`.  
- Add a static method `is_motor_vehicle` that always returns `True`.  
- Call the method both from an instance and directly from the class.  

This exercise demonstrates how to use `@staticmethod` in Python OOP.

---
# Exercise 07_19 - Encapsulation in Python

## Objective
Learn about **encapsulation** using private and protected attributes in Python.

## Exercise
- Create a class `Car` with:  
  - A **private attribute** `__speed`.  
  - A **protected attribute** `_color`.  
- Implement methods `get_speed` and `set_speed` with validation.  
- Demonstrate accessing the private attribute via methods and direct access using name mangling.  
- Show that protected attributes can be accessed directly but should be treated with caution.

## Key Takeaways
- Private attributes (`__attribute`) are not directly accessible; Python uses name mangling.  
- Protected attributes (`_attribute`) are a convention to indicate “use with caution.”  
- Getter and setter methods help control access and maintain data integrity.
---
## Exercise 07_20 — Multiple Inheritance

**Task:**  
- Create two base classes:  
  - `Engine` with a method `start_engine` that prints `"Engine started"`.  
  - `Wheels` with a method `rotate_wheels` that prints `"Wheels are rotating"`.  
- Create a `Car` class that inherits from both classes.  
- Instantiate a `Car` object and call both `start_engine` and `rotate_wheels`.  
---
# Exercise 07_21 - Method Resolution Order (MRO)

## Objective
Understand how Python determines which method to call when multiple inheritance is used.

## Exercise
- Define classes `A`, `B(A)`, and `C(A)` each with a `show` method.  
- Define class `D(B, C)` that inherits from both `B` and `C`.  
- Create an instance of `D` and call the `show` method.  
- Print the Method Resolution Order (`D.__mro__`) to see the order Python follows.

## Key Takeaways
- Python uses **C3 Linearization** to determine the MRO.  
- In multiple inheritance, Python searches from left to right in the class definition.  
- The `__mro__` attribute shows the exact order of method resolution.
---
## Exercise 07_22 — Operator Overloading with `__add__`

**Task:**  
Create a class `Vector` with attributes `x` and `y`.  
- Implement the `__add__` method so that adding two vectors (`v1 + v2`) returns a new `Vector` with summed coordinates.  
- Implement the `__str__` method to return a readable string in the format:  


**Example:**  
```python
v1 = Vector(2, 2)  
v2 = Vector(4, 5)  
print(v1 + v2)  
# Output: Vector(x=6, y=7)
```
---
## Exercise 07_23 — Operator Overloading with `__eq__`

**Task:**  
Create a `Vector` class with attributes `x` and `y`.  
- Implement the `__eq__` method so that comparing two vectors with `==` returns `True` if both their `x` and `y` values are equal.  
- Implement the `__str__` method for a readable string representation.  

**Example:**  
```python
v1 = Vector(2, 3)  
v2 = Vector(2, 3)  
v3 = Vector(4, 5)  

print(v1 == v2)  # True  
print(v1 == v3)  # False  
print(v1)        # Vector(x=2, y=3)
```
---
## Exercise 07_24 — Operator Overloading with `__lt__`

**Task:**  
Create a `Vector` class with attributes `x` and `y`.  
- Implement the `__lt__` method so that vectors can be compared using `<`.  
- The comparison rule:  
  1. First compare the sum of `x + y` for both vectors.  
  2. If the sums are equal, compare the `x` values.  
- Implement `__str__` for readable representation.  

**Example:**  
```python
v1 = Vector(2, 5)  
v2 = Vector(3, 4)  

print(v1 < v2)   # False  
print(v2 < v1)   # True  
print(v1)        # Vector(x=2, y=5)
```
---
## Exercise 07_25 — Operator Overloading with `__len__`

**Task:**  
Create a `Vector` class with attributes `x` and `y`.  
- Implement the `__len__` method to return the Euclidean length of the vector as an integer using `len()`.  
- Implement `__str__` for a readable string representation.  

**Example:**  
```python
v = Vector(2, 3)
print(len(v))  # 4
print(v)       # Vector(x=2, y=3)
```
---
## Exercise 07_26 — Property Decorators

**Task:**  
Create a `Car` class with a private attribute `__speed`.  
- Implement a property `speed` with a getter to return the speed.  
- Implement a setter for `speed` that only accepts positive numbers and raises an error for negative values.  
- Test reading and updating the speed, including error handling for invalid values.

**Example:**  
```python
car = Car()
print(car.speed)   # 0
car.speed = 6
print(car.speed)   # 6
car.speed = -3     # ValueError: Speed cannot be negative
```
---
## Exercise 07_27 — Class Attributes vs Instance Attributes

**Task:**  
Create a `Car` class with:  
- A **class attribute** `wheel = 4`  
- An **instance attribute** `color` set during object creation  

Test the following:  
- Access `wheel` through the class and instances.  
- Access `color` for each instance.  
- Change `wheel` on one instance and observe the effect on other instances and the class itself.  
- Use `try/except` to catch invalid types for `color`.

**Example Output:**  
```python
red
blue
4
4
4
8
4
TypeError: Expected a string, got int
```

**Key Takeaways:**  
- Class attributes are shared across all instances unless overridden by an instance.  
- Instance attributes are unique to each object.  
- Using `try/except` allows safe handling of invalid input.
---
### Exercise 07_28 - Private Attribute in the `Car` Class

Create a class called `Car` that receives an `engine_number` in its constructor.  
Follow these requirements:

1. If the value passed is not of type `int`, raise a `TypeError`.  
2. If the value is negative, raise a `ValueError`.  
3. Store the engine number as a **private attribute** (using `__engine_number`).  
4. Implement a method `get_engine_number` that returns the engine number.  
5. In the `main` section:  
   - Create an instance of the class.  
   - Print the engine number using the method.  
   - Access the engine number with `._Car__engine_number`.  
   - Try to access it directly with `. __engine_number` and see the error.
---
# Exercise 07_29: Person Class

## Task
Create a class `Person` with the following requirements:

1. The constructor (`__init__`) should accept two attributes: `name` and `age`.  
2. If `name` is not a string, raise a `TypeError`.  
3. If `age` is not an integer or is negative, raise an appropriate error (`TypeError` or `ValueError`).  
4. Implement a method `display_info` that prints the person’s name and age.  

## File name
`exercise_07_29_person_class.py`

---
# Exercise 07_30: BankAccount Class

## Task
Create a class `BankAccount` with the following requirements:

1. The constructor (`__init__`) should accept two attributes: `owner` and `balance`.  
   - `owner` must be a string.  
   - `balance` must be a non-negative number (int or float).  
2. Implement a method `deposit(amount)` that increases the balance.  
   - Raise a `ValueError` if `amount` is not positive.  
3. Implement a method `withdraw(amount)` that decreases the balance.  
   - Raise a `ValueError` if `amount` is greater than the current balance or not positive.  
4. Implement a method `display_balance()` that prints the current balance with the owner’s name.  

## File name
`exercise_07_30_bank_account.py`

---
# Exercise 07_31: Library Class

## Task
Create a `Library` class with the following requirements:

1. The constructor (`__init__`) should initialize an empty list to store books.  
2. Implement a method `add_book(title)` to add a book to the list.  
   - Raise a `TypeError` if `title` is not a string.  
   - Raise a `ValueError` if `title` is empty or already exists in the library.  
3. Implement a method `remove_book(title)` to remove a book from the list.  
   - Raise a `ValueError` if the book does not exist.  
4. Implement a method `display_books()` to display all books in the library.  

## File name
`exercise_07_31_library_class.py`

---
# Exercise 07_32: Non-Negative Descriptor

## Task
Create a descriptor class `NonNegative` that ensures a numeric attribute is always non-negative.

1. Implement a class `NonNegative` with `__get__` and `__set__` methods.  
   - If a negative value is assigned, raise a `ValueError`.  
2. Create a class `Product` with two attributes using this descriptor:  
   - `price`  
   - `quantity`  
3. In `main`:  
   - Create an instance of `Product`.  
   - Try assigning both valid and invalid (negative) values to `price` and `quantity`.  
   - Verify that negative values raise a `ValueError`.  

## File name
`exercise_07_32_descriptor_nonnegative.py`

---
# Exercise 07_33: PositiveInteger Descriptor

## Task
Create a descriptor class `PositiveInteger` that ensures an attribute only accepts positive integers.

1. Implement a class `PositiveInteger` with `__get__` and `__set__` methods.  
   - Raise a `TypeError` if the value is not an integer.  
   - Raise a `ValueError` if the value is negative.  
2. Create a class `Item` that uses this descriptor for a `stock` attribute.  
3. In `main`:  
   - Create an instance of `Item` with a valid positive integer.  
   - Try assigning negative or non-integer values to `stock` to test the descriptor.  

## File name
`exercise_07_33_positive_integer_descriptor.py`

---
# Exercise 07_34: String Length Descriptor

## Task
Create a **descriptor** called `StringLength` that:

1. Accepts only **string values**; otherwise, raises a `TypeError`.  
2. Ensures that the string length does not exceed a maximum value (default: **10 characters**); otherwise, raises a `ValueError`.  
3. The maximum length should be passed as a parameter when creating the descriptor (e.g., `StringLength(max_length=10)`).  

## Requirements
- Define a class `User` that uses this descriptor for its `username` attribute.  
- In the `main` section:  
  - Create a valid `User` instance and print the `username`.  
  - Attempt to set invalid values (too long string or non-string value) and confirm that the correct exceptions are raised.  
---
# Exercise 07_35: FileManager Context Manager

## Task
Create a context manager class `FileManager` to handle file operations safely.

### Requirements
1. Implement `__enter__` to open the file and return the file object.  
2. Implement `__exit__` to close the file, even if an exception occurs.  
3. Support opening the file in different modes ('r', 'w', 'a', etc.).  

### Usage
```python
with FileManager('text.txt', 'w') as f:
    f.write('Hello World')
```
---
# Exercise 07_36: Timer Context Manager

## Task
Create a context manager class `Timer` that measures the execution time of a code block.

### Requirements
1. Implement `__enter__` to start the timer.  
2. Implement `__exit__` to stop the timer and print the elapsed time in seconds.  
3. Ensure that it works correctly even if an exception occurs inside the block.  
4. Use `time.perf_counter()` for high-precision timing.  

### Usage Example
```python
from time import perf_counter

with Timer():
    for i in range(100000000):
        pass
# Output: Finished in X.XXX seconds
```
---
# Exercise 07_37: Suppress Exception Context Manager

## Task
Create a context manager class `SuppressException` that suppresses any exceptions occurring inside a `with` block.

### Requirements
1. Implement `__enter__` to initialize the context manager.  
2. Implement `__exit__` to suppress exceptions by returning `True`.  
3. Ensure that the program continues execution even if an exception occurs in the block.  

### Usage Example
```python
with SuppressException():
    print(10 / 0)  # This will not raise an exception
print("Program continues execution.")
```
---
# Exercise 07_38: MultiFileManager Context Manager

## Task
Create a context manager class `MultiFileManager` that handles opening multiple files at once.

### Requirements
1. Accept a list of file names and a mode (`'r'`, `'w'`, `'a'`, etc.).  
2. Implement `__enter__` to open all files and return a list of file objects.  
3. Implement `__exit__` to close all files.  
4. Ensure files are properly closed even if an exception occurs inside the `with` block.

### Usage Example
```python
with MultiFileManager(['file1.txt', 'file2.txt', 'file3.txt'], mode='w') as file_list:
    for f in file_list:
        f.write('Hello World')
```
---
## Exercise 07_39: Implement a Context Manager for Appending Text to a File

Create a Context Manager called `AppendFile` that opens a file in `append` mode.  
This Context Manager should allow writing to the file inside the `with` block, and once the block is exited, it should automatically append a given string (e.g., a separator or special marker) to the file.  

### Requirements:
- The constructor (`__init__`) should take the file name and the string to be appended.  
- In the `__enter__` method, the file should be opened in `append` mode and returned to the user.  
- In the `__exit__` method, the file should be closed and the specified string appended to the file.  

### Example:
If the following code is executed:

```python
with AppendFile("test.txt", "----\n") as f:
    f.write("First line\n")
    f.write("Second line\n")
```
---
## Exercise 07_40: Context Manager for Temporary Directory and File

Create a Context Manager called `TempDir` that creates a temporary directory and a temporary file inside it when entering the `with` block, and optionally deletes the directory and its contents when exiting the block.

### Requirements:
- The constructor (`__init__`) should accept the following optional parameters:
  - `dir`: base directory where the temp directory will be created.
  - `dir_prefix`: prefix for the temporary directory name.
  - `file_prefix`: prefix for the temporary file name.
  - `file_suffix`: suffix for the temporary file.
  - `delete`: boolean to indicate whether the directory should be deleted upon exit.
- In the `__enter__` method:
  - Create the temporary directory and file.
  - Return a tuple `(temp_dir_name, temp_file_name)`.
- In the `__exit__` method:
  - If `delete` is True, remove the directory and its contents.

### Example:
```python
with TempDir(delete=False) as (temp_dir, temp_file):
    print("Temporary directory created:", temp_dir)
    with open(temp_file, 'w+') as f:
        f.write("Hello World")
        f.seek(0)
        print(f.read())
```
---
# Exercise 07_41: ExecutionTimer Context Manager

## Task
Create a context manager named `ExecutionTimer` that measures and prints the execution time of a block of code.

## Requirements
- The constructor (`__init__`) should optionally accept a `label: str | None` parameter to identify the measured block.  
- `__enter__` must record the start time (use `time.perf_counter()`) and return the context manager (e.g., `self`).  
- `__exit__` must record the end time, compute the elapsed time, and print it in seconds with **3 decimal places**. If a `label` was provided, include it in the printed message (e.g., `[Label] Finished in 0.123 seconds`).  
- The context manager must behave correctly even if an exception occurs inside the `with` block (i.e., still measure and print elapsed time).

## File name
`exercise_07_41_execution_timer.py`

---
