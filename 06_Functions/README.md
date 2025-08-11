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
### 📘 Exercise 06-18 – Recursive Maximum Finder

**Description**
- This program receives a list of positive integers from the user, separated by spaces.
- It uses a recursive function to determine and return the maximum value in the list.
- Input is validated to ensure all values are digits.
- The function avoids using built-in tools like max() or loops, and instead uses recursion.

**Example:**
```python
Enter list of numbers that separate with space: 3 9 12 4 7
Max value: 12
```
---
## Exercise 06-19 – Unique Characters Check

**Description**  
Write a function that checks if all characters in a given string are unique.  
Do **not** use Python sets or `len(set(...))`.  
Use **loops only** to check for character repetition.

**Requirements**  
- The input should be a non-empty string.
- The function should return `True` if all characters are unique, otherwise `False`.

**Example**  
```python
Input: "Python"
Output: True

Input: "letter"
Output: False
```
---
### Exercise 06-20 – Palindrome Anagram Checker

**Description**
- This program checks whether the characters of a given string can be rearranged to form a palindrome.
- A string is a palindrome anagram if at most one character appears an odd number of times.

**Example:**
```python
Input: civic     → ✅ Can form a palindrome
Input: racecar   → ✅ Can form a palindrome
Input: hello     → ❌ Cannot form a palindrome
```
---
### Exercise 06-21 – Toggle Case Function

**Description**
- Write a function that receives a string and returns a new string with uppercase letters converted to lowercase, and lowercase letters converted to uppercase.
- You must use loops and conditional statements — built-in methods like swapcase() are not allowed.
- Non-alphabetic characters (like spaces and punctuation) must remain unchanged.

**Example**
```python
Input:  Hello World!
Output: hELLO wORLD!
```
---
### ✅ Exercise 06-22 – Consecutive Unicode Characters

**Description**
- Write a function that checks if the characters in a string appear consecutively in Unicode order.
- Each character must be exactly one code point after the previous one.

**Example:**
```python
"abcd" → ✅ Valid
"ace" → ❌ Invalid
"mnopq" → ✅ Valid
```
---
### Exercise 06-23 — Check for Perfect Number Using Nested Functions

**Topic:** Nested Functions

**Description:**  
Write a program that checks whether a given number is a **perfect number** or not.  
A perfect number is a number that is equal to the sum of its **proper divisors** (excluding itself).  
Use **nested functions** to structure your code.

---

**Example:**
```python
Enter a number: 28
'28' is a perfect number? True
```
---
## Exercise 06-24: Happy Number Checker


### 🧠 Description

Write a Python function named `is_happy_number(n)` that checks whether a given number is a **happy number**.

A **happy number** is defined by the following process:
- Starting with any positive integer, replace the number with the **sum of the squares of its digits**.
- Repeat the process until the number becomes `1`, or it loops endlessly in a cycle that does **not** include `1`.

If the process ends in `1`, the number is considered **happy**.

### 🔢 Example
```python
Enter a number: 19
'19' is happy number? True

Enter a number: 4
'4' is happy number? False
```
---
### ✅ Exercise 06-25: Calculate Average of Positive Numbers Using a Function

**Description**
- Write a function that takes a list of integers and returns the average of only the positive numbers. The program should take input from the user as space-separated values, convert them to integers, and print the average of the positive numbers. If no positive numbers are present, return None.

**Example:**
```python
Enter list of number that separate with space: -5 3 6 -2 1

Sum of average numbers: 3.3333333333333335
```
---
### 🧮 Exercise 06-26: Find Prime Numbers in a List

**📋 Task**

- Write a program that:
- Takes a list of integers as input (space-separated).
- Validates that all inputs are valid integers.
- Defines a function is_prime(n) that checks whether a number is prime.
- Filters and prints only the prime numbers from the list.

**✅ Example:**
```python
Input:  3 5 8 10 11 17 20  
Output: Prime numbers: [3, 5, 11, 17]
```
---
### ✅ Exercise 06-27: Frequency Count in a List


#### 📌 Question:

Write a Python program that:

1. Asks the user to input a list of positive integers separated by spaces.
2. Defines a function `frequency_count(lst)` that calculates how many times each number appears in the list.
3. Prints the frequency of each number as a dictionary: `{number: frequency}`.

> ✅ This exercise helps you practice working with functions, loops, dictionaries, and input validation.

#### 🧪 Example:
```python
Enter list of numbers that separate with space: 4 1 2 4 2 4 1
{4: 3, 1: 2, 2: 2}
```
---
### ✅ Exercise 06-28: Most Frequent Number

**Topic: Functions – Counting frequency of elements in a list**

**📘 Description:**

- Write a Python program that:
- Asks the user to enter a list of positive integers separated by spaces.
- Then, defines a function called most_frequent() that takes a list as input and returns the number that appears most frequently in the list along with its count.
- Finally, print the number and how many times it appeared.

