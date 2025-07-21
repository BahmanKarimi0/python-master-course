# 📘 Chapter 06 – Functions in Python

## Overview

In this chapter, we will explore **functions** in Python from the ground up.  
Functions allow you to break your code into reusable, modular blocks, making programs more readable and maintainable.

We will begin with simple function definitions and gradually move toward more advanced concepts such as:

- ✅ Defining and calling functions  
- ✅ Parameters and arguments (positional, keyword, default)  
- ✅ Return values  
- ✅ Variable scope (local vs. global)  
- ✅ Nested functions  
- ✅ Lambda (anonymous) functions  
- ✅ Recursion  
- ✅ Functional programming tools (`map`, `filter`, `reduce`)  
- ✅ Higher-order functions  
- ✅ Closures  
- ✅ Decorators (🔶 Custom & built-in)  
- ✅ Generators and `yield`  
- ✅ Coroutines and `async def`, `await`  
- ✅ Type annotations for functions  
- ✅ Docstrings and documentation standards  
- ✅ Error handling in functions  
- ✅ Practical design tips for real-world projects

> 💡 **Note**: While the plan is to include 30 exercises, we may exceed this number to ensure full mastery of advanced topics like **decorators**, **generators**, and **coroutines** — all of which are essential for intermediate to advanced Python development.

---
## ✅ Exercise 06‑01 – Basic Function Call
### Description
This exercise introduces function basics.
Define a simple function named basic_call() that, when called, prints a greeting message.

**Requirements:**
- Define a function without parameters.
- Inside the function, print: Hello from a function!
- Call the function from the main program.

**Example Output:**
```python
Hello from a function!
```
---
## Exercise 06-02 – Function with Parameters

**Description**  
This exercise introduces the concept of **function parameters** in Python.  
The goal is to define a function that takes a user's name as an argument and prints a personalized greeting.

**Objectives**  
- Learn how to define functions with parameters.
- Understand the separation of input logic from function logic.

**Requirements**  
- Define a function named `greet_user(name)`.
- The function should print a message like:  
  `Hello, Alice! Welcome aboard. 👋`
- Get the user’s name from input **outside the function**, and validate that it’s not empty.

**Example**
```python
Enter your name: Alice
Hello, Alice! Welcome aboard. 👋
```
---
## Exercise 06-03 – Function that returns a value

**Description**  
This exercise introduces the concept of returning values from a function instead of just printing them.  
The function `sum_upto(n)` takes a positive integer `n` and returns the sum of numbers from 1 to `n`.  
The result is then printed outside the function.


**Example:**
```python
Enter a positive integer: 6
Sum from 1 to 6 is 21
```
---
## Exercise 06-04 – Average of a Range

**Description**
This program defines a function average_range(start, end) that calculates the average of all integers between two given numbers (inclusive).
It prompts the user to enter two valid positive integers such that start < end, and returns their average.

**Functionality**

- Input validation ensures both inputs are digits and start is less than end.
- The function loops through numbers in the range [start, end].
- It accumulates the sum and counts how many numbers are processed.
- It calculates and returns the average.

**Example:**
```python
Enter start: 3
Enter end: 8
Average of numbers from 3 to 8 is 5.5
```
---
## Exercise 06-05 – Calculating Factorial Using a Function

### Description  
This program defines a function `factorial(n)` that calculates the factorial of a given number using a `for` loop.  
It prompts the user to enter a positive integer, computes its factorial, and prints the result.

### Features
- Input validation to ensure a positive integer.
- Uses a `for` loop to compute the factorial.
- Returns and displays the result.

### Example
```pyhon
Enter a number: 5
Factorial of 5 is 120
```
---
## Exercise 06-06 – Sum of Digits Using a Function

**Description**  
This program prompts the user to enter a positive integer.  
It defines a function `sum_of_digits(number)` that calculates the sum of the digits of the number using a `for` loop.

**Functionality**
- Input validation ensures the user enters only digits.
- The function adds each digit (after converting to `int`) and returns the total.

**Example**
```python
Enter a number: 5379
Sum of digits: 24
```
---
## Exercise 06-07 – Sum of Even Numbers Using Function

**Description**  
This exercise defines a function `sum_of_evens(number)` that calculates the sum of all even numbers from 1 up to the given input (inclusive).  
It uses a `for` loop inside the function and simple conditional logic.


**Functionality Example**
```python
Enter a number: 10
Sum of even numbers from 1 to 10 is 30
```
---
## Exercise 06-08 – Sum of Digits Using Recursion

### 📝 Description
This exercise defines a function `sum_digits_recursion()` that takes a number in string form and recursively calculates the sum of its digits without using any loops.

The function uses the base case of an empty string to stop the recursion and builds the total sum by converting and adding the first digit to the result of the recursive call on the rest of the string.

### 📌 Example
```python
Enter a number: 573
Sum of digits: 15
```
