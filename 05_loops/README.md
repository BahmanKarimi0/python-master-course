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