**🧪 Example:**
```python
Input: 5 3 5 2 9 5 3 2  
Output: Number: 5, Count: 3
```
---
## Exercise 06-29: Find Duplicate Numbers in a List

**Description**  
Write a Python program that:
1. Prompts the user to enter a list of positive integers separated by space.
2. Defines a function `find_duplicates(lst)` that returns a dictionary of numbers that appear more than once.
3. Prints the repeated numbers and their counts.
4. If the list contains only unique numbers, print a message indicating that.

**Example Input:**
```python
Enter list of numbers that separated by a space: 1 2 3 2 4 3 5 6
2: 2
3: 2
```
---
### 📄 Exercise 06-30: Find Perfect Numbers in a Given Range

**🧠 Problem**
- Write a Python program that asks the user to enter two positive integers: start and end.
- Define a function that returns a list of all perfect numbers in the range [start, end].
- A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

**For example:**
```text
6 → 1 + 2 + 3 = 6
28 → 1 + 2 + 4 + 7 + 14 = 28
```

**✅ Example:**

Input:
```text
    start = 1
    end = 30
```
**Output:**
```text
    In range 1 to 30, perfect number was found: [6, 28]
```

**🚦Requirements**
- Prompt the user for two positive integers.
- Use a user-defined function to find all perfect numbers in the range.
- Display a clear message if no perfect numbers are found.
- Validate user inputs (must be positive integers).

**💡 Hint**
- Use a nested loop:
- Outer loop: from start to end
- Inner loop: sum of proper divisors of each number

**🧪 Sample Run**
```python
Enter a positive number: 1
Enter a positive number: 1000
In range 1 to 1000, perfect number was found: [6, 28, 496]
```
---
### 🧠 Exercise 06-31 — Variable Scope: Local vs. Global

**File Name:** `exercise_06_31_variable_scope_basic.py`

---

#### 📋 Task:
Define a function named `greet()` that contains a local variable `name` with the value `"Alice"`.  
Outside the function, also define a global variable `name` with the value `"Bob"`.

Then:

1. Call the `greet()` function.
2. After calling the function, print the value of the global variable `name`.

---

#### 🎯 Goal:
Understand how Python distinguishes between **local** and **global** variable scope inside and outside functions.

---

#### ✅ Example Output:
```python
Hello, Alice
Hi, Bob
```
#### 💡 Hint:
Variables defined inside a function are **local to that function** and do not affect variables in the global scope — even if they have the same name.

---

### 🧠 Exercise 06-32 — Using `global` to Modify a Global Variable

**File Name:** `exercise_06_32_global_keyword_intro.py`

---

#### 📋 Task:
Define a global variable named `counter` and set it to `0`.

Write a function named `increase()` that:

- Uses the `global` keyword to access and modify the global variable `counter`.
- Increments `counter` by 1.
- Prints the current value of `counter`.

Then, call the function three times.  
The output should be:
```python
1
2
3
```


#### 🎯 Goal:
Learn how the `global` keyword allows functions to modify global variables directly.


#### 💡 Hint:
Without using `global`, any assignment inside the function would create a new **local** variable named `counter`, shadowing the global one.

---
### 🧠 Exercise 06-33 — Using `nonlocal` in Nested Functions

**File Name:** `exercise_06_33_nonlocal_scope_nested.py`

---

#### 📋 Task:
1. Define a function called `outer()` with a local variable `count = 0`.
2. Inside `outer()`, define a nested function `inner()` that:
   - Uses the `nonlocal` keyword to access `count`.
   - Increments `count` by 1.
   - Prints the current value of `count`.
3. Call `inner()` three times inside `outer()`.
4. Finally, call `outer()`.

---

#### 🎯 Expected Output:
```python
1
2
3
```

#### 💡 Hint:
Use `nonlocal` when you want a nested function to modify a variable defined in its enclosing function scope — not global, not local, but *nonlocal*.

---
### 🧠 Exercise 06-34 — Combining `global` and `nonlocal` in Nested Scopes

**File Name:** `exercise_06_34_global_nonlocal_combo.py`

---

#### 📋 Task:
1. Define a **global** variable `total = 100`.
2. Create a function `outer()` with a local variable `count = 0`.
3. Inside `outer()`, define a nested function `inner()` that:
   - Uses `nonlocal` to access and increment `count` by 1.
   - Uses `global` to access and decrement `total` by 2.
   - Prints the current values of `count` and `total` in this format:
     ```
     Inner Call X: count = Y, total = Z
     ```
4. Call `inner()` three times inside `outer()`.
5. After calling `outer()`, print the final value of `total`.

---

#### ✅ Expected Output:
```python
Inner Call 1: count = 1, total = 98
Inner Call 2: count = 2, total = 96
Inner Call 3: count = 3, total = 94
Final total = 94
```

