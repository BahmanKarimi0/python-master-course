## Chapter 05 – Loops (for, while, range, and more)

In this chapter, we focus on **iteration and repetition** using Python loops.

You will learn:
- How and when to use `for` and `while` loops
- Working with `range()`, `break`, `continue`, and `else` with loops
- Nested loops and pattern generation
- Practical loop-based tasks like factorial, Fibonacci, and data scanning
- Short-circuit logic inside loops (`and`, `or`, `not`)
- Challenges involving numbers, strings, and data simulation

We'll gradually go from **basic to advanced**, and end the chapter with a **Mini Project** to put everything together.


### 🔁 Exercises 05-01 to 05-30

Each exercise builds on your understanding of loops and related logic.

---
### Exercise 05‑01 – counting with a for‑loop and summing integers

Write a program that:

- Asks the user for an integer `n` (≥ 1)
- Prints all numbers from `1` to `n` in a single line, separated by spaces
- Prints the sum of the numbers below the list

#### Example
```python
Enter a number: 5
1 2 3 4 5
Sum: 15
```
---
### Exercise 05‑02 – countdown using a while loop

Write a program that:

- Prompts the user to enter a **positive integer `n`**
- Uses a `while` loop to count down from `n` to `1`, printing each number
- After the countdown, prints `"🚀 Liftoff!"`

#### Example:
```python
Enter a positive number (e.g. 12): 5
5
4
3
2
1
🚀 Liftoff!
```
---
### Exercise 05‑03 – printing even numbers using for and if

Write a program that:

- Asks the user to enter a **positive integer `n`**
- Prints all even numbers from `1` to `n`, separated by spaces
- At the end, prints the total number of even numbers printed

#### Example:
```python
Enter a positive number: 10
2 4 6 8 10
Total even numbers: 5
```
---
### Exercise 05‑04 – triangle pattern using nested for-loop

Write a program that:

- Asks the user to enter a **positive integer `n`**
- Prints a left-aligned triangle of stars, with `n` rows
- Each row contains a number of stars equal to the row number

#### Example:
```python
*
**
***
****
*****
```
---
### Exercise 05‑05 – summing digits of a number using for-loop

Write a program that:

- Asks the user to enter a **positive integer**
- Iterates through each digit of the number using a `for` loop
- Sums the digits
- Displays each digit with a `+` symbol and shows the total sum

#### Example:
```python
Enter a number: 391
3 + 9 + 1 = 13
```
---
### Exercise 05‑06 – reversing a number using for or while loop

Write a program that:

- Prompts the user to enter a **positive integer**
- Reverses the digits using a loop (not slicing or built-in functions!)
- Converts the result back to `int`
- Displays the reversed number and its type

#### Example:
```python
Enter a positive number (e.g. 234): 391
Reversed: 193 (type: <class 'int'>)
```
---
### Exercise 05‑07 – Checking if a Number is Prime Using a Loop

Write a program that:

- Prompts the user to enter a number greater than 1
- Checks whether the number is **prime** using a loop
- A number is prime if it is divisible only by 1 and itself
- Uses `range()` with `step=2` for better performance (skipping even numbers)
- Handles invalid inputs using exception handling

#### Example:
```python
Enter a number: 23
✅ 23 is a prime number.
```
- or
```python
Enter a number: 12
❌ 12 is not a prime number.
```
----
### 🧮 Exercise 05‑08 – Finding indices of zero and non-zero digits using `enumerate()`

#### 📌 Description
Write a program that:
- Asks the user to input a sequence of digits (e.g. `"1050401"`).
- Iterates over the digits using the `enumerate()` function.
- Separates the **indices of digits that are zero** and the **indices of digits that are non-zero** into two separate lists.
- Prints both index lists.

#### ✅ Requirements
- Use `enumerate()` to get both index and digit.
- Store the results in two lists: one for zeros and one for non-zero digits.
- Input must be validated to contain only digits.

#### 📥 Input Example:
```python
Enter a number (e.g. 1100023012): 1050401
```

