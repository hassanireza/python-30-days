# Day 01 🐍 - Setup & Hello World

<div align="center">

| ← This is the first lesson | [🏠 Home](../../README.md) | [Day 02: Next Lesson →](../day-02/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Install Python, write your first script, and understand how Python programs run.

**What you will learn today:**

- Installing Python 3.10+
- Running your first script
- The `print()` function
- Comments in Python
- Python interactive shell (REPL)
- How Python executes code

---

## Key Concepts

| Concept | Description |
|---|---|
| `print()` | Outputs text to the screen. The most fundamental Python function. |
| `# comments` | Lines starting with `#` are ignored by Python. They explain code to humans. |
| `Python REPL` | Type `python3` in your terminal to enter an interactive Python session. |

---

## Code Examples

### Your First Python Program

```python
# This is a comment - Python ignores it
print("Hello, World!")
print("My name is Python and I am 30 years old.")
```

### print() with multiple arguments

```python
# print() can take multiple arguments separated by commas
print("Python", "is", "awesome")   # Output: Python is awesome

# You can change the separator
print("2024", "01", "15", sep="-")  # Output: 2024-01-15

# You can change the line ending
print("Loading", end="...")         # Output: Loading...
print("Done!")                       # Output: Done!
```

### Python as a calculator (REPL)

```python
# In your terminal, type: python3
# Then try these:
>>> 2 + 2
4
>>> 10 / 3
3.3333333333333335
>>> 2 ** 10
1024
>>> exit()  # Leave the REPL
```

---

## Today's Project: Personal Info Card

> Build a formatted personal information card that displays your name, age, city, and a fun fact.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 01 Project: Personal Info Card
===================================
Print a formatted card showing personal information.
"""

# Personal information (change these to your own!)
name = "Alice Johnson"
age = 28
city = "San Francisco"
occupation = "Software Developer"
fun_fact = "I can solve a Rubik's cube in under 2 minutes"
favorite_language = "Python"

# Print a formatted info card
print("=" * 45)
print("       PERSONAL INFO CARD")
print("=" * 45)
print(f"  Name        : {name}")
print(f"  Age         : {age}")
print(f"  City        : {city}")
print(f"  Occupation  : {occupation}")
print(f"  Fun Fact    : {fun_fact}")
print(f"  Fav Language: {favorite_language}")
print("=" * 45)
print("  Happy coding! 🐍")
print("=" * 45)
```

---

## Knowledge Check

Before moving on, make sure you can answer these:

1. How do you run a Python script from the terminal?
2. What is the difference between `print("a", "b")` and `print("a" + "b")`?
3. Can you explain what happens when Python reads your file top to bottom?
4. What does the `#` symbol do in Python?
5. How do you enter and exit the Python REPL?

---

## Common Mistakes to Avoid

```python
# WRONG - mixing indentation
if True:
    print("hello")
  print("world")  # IndentationError

# CORRECT - consistent 4-space indentation
if True:
    print("hello")
    print("world")
```

---

<div align="center">

| ← This is the first lesson | [🏠 Home](../../README.md) | [Day 02: Next Lesson →](../day-02/README.md) |
|:---|:---:|---:|

</div>