#### 💡 Hint:
- Use `global` to modify variables defined outside all functions.
- Use `nonlocal` to modify variables defined in enclosing (but not global) scopes.
---
### 🧠 Exercise 06-35 — Implementing a Simple Timer Decorator

**File Name:** `exercise_06_35_simple_timer_decorator.py`

---

#### 📋 Task:
1. Create a decorator `timer` that:
   - Measures the execution time of the decorated function using `perf_counter`.
   - Prints the elapsed time with the function name.
   - Returns the original function’s return value.

2. Define a function `countdown(n)` that:
   - Counts down from `n` to `1`, printing each number.
   - Uses `sleep(1)` to pause for 1 second between prints.

3. Apply the `timer` decorator to `countdown`.

#### 🎯 Goal:
Understand how decorators work and how to use them for timing function execution.

#### 💡 Hint:
Use `functools.wraps` to preserve metadata of the original function.

### Output example:
```python
3
2
1
Time taken for 'countdown' is 3.00xx seconds
```
---
### 🧠 Exercise 06-36 — Decorator Handling Arbitrary Arguments (*args, **kwargs)

**File Name:** `exercise_06_36_debug_args_decorator.py`

---

#### 📋 Task:
Create a decorator `debug_args` that:
- Prints the function name along with all positional (`*args`) and keyword (`**kwargs`) arguments whenever the decorated function is called.
- Calls the original function with the same arguments.
- Returns the original function's return value.

---

#### 🎯 Goal:
Learn how to write decorators that support any number and type of function arguments.

---

#### 💡 Hint:
Use `*args` and `**kwargs` in the wrapper function to capture all arguments.
Use `functools.wraps` to preserve the decorated function’s metadata.

### Example input:
```python
@debug_args
def greet(name, age=None):
    print(f"Hello {name}, age {age}")

greet("Alice")
greet("Bob", age=30)
```
### Example output:
```python
Calling greet with args: ('Alice',), kwargs: {}
Hello Alice, age None
Calling greet with args: ('Bob',), kwargs: {'age': 30}
Hello Bob, age 30
```
---
### 🧠 Exercise 06-37 — Decorator with Arguments (Repeat Decorator)

**File Name:** `exercise_06_37_repeat_decorator_factory.py`

---

#### 📋 Task:
Create a decorator factory `repeat(num_times)` that returns a decorator.  
This decorator, when applied to a function, causes it to run `num_times` times each time it's called.  
Only the result of the **last** call should be returned (if any).

---

#### ✅ Example:
```python
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```

### Output:
```python
Hello Alice
Hello Alice
Hello Alice
```
---
### 🧠 Exercise 06-38 — Using Multiple Decorators on a Single Function

**File Name:** `exercise_06_38_multiple_decorators.py`

---

#### 📋 Task:
1. Write two decorators:
   - `uppercase`: Converts the function’s return string to uppercase.
   - `add_exclamation`: Adds an exclamation mark `!` to the end of the returned string.

2. Apply both decorators to a function `say_hello(name)` which returns `"Hello {name}"`.

3. Print the result of calling `say_hello("Alice")`.


#### ✅ Expected Output:
```python
HELLO ALICE!
```

#### 💡 Hint:
- Decorators are applied **bottom-up**, but executed **top-down**.
- Use `functools.wraps` to preserve the identity of the original function.
---
### 🧠 Exercise 06-39 — Logging Decorator

**File Name:** `exercise_06_39_logging_decorator.py`


#### 📋 Task:
Write a decorator `log_status` that:
- Before the function runs, prints: `--> Starting function 'func_name'`
- After the function runs, prints: `<-- Finished function 'func_name'`

Apply it to a function `process_data()` that prints `"Processing data..."`.

#### ✅ Expected Output:
```python
--> Starting function process_data
Processing data...
<-- Finished function process_data
```

#### 💡 Hint:
Use `@wraps(func)` to preserve the original function’s identity.

---
### 🧠 Exercise 06-40 — Authorization Decorator

**File Name:** `exercise_06_40_authorization_decorator.py`

---

#### 📋 Task:
Create a decorator factory `authorize(allowed_users)` that returns a decorator.  
This decorator should allow only the users listed in `allowed_users` to execute the decorated function.

- The first parameter of the function must be `user`.
- If the user is allowed, the function runs.
- If not, print: ❌ Access denied for user 'username'

---

#### 🧪 Example:

```python
@authorize(allowed_users=["admin", "root"])
def delete_all_data(user):
    print("🚨 All data deleted!")

delete_all_data("admin")  # ✅ Allowed
delete_all_data("guest")  # ❌ Denied
```

#### ✅ Expected Output:
```python
🚨 All data deleted!
❌ Access denied for user 'guest'
```
---
### 🧠 Exercise 06-41 — Memoization Decorator

**File Name:** `exercise_06_41_memoize_decorator.py`


