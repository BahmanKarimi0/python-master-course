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

** Requirements: **
- Define a function without parameters.
- Inside the function, print: Hello from a function!
- Call the function from the main program.

** Example Output: **
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