#### 📤 Output Example:
```python
Indices of zeros: [1, 3, 5]
Indices of non-zero digits: [0, 2, 4, 6]
```
---
### ✅ Exercise 05-09 – Counting vowels and their indices

**Description:**  
Write a Python program that:
1. Prompts the user to input a string.
2. Counts the number of vowels (a, e, i, o, u – both uppercase and lowercase).
3. Tracks the **indices** of vowels in the string.
4. Calculates and displays the number of **non-vowel** characters.

**Input Example:**
```python
Enter a string: OpenAI creates amazing tools
```

**Expected Output:**
```python
Vowel characters: ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
Vowel count: 12
Indices of vowels: [0, 2, 4, 5, 9, 10, 12, 15, 17, 19, 24, 25]
Non-vowel count: 16
```
---
### Exercise 05‑10 – Split numbers into even and odd lists and calculate their sums

**Description**:  
This program asks the user to enter a positive integer `N`, then:

- Iterates from 1 to N (inclusive)
- Separates even and odd numbers into two different lists
- Calculates and prints the sum of each group

**Example:**
```pyhton
Enter a number: 7
Even numbers: [2, 4, 6]
Sum of evens: 12

Odd numbers: [1, 3, 5, 7]
Sum of odds: 16
```
---
### Exercise 05-11 – Repeated Digits and Their Positions

**Description**:  
This program asks the user to enter a positive integer and checks for any repeated digits.  
If a digit appears more than once, it shows the digit and the index positions (except the first one).  
If no repetitions are found, it will indicate that all digits are unique.

**Example**:
```python
Enter a number (e.g. 123543421): 123543421
🔁 Repeated digits found:
Digit '1' occurs again at positions: [8]
Digit '2' occurs again at positions: [6]
Digit '3' occurs again at positions: [4]
```
---
## Exercise 05-12 – Digits that occur only once and their indices

**Description**:  
This program prompts the user for a number (as a string of digits), then finds the digits that appear exactly once in the input.  
It prints those digits along with the index where they appear.

**Example**:
```pyhton
Enter a number (e.g. 123543421): 12234456
🔍 Digits that appear only once:
Digit '1' at index 0
Digit '5' at index 6
Digit '6' at index 7
```
---
## Exercise 05-13 – Most Frequent Digit (with First Appearance Priority)

**Description**  
This program receives a number as a string input from the user.  
It finds the most frequent digit that appears more than once.  
If multiple digits have the same maximum frequency, the one that appears **first** in the string is selected.

**Example:**
```python
Input: 99887712345
Output: Most frequent digit: 9 (2 times)

Input: 1234567890
Output: No repeated digits found.
```
---
## Exercise 05-14 – Most Frequent Digits and Their Indices

**Description**
Write a program that asks the user to enter a number (as a string).
The program should count the frequency of each digit and store their indices (positions).
Only digits that occur more than once should be displayed.
The output should be sorted in descending order of frequency.

**Requirements:**

- Use a dictionary to store each digit as a key.
- Each value should be a list containing the count and a list of indices.
- Use enumerate() to track positions.
- Sort the final output based on the number of occurrences (highest first).
- Ignore digits that occur only once.
- Validate the input to ensure it contains only digits.

**Example:**
```python
Enter positive number (e.g. 123432):
Digit: 2 – Count: 2 – Indices: [1, 5]
Digit: 3 – Count: 2 – Indices: [2, 4]
```
---
## Exercise 05-15 – Finding repeated characters and their positions in a string

**Description**  
This program prompts the user to input a non-empty string.  
It counts the occurrences of each character and records their indices.  
Finally, it prints the characters that appear more than once along with their counts and positions.

**Example:**  
```python
Enter a string (e.g. Python): programming
Character 'r' occurs 2 times at positions: [2, 6]
Character 'g' occurs 2 times at positions: [5, 9]
Character 'm' occurs 2 times at positions: [3, 4]
```
---