#### 📋 Task:
Write a decorator `memoize` that caches the result of a function for repeated arguments.  
If the same arguments are passed again, return the cached result instead of re-running the function.

Additionally, print:
```python
✅ Returned cached result for args: (a, b)
```


#### 🧪 Example:

```python
@memoize
def show_add(a, b):
    print(f"Calculating {a} + {b}...")
    return a + b

print(show_add(1, 2))
print(show_add(2, 1))
```
#### ✅ Expected Output:
```python
Calculating 1 + 2...
3
✅ Returned cached result for args: (1, 2)
3
```
---
### 🧠 Exercise 06-42 — Call Counter Decorator

**File Name:** `exercise_06_42_call_counter_decorator.py`

---

#### 📋 Task:
Create a decorator `call_counter` that tracks how many times a function has been called.

- After each call, it should print:
  🧮 Called func_name X times

- Each decorated function must maintain its own independent counter.

---

#### 🧪 Example:

```python
@call_counter
def greet(name):
    print(f"Hello {name}")

@call_counter
def say_hi(name):
    print(f"Hi {name}")

say_hi('Alice')
say_hi('John')
greet('Bob')
```
#### ✅ Expected Output:
```python
Hi Alice
🧮 Called say_hi 1 times
Hi John
🧮 Called say_hi 2 times
Hello Bob
🧮 Called greet 1 times
```
---
### 🧠 Exercise 06-43 — Time-Restricted Function Decorator

**File Name:** `exercise_06_43_time_restricted_decorator.py`

---

#### 📋 Task:
Write a decorator factory `only_during(start_time, end_time)` that:
- Allows the decorated function to run only between the given hours.
- If the current hour is outside the allowed range, print:
  ❌ Access denied: only available from {start_time} to {end_time}

---

#### 🧪 Example:

```python
@only_during(start_time=8, end_time=18)
def access_data():
    print("🔓 Access granted!")

access_data()
```
#### ✅ Expected Output:
If current hour is 10:
```python
🔓 Access granted!
```

If current hour is 22:
```python
❌ Access denied: only available from 8 to 18
```
---
### 🧠 Exercise 06-44 — Multi-Condition Access Control Decorator

**File Name:** `exercise_06_44_multi_condition_decorator.py`

---

#### 📋 Task:
Build a decorator `access_controlled()` that enforces 3 conditions before allowing access to a function:

1. ✅ Only allowed users can access the function.
2. 🕒 Function can only be accessed during a specific time window (e.g. 9–17).
3. 🔁 Each user can only call the function a limited number of times.

---

#### 🧪 Example:

```python
@access_controlled(allowed_users=["admin", "root"], start_hour=9, end_hour=17, max_calls=2)
def access_dashboard(user):
    print(f"✅ Welcome {user}, here is your dashboard")

access_dashboard("admin")  # ✅
access_dashboard("admin")  # ✅
access_dashboard("admin")  # ❌ Max call
access_dashboard("guest")  # ❌ Unauthorized
```
#### 🧠 Requirements:

- Use inspect to extract the user argument.
- Store call counts per user.
- Print messages based on what condition failed.
```
---
### 🧠 Exercise 06-45 — Type Validator Decorator

**File Name:** `exercise_06_45_validate_argument_types.py`

---

#### 📋 Task:
Write a decorator factory `validate_types()` that checks whether given arguments match their expected types.  
If any mismatch is found, print a helpful error and prevent function execution.

---

#### ✨ Example:

```python
@validate_types(name=str, age=int, active=bool)
def register(name, age, active=True):
    print(f"✅ Registered {name}, age {age}, active={active}")

register("Ali", 30, active=True)        # ✅
register("Sara", "twenty", active=True) # ❌ age must be int
register("Bob", 25, active="yes")       # ❌ active must be bool
```
#### ✅ Expected Output:
```python
✅ Registered Ali, age 30, active=True
❌ Invalid type for argument "age": expected int, got str
❌ Invalid type for argument "active": expected bool, got str
```
---
### 🧠 Exercise 06-47 — Basic Generator: Count up to n

**File Name:** `exercise_06_47_count_up_to_generator.py`

---

#### 📋 Task:
Write a generator function `count_up_to(n)` that yields numbers from 1 up to and including `n`, one at a time.

---

#### 🧪 Example:

```python
gen = count_up_to(5)
for num in gen:
    print(num)
```
#### Output:
```python
1
2
3
4
5
```
---
### 🧠 Exercise 06-48 — Generator for Even Numbers

**File Name:** `exercise_06_48_even_numbers_generator.py`

---

#### 📋 Task:
Write a generator function `even_numbers_up_to(n)` that yields all even numbers from 1 up to and including `n`.

---

#### 🧪 Example:

```python
gen = even_numbers_up_to(10)
for num in gen:
    print(num)
