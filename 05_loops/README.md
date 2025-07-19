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
## Exercise 05-16 – List all prime numbers up to N

**Description**  
This program receives a number from the user and prints  
all **prime numbers** less than or equal to the input.  
It uses a basic algorithm to check for primality using trial division.

**Example**
```pyhton
Enter a positive number: 17
Prime numbers up to 17: 2, 3, 5, 7, 11, 13, 17
```
---
## Exercise 05-17 – Run-Length Encoding of Repeated Digits

**Description**  
This program receives a number from the user as a string.  
It compresses the string using **run-length encoding**, which counts **consecutive repeated digits**.  
The result is a new string where each group of repeated digits is represented by the digit followed by its count.

**Example:**
```python
Enter a number: 11223344445555
Output: 2132234455
```

Explanation:
- Two '1's → `21`  
- Two '2's → `22`  
- Three '3's → `33`  
- Four '4's → `44`  
- Three '5's → `53`

**Sample Input/Output:**
```python
Input: 11233355
Output: 2133352
```
---
## Exercise 05-18 – Most Consecutive Repeated Digit

**Description**  
This program prompts the user to enter a number as a string.  
It finds the digit that appears **the most consecutively**, and displays both the digit and how many times it was repeated in sequence.

**Example**  
```python
Enter a number: 1223334444555
Digit '4' appears the most consecutively (4 times).
```
---
## Exercise 05-19 – Check if Digits Are in Ascending or Descending Order (with loops)

**Description**  
This program asks the user to enter a number (as a string).  
Using a `for` loop, it checks whether the digits of the number are arranged in ascending, descending, or unordered sequence.

It compares each digit with the next one and keeps track of whether the sequence is strictly increasing or decreasing.

**Example**
```python
Enter a number: 123456
✅ The digits are in ascending order.

Enter a number: 987321
✅ The digits are in descending order.

Enter a number: 135264
❌ The digits are not in a consecutive order.
```
---
## Exercise 05‑20 – Digit Factorial Match (Weird Number)

**Description**  
This program checks if a number is a "Weird Number" — meaning the sum of the factorials of its digits equals the number itself.  
It demonstrates the use of `for` loops for digit iteration and factorial calculation.

**Example:**
```python
Enter a number: 145
✅ 145 is a Weird Number (1! + 4! + 5! = 145)

Enter a number: 123
❌ 123 is NOT a Weird Number (1! + 2! + 3! = 9)
```
---
## Exercise 05-21 – Triple Repeat Finder (Loop & String Analysis)

**Description**  
This program receives a string from the user and checks if any character appears **exactly 3 times in a row**.  
If so, it prints those characters and the index where the triple repetition starts.  
If no such sequence exists, it informs the user accordingly.

**Example 1:**
```python
Enter a string: aaabbcccddde
✅ Found: character 'a' repeats 3 times starting at index 0
✅ Found: character 'c' repeats 3 times starting at index 5
✅ Found: character 'd' repeats 3 times starting at index 8
```

**Example 2:**
```python
Enter a string: abcdefgh
❌ No character repeated exactly 3 times in a row.
```
---
## Exercise 05‑22 – Shifted Characters Using Unicode

**Description**  
This program prompts the user to enter a string.  
It then generates a new string where each character is shifted forward by one in the Unicode table.  
For example, `'a'` becomes `'b'`, `'Z'` becomes `'['`, and `'9'` becomes `':'`.

**Functions used:**
- `ord(char)` – returns the Unicode code point of the character
- `chr(code)` – returns the character represented by the Unicode code point

**Example:**
```python
Enter a string: abZ9*
Shifted string: bc[:+
```
---
## Exercise 05‑23 – Count Duplicate Letters (Case-Insensitive)

**Description**  
This program receives a string input from the user and finds all alphabetic characters (letters)  
that appear more than once, regardless of case (A/a treated the same).  
It prints how many times each repeated letter appears, along with the list of indices where they occur.

**Key Concepts:**
- `for` loop with `enumerate()`
- `dict` for counting and storing indices
- `str.casefold()` for case-insensitive comparison
- `str.isalpha()` to filter only letters

**Example:**
```python
Enter a string: ApPle is Amazing

Found repeated letters:
Letter 'a' appears 3 times at indices: [0, 10, 14]
Letter 'i' appears 2 times at indices: [6, 12]
```
---
## Exercise 05-24 – Sum of Inner Digits (Excluding First and Last)

**Description**  
This program receives a number as input and calculates the sum of the digits **excluding the first and last** digit.  
If the number has fewer than 3 digits, it prints a warning.

**Example 1:**
```python
Enter a number: 52367
Sum: 12 (2 + 3 + 7)
```

**Example 2:**
```python
Enter a number: 81
Number must have at least 3 digits.
```
## Exercise 05-25 – Detecting Consecutive Ascending Digits

**Description**  
This program prompts the user to enter a number (as a string).  
It then searches for a **sequence of at least 3 digits** that are in strictly increasing consecutive order.  
If such a sequence is found, it prints it. Otherwise, it informs the user that no such sequence exists.

**Example:**
```python
Enter a number: 245678
✅ Found ascending number: 456

Enter a number: 987654
❌ No ascending digits were found.
```
---
## Exercise 05-26 – Alternating Odd and Even Digits

**Description**  
This program checks whether the digits of a given number alternate between odd and even values.  
If any two consecutive digits are both odd or both even, the sequence is **not** considered alternating.

**Example:**
```python
Enter a number: 281739
✅ Digits alternate between odd and even.

Enter a number: 1223
❌ Digits do not alternate.
```
---
## Exercise 05-27 – Alternating Case Sequence

**Description**  
This program takes a string input from the user and checks whether the letters alternate between uppercase and lowercase.  
An alternating sequence is one where no two adjacent letters share the same case.

**How it works:**
- The user is prompted to enter a string (letters only, no spaces or numbers).
- The program checks that each letter has a different case than the one before.
- If all adjacent letters alternate in case, the input is considered valid.

**Example:**
```python
Input: AbCdEfG → ✅ Alternating case
Input: aBcDEfg → ❌ Not alternating
Input: aBCd → ❌ Not alternating
```

**Constraints:**
- Input must contain only alphabetic characters (A-Z, a-z).
- Case sensitivity is enforced (i.e., 'a' and 'A' are treated differently).
---
## Exercise 05-28 – Longest Substring Without Repeating Characters

**Description**  
This program takes a string as input and finds the longest substring without repeating characters using a loop-based approach.  
It uses a sliding window logic to check each possible segment and updates the longest substring accordingly.

**Example:**
```python
Enter a string: abcadefgb
✅ Longest substring without repeating characters: bcadefg (length: 7)
```
---
## Exercise 05-29 – Repeated Substrings (Length ≥ 2)

**Description**  
This program takes a string input and identifies all substrings (length ≥ 2)  
that occur more than once in the input string.  
It then prints each repeated substring along with the number of times it appears.

**How it works:**
- It uses nested `while` loops to generate all possible substrings.
- Only substrings of length 2 or more are tracked.
- The program uses a dictionary to count how many times each substring appears.
- Finally, it prints only those substrings that appear more than once.

**Example:**
```python
Enter a string: ababcabc
Found repeated substrings:
'ab' → 3 times
'ba' → 2 times
'abc' → 2 times
'bca' → 2 times
```
---
