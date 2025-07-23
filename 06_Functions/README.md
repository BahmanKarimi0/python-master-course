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
---
## Exercise 06-09 – Find the Maximum Value in a List (Without `max()`)

**Description**  
This program asks the user to input a list of space-separated numbers.  
It then defines a function `find_max(lst)` that manually iterates through the list to find and return the maximum value, without using Python’s built-in `max()` function.

**Example**
```python
Enter list of number separate with space (e.g. 1 2 3): 6 2 8 1 9
Max number is 9
```
---
## Exercise 06-10 – Average of Numbers in a List (Using a Function)

### Description
This program asks the user to enter a list of **positive integers** separated by space.  
It defines a function named `calculate_average(numbers)` that:

- Iterates through the list using a loop
- Calculates the sum of all elements manually
- Counts the number of elements
- Returns the **average**

> ✅ The goal is to reinforce function usage and avoid using built-in functions like `sum()` or `statistics.mean()`.


### Example
```python
Enter list of number separate with space (e.g. 1 2 3): 5 8 3 10
Average = 6.5
```
---
## Exercise 06-11 – Recursive Sum of a List

**Description**  
This program takes a list of space-separated integers as input from the user.  
It then calculates the sum of those numbers using a **recursive function**, without using loops.

**Example:**
```python
Enter list of number separate with space (e.g. 1 2 3): 4 5 6
Sum of digits: 15
```
---
### ✅ Exercise 06-12 – Check for Prime Number
**Description**
- This program defines a function is_prime(n) that checks whether a number is prime or not.
- It takes a positive integer as input from the user, and then returns True if the number is prime, otherwise False.

**Function Logic**
- A number is prime if it is greater than 1 and divisible only by 1 and itself.
- To optimize performance, we only check divisibility up to the square root of the number.

**Example:**
```python
Enter a number: 17
✅ Is prime? True
```
---
### Exercise 06-13 – Check for Perfect Number

**Description**
- This program defines a function is_perfect(n) that checks whether a given number is a perfect number.
- A perfect number is an integer that is equal to the sum of its proper positive divisors (excluding itself).

**Example:**
```python
Enter a number: 28  
✅ Is perfect? True
```
---
## Exercise 06-14 – Is Palindrome Number?

**Description**  
This program defines a function `is_palindrome()` that checks whether a given number (as a string) is a palindrome.  
A number is considered a palindrome if it reads the same forwards and backwards.

**Functionality**  
- Prompts the user to enter a positive integer.
- Calls the function `is_palindrome()` to check the condition.
- Prints the result accordingly.

**Example:**
```python
Enter a number: 1221
✅ Is palindrome: True

Enter a number: 1234
✅ Is palindrome: False
```
---
### Exercise 06‑15 – Reverse Digits of a Number
**Description**
- This program defines a function reverse_digit(number) that takes a number as a string and returns its reverse.
- The user is prompted to enter a positive integer, and the reversed number is displayed.

**Example:**
```python
Enter a number: 12345  
Reversed number: 54321
```
---
## Exercise 06-16 – Digit Count and Sum

**Description**  
This program defines a function `digit_info(number)` that receives a number as a string input.  
It calculates the total number of digits and their sum. The function returns a tuple containing both values.

**Functionality:**  
- Input: A positive integer as a string  
- Output:  
  - The number of digits  
  - The sum of all digits

**Example:**
```python
Enter a number: 4813
→ Digit count: 4
→ Sum of digits: 16
```
----
### Exercise 06-17 – Filter Prime Numbers from a List

**Description**
- This program defines a function is_prime() that determines if a given number is prime.
- It receives a list of positive integers from the user and filters out only the prime numbers using the built-in filter() function.

**Example:**
```python
Input:  12 7 9 2 5 10  
Output: [7, 2, 5]
```
---