```
#### Output:
```python
2
4
6
8
10
```
---
### 🧠 Exercise 06-49 — Countdown Generator

**File Name:** `exercise_06_49_countdown_generator.py`

---

#### 📋 Task:
Write a generator function `countdown_generator(n)` that yields numbers from `n` down to 1 (inclusive), one at a time.

---

#### 🧪 Example:

```python
gen = countdown_generator(5)
for num in gen:
    print(num)
```
#### Output:
```python
5
4
3
2
1
```
---
### 🧠 Exercise 06-50 — Prime Numbers Generator

**File Name:** `exercise_06_50_prime_generator.py`

---

#### 📋 Task:
Write a generator function `prime_generator(n)` that yields all prime numbers from 2 up to and including `n`.

You must not use any list, set, or external library — only `yield` and manual prime checking.

---

#### 🧪 Example:

```python
gen = prime_generator(10)
for p in gen:
    print(p)
```
#### Output:
```python
2
3
5
7
```
---
### 🧠 Exercise 06-51 — Generator with Internal State: Numbered Lines

**File Name:** `exercise_06_51_numbered_lines_generator.py`

---

#### 📋 Task:
Write a generator function `numbered_lines(lst)` that takes a list of strings and yields each line with its line number, starting from 1.

Do not use `enumerate()` — you must implement manual numbering logic.

---

#### 🧪 Example:

```python
lines = ["Hello", "This is a test", "Goodbye"]
gen = numbered_lines(lines)
for line in gen:
    print(line)
```
#### Output:
```python
1: Hello
2: This is a test
3: Goodbye
```
---
### 🧠 Exercise 06-52 — Character Stream Generator

**File Name:** `exercise_06_52_char_stream_generator.py`

---

#### 📋 Task:
Write a generator function `char_stream(lst)` that takes a list of strings and yields each character from each string, in order.

---

#### 🧪 Example:

```python
sentences = ["Hello", "Bye"]
gen = char_stream(sentences)
for c in gen:
    print(c, end=" ")
```
#### Output:
```python
H e l l o B y e
```
---
### 🧠 Exercise 06-53 — Infinite Fibonacci Generator

**File Name:** `exercise_06_53_infinite_fibonacci_generator.py`

---

#### 📋 Task:
Write a generator function `fibonacci_generator()` that yields an infinite sequence of Fibonacci numbers.

- Must use `yield`
- Must use `while True`
- Do not use lists or store the entire sequence in memory

---

#### 🧪 Example:

```python
gen = fibonacci_generator()
for _ in range(10):
    print(next(gen), end=' ')
```
#### Output:
```python
0 1 1 2 3 5 8 13 21 34
```
---
### 🧠 Exercise 06-54 — Custom Reverse Range Generator

**File Name:** `exercise_06_54_reverse_range_generator.py`

---

#### 📋 Task:
Write a generator function `reverse_range(start, end, step)` that yields numbers from start to end (exclusive), counting backwards by step.

You must:
- Not use `range()`
- Not use any list or comprehension
- Only use `yield` and a while loop

---

#### 🧪 Example:

```python
for i in reverse_range(10, 0, 2):
    print(i, end=' ')
```
#### Output:
```python
10 8 6 4 2
```
---
### 🧠 Exercise 06-55 — Perfect Squares Generator

**File Name:** `exercise_06_55_perfect_squares_generator.py`

---

#### 📋 Task:
Write a generator function `perfect_squares(lst)` that takes a list of integers and yields only the perfect square numbers.

- Must use `yield`
- Do not return a list
- Use `math.isqrt()` for precise square root comparison

---

#### 🧪 Example:

```python
nums = [2, 4, 8, 9, 10, 16, 18, 25, 30]
gen = perfect_squares(nums)
for num in gen:
    print(num, end=' ')
```
#### Output:
```python
4 9 16 25
```
---
### 🧠 Exercise 06-56 — Lazy Line Reader Generator

**File Name:** `exercise_06_56_lazy_line_reader.py`

---

#### 📋 Task:
Write a generator function `lazy_line_reader(lst)` that yields lines from a list of strings one by one.

- The generator should stop when it encounters an empty string (`''`)
- Use only `yield`, no return or list-based processing

---

#### 🧪 Example:

```python
lines = [
    "User: Alice",
    "Action: Login",
    "Status: Success",
    "",
    "This should not be printed"
]

for line in lazy_line_reader(lines):
    print(line)
```
#### Output:
```python
User: Alice
Action: Login
Status: Success
```
---
### 🧠 Exercise 06-57 — Event Tracker Generator

**File Name:** `exercise_06_57_event_tracker_generator.py`

---

#### 📋 Task:
Write a generator function `event_tracker(events)` that yields formatted log messages for each event.

Each message should be like:
```text
[1] Received event: Login
```

---

#### 🧪 Example:

```python
events = ["Login", "ViewProfile", "Logout"]

for log in event_tracker(events):
    print(log)
```
#### Output:
```python
[1] Received event: Login
[2] Received event: ViewProfile
[3] Received event: Logout
```
---
### 🧠 Exercise 06-58 — Filtered Events Generator

**File Name:** `exercise_06_58_filtered_events_generator.py`

---

#### 📋 Task:
Write a generator function `filtered_events(events, important)` that yields only those events which are present in the `important` list.

- Use `yield` only.
- Case-sensitive comparison.
- No intermediate lists.

---

#### 🧪 Example:

```python
events = ["Login", "ViewProfile", "Logout", "Download", "Error", "Upload"]
important = ["Login", "Logout", "Error"]

gen = filtered_events(events, important)
for log in gen:
    print(log)
```
#### Output:
```python
Login
Logout
Error
```
---
### 🧠 Exercise 06-59 — Real-Time Alert Generator

**File Name:** `exercise_06_59_real_time_alert_generator.py`

---

#### 📋 Task:
Write a generator function `real_time_alert(data, threshold=100)` that:

- Yields `"OK: value"` for values below the threshold
- Yields `"⚠️ ALERT: value exceeded! (value)"` if value > threshold
- After 3 alerts, yields `"🛑 Max alerts reached. Monitoring stopped."` and exits

---

#### 🧪 Example:

```python
data = [45, 55, 102, 88, 120, 101, 99, 80]

for msg in real_time_alert(da
```
#### Output:
```python
OK: 45
OK: 55
⚠️ ALERT: value exceeded! (102)
OK: 88
⚠️ ALERT: value exceeded! (120)
⚠️ ALERT: value exceeded! (101)
🛑 Max alerts reached. Monitoring stopped.
```
---
### 🧠 Exercise 06-60 — Dynamic Command Generator with `send()`

**File Name:** `exercise_06_60_dynamic_command_generator.py`

---

#### 📋 Task:
Write a coroutine-based generator `command_generator()` that:

- Starts counting from 0
- Yields `"Message number X"` each time
- If it receives `'reset'` via `send()`, it resets the counter to 0
- If it receives `'stop'`, it terminates and returns `"Finish"`

---

#### 🧪 Example:

```python
gen = command_generator()

print(next(gen))          # Message number 0
print(gen.send(None))     # Message number 1
print(gen.send('reset'))  # Message number 0
print(next(gen))          # Message number 1
print(gen.send('stop'))   # Raises StopIteration with value 'Finish'
```
---
### 🧠 Exercise 06-61 — Threshold Filter Coroutine

**File Name:** `exercise_06_61_threshold_filter_coroutine.py`

---

#### 📋 Task:
Write a coroutine function `filter_above(threshold)` that:

- Accepts numeric input via `send()`
- Yields a message indicating if the input is above the threshold
- Closes gracefully with `.close()`

---

#### 🧪 Example Usage:

```python
f = filter_above(50)
next(f)
print(f.send(42))   # ❌ Rejected: 42
print(f.send(75))   # ✅ Accepted: 75
f.close()
```
---
### 🧠 Exercise 06-62 — Filter & Forward Coroutine (Pipeline Stage)

**File Name:** `exercise_06_62_pipeline_filter_stage.py`

---

#### 📋 Task:
Create a coroutine function `filter_and_forward(threshold, target_coroutine)` that:

- Receives data via `send()`
- Only forwards values greater than `threshold` to `target_coroutine` using `.send()`
- Ignores values below or equal to threshold
- Closes the `target_coroutine` when itself is closed

---

#### 🧪 Example:

```python
def printer():
    try:
        while True:
            msg = yield
            print(f'📥 Received in sink: {msg}')
    except GeneratorExit:
        print('🔚 Printer closed.')

sink = printer()
next(sink)

stage = filter_and_forward(threshold=10, target_coroutine=sink)
next(stage)

stage.send(5)     # Ignored
stage.send(20)    # Forwarded
stage.send(12)    # Forwarded
stage.close()     # Sink also closes
```
#### Output:
```python
📥 Received in sink: 20
📥 Received in sink: 12
🔚 Printer closed.
```
---
### 🧠 Exercise 06-63 — Accumulator Coroutine

**File Name:** `exercise_06_63_accumulator_coroutine.py`

---

#### 📋 Task:
Build a coroutine function `accumulator_and_print()` that:

- Accepts numerical input via `.send()`
- Keeps a running total and prints it
- If `"reset"` is received, resets the total to 0 and prints a reset message
- If invalid input is received (not number or "reset"), prints a warning
- On close, prints shutdown message

---

#### 🧪 Example:

```python
acc = accumulator_and_print()
next(acc)

print(acc.send(10))        # 📈 Running total: 10
print(acc.send(20))        # 📈 Running total: 30
print(acc.send('reset'))   # 🔄 Total reset to 0
print(acc.send(5))         # 📈 Running total: 5
print(acc.send('oops'))    # ⚠️ Invalid input: 'oops'
acc.close()                # 🔒 Coroutine closed gracefully.
```
---
# Exercise 06-64 — Pattern Filtering & Forwarding Coroutine

**File Name:** `exercise_06_64_pattern_filter_forward.py`

---

## Task:

Implement a coroutine function `filter_by_keyword(keyword, target)` that:

- Receives messages (strings) via `.send()`
- Checks if the message contains the specified `keyword`
- If yes, forwards the message to the `target` coroutine
- If the message is not a string, prints a warning message
- Upon closing, closes the `target` coroutine as well

---

## Example usage:

```python
def logger():
    try:
        while True:
            msg = yield
            print(f"📝 Log: {msg}")
    except GeneratorExit:
        print("📕 Logger closed.")

sink = logger()
next(sink)

fwd = filter_by_keyword(keyword="ERROR", target=sink)
next(fwd)

fwd.send("System started")
fwd.send("ERROR: Disk failure")
fwd.send("User logged in")
fwd.send(123)  # warning for invalid input
fwd.send("ERROR: Overheating")

fwd.close()
```
#### Output:
```python
📝 Log: ERROR: Disk failure
⚠️ Invalid input (not string): 123
📝 Log: ERROR: Overheating
📕 Logger closed.
```
---
## Exercise 06-65: SMA Calculation with Coroutines and Error Handling

**Description**  
Create a Python **coroutine** that receives temperature readings and calculates the **Simple Moving Average (SMA)** in real time.  
The coroutine should handle the following cases:
1. If the input is a number (`int` or `float`), update the SMA and yield the new value.
2. If the input is the string `"reset"`, reset all calculations and start fresh.
3. If the input is of an invalid type, print an informative error message showing:
   - the expected types
   - the actual type received
   - the value itself
4. On coroutine closure, print a shutdown message.

---

**Expected Behavior**  
Given the input sequence:  
```python
tsma = temperature_monitoring()
next(tsma)
print(tsma.send(10))
print(tsma.send(20))
print(tsma.send(30))
print(tsma.send('reset'))
print(tsma.send(30))
```
#### Output:
```python
SMA: 10.00
SMA: 15.00
SMA: 20.00
🔄 SMA values have been reset. Starting fresh from next input.
SMA: 30.00
🔒 Coroutine closed gracefully.
```
---
# Exercise 06-66: Coroutine-based Multi-Stage Pipeline

## Description

Build a multi-stage message processing pipeline using Python coroutines:

1. **filter_by_length(min_length, target)**  
   - Pass only string messages longer than `min_length` to the next coroutine.  
   - If input is not a string, print an error message showing the invalid input and its type.  

2. **to_upper(target)**  
   - Convert incoming strings to uppercase and send to the next coroutine.  

3. **logger()**  
   - Receive strings and print them with the prefix `"LOG:"`.  

The coroutines should be chained so messages flow from `filter_by_length` → `to_upper` → `logger`.  

---

## Sample usage

```python
log = logger()
next(log)
upper = to_upper(log)
next(upper)
fbl = filter_by_length(5, upper)
next(fbl)

fbl.send("hi")
fbl.send("coroutine")
fbl.send(123)
fbl.send("python")
```
#### Output:
```python
⚠️ Invalid input type: expected str, got int (123)
LOG: COROUTINE
LOG: PYTHON
```
---
# Exercise 06-67: Delayed Message Sender Using Coroutine

## Description

Create a coroutine `delayed_sender(delay, target)` that receives messages,  
waits for a specified `delay` (in seconds) before forwarding each message to a target coroutine.  

Also implement a `sink_printer()` coroutine that receives messages and prints them.

The coroutines work together to simulate delayed message passing.

---

## Functions

- `delayed_sender(delay, target)`  
  Receives messages, delays for `delay` seconds, then sends the message to `target`.  

- `sink_printer()`  
  Receives messages and prints them prefixed with `"Received:"`.  

---

## Example Usage

```python
import time

sink = sink_printer()
next(sink)

delayed = delayed_sender(1, sink)
next(delayed)

messages = ["first", "second", "third"]
start = time.time()

for msg in messages:
    delayed.send(msg)

end = time.time()
print(f"Total elapsed time: {end - start:.2f} seconds")
```
#### Output:
```python
Received: first
Received: second
Received: third
Total elapsed time: 3.00 seconds
```
---
# Exercise 06-68: Coroutine Advanced Filter with Message Statistics

## Description

Create a coroutine function `advanced_filter(keyword, min_length, target)` that receives messages and forwards only those messages to the `target` coroutine that:

- Contain the specified `keyword` (case-insensitive),
- Have length greater than `min_length`.

The coroutine should count the total messages received and the number of messages that passed the filter. When the coroutine is closed (using `.close()`), it should print these statistics.

Create another coroutine `message_logger()` that receives messages and logs them by printing.

---

## Functions

- `advanced_filter(keyword: str, min_length: int, target: coroutine)`
- `message_logger()`

---

## Example Usage

```python
log = message_logger()
next(log)

filterer = advanced_filter('error', 10, log)
next(filterer)

messages = [
    "Error 404",           # filtered out (length < 10)
    "Critical error found",# passed filter
    "Warning: Disk full",  # filtered out (keyword not found)
    "Major error detected" # passed filter
]

for msg in messages:
    filterer.send(msg)

filterer.close()
```
#### Output:
```python
Logged: Critical error found
Logged: Major error detected
Total messages received: 4
Messages passed filter: 2
```
---
# Exercise 06-69: Coroutine Pipeline with Keyword and Length Filters

## Description

Implement a coroutine pipeline with the following stages:

1. `keyword_filter(keyword, target)`: Passes only messages containing the `keyword` (case-insensitive) to the next coroutine.
2. `length_filter(min_length, target)`: Passes only messages with length greater than `min_length` to the next coroutine.
3. `message_logger()`: Logs received messages by printing them.

The messages flow through the pipeline in order: keyword filter → length filter → logger.

---

## Functions

- `keyword_filter(keyword: str, target: coroutine)`
- `length_filter(min_length: int, target: coroutine)`
- `message_logger()`

---

## Example Usage

```python
log = message_logger()
next(log)

lf = length_filter(5, log)
next(lf)

kw = keyword_filter('error', lf)
next(kw)

messages = [
    "Error 404",
    "Critical error found",
    "Warning: Disk full",
    "Major error detected"
]

for msg in messages:
    kw.send(msg)

kw.close()
```
#### Output:
```python
Logged: Critical error found
Logged: Major error detected
🔒 Coroutine closed gracefully.
```
---
## 📝 Exercise 06-70: Coroutine Pipeline with State & Error Handling

### 🎯 Objective
In this exercise, you'll build a **coroutine pipeline** that:
1. Receives inputs and validates their type.
2. Accepts only integers (`int`).
3. Passes only **even** numbers to the next stage.
4. Accumulates the sum of positive numbers until a negative number is received.
5. Closes all coroutines gracefully without raising `StopIteration`.

---

### 📌 Details
- Use the `.close()` method to terminate coroutines safely.
- If an invalid data type is received, print a warning but **do not** stop the program.
- Implement the logic as a chain of coroutines (**pipeline**).
- On closing each coroutine, print a message so the shutdown sequence is clear.

---

### 📥 Sample Input
```python
[2, 6, "oops", -4, 10]
```
#### Output:
```python
Running sum: 2
Running sum: 8
⚠️ Invalid input type: expected int, got str ('oops')
Negative number received, closing accumulator.
Final sum: 8
📥 Input receiver closed.
🔍 Even filter closed.
🔒 Coroutine closed gracefully.
```
---
# Exercise 06-71: Coroutine Pipeline for Text Processing

## Description

Implement a coroutine pipeline that processes lines of text through multiple stages. Each stage is a coroutine that performs a specific transformation or filtering on the text, then passes the result to the next stage.

The pipeline stages are:

1. **Keyword Filter**: Only passes lines containing a specified keyword (case-insensitive).
2. **Length Filter**: Only passes lines longer than a specified minimum length.
3. **Uppercase Transformer**: Transforms lines to uppercase.
4. **Logger**: Prints the final processed lines.

The pipeline should properly handle:

- Invalid input types (print a warning message).
- Graceful closing of coroutines.
- Data should flow from one stage to the next via `send()` calls.

## Expected Behavior

Given the input data:

```python
[
  'CRITICAL ERROR detected',
  'CRITICAL disk FAILURE',
  'CRITICAL MEMORY error',
  'minor issue logged'
]
```
#### Output:
```python
LOG: CRITICAL ERROR DETECTED
LOG: CRITICAL DISK FAILURE
LOG: CRITICAL MEMORY ERROR
```
---
# Exercise 06-72: Recursive Factorial Function

## Problem Statement

Write a recursive function named `factorial` that takes a non-negative integer `n` as input and returns the factorial of `n`.

- If `n` is 0, the function should return 1.
- Otherwise, the function should return `n * factorial(n - 1)`.

**Notes:**  
- The input will always be a non-negative integer.  
- Do **not** use loops; implement the solution using recursion only.

## Example

```python
factorial(5)  # Output: 120
```
---
# Exercise 06-73: Recursive Fibonacci Function

## Problem Statement

Write a recursive function named `fibonacci` that takes a non-negative integer `n` as input and returns the `n`-th number in the Fibonacci sequence.

The Fibonacci sequence is defined as:
- `fibonacci(0) = 0`
- `fibonacci(1) = 1`
- For `n >= 2`: `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)`

**Notes:**
- The input will always be a non-negative integer.
- Do **not** use loops; implement the solution using recursion only.

## Example

```python
fibonacci(5)  # Output: 5
```
--
