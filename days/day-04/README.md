# Day 04 🔢 - Numbers & Math Operations

<div align="center">

| [← Day 03: Previous Lesson](../day-03/README.md) | [🏠 Home](../../README.md) | [Day 05: Next Lesson →](../day-05/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Work with integers, floats, and Python's math module to perform calculations from basic arithmetic to trigonometry.

**What you will learn today:**

- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operator precedence (PEMDAS/BODMAS)
- Integer vs float division
- The `math` module
- `round()`, `abs()`, `min()`, `max()`
- Augmented assignment operators

---

## Key Concepts

| Concept | Description |
|---|---|
| ``//` Floor Division` | Divides and rounds down to the nearest integer. `7 // 2` gives `3`, not `3.5`. |
| ``%` Modulo` | Returns the remainder after division. `7 % 2` gives `1`. Great for checking if a number is even. |
| ``**` Exponentiation` | Raises to a power. `2 ** 8` gives `256`. Much more readable than `pow(2, 8)`. |
| `Augmented assignment` | Shortcuts like `x += 5` are equivalent to `x = x + 5`. |

---

## Code Examples

### All arithmetic operators

```python
a = 17
b = 5

print(a + b)   # 22   Addition
print(a - b)   # 12   Subtraction
print(a * b)   # 85   Multiplication
print(a / b)   # 3.4  True division (always float)
print(a // b)  # 3    Floor division (rounds down)
print(a % b)   # 2    Modulo (remainder)
print(a ** b)  # 1419857  Exponentiation

# Augmented assignment
score = 100
score += 10   # score = 110
score -= 5    # score = 105
score *= 2    # score = 210
score //= 3   # score = 70
print(score)  # 70
```

### The math module

```python
import math

print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828459045

print(math.sqrt(144))       # 12.0
print(math.ceil(4.1))       # 5   (round up)
print(math.floor(4.9))      # 4   (round down)
print(math.factorial(5))    # 120 (5!)
print(math.log(100, 10))    # 2.0 (log base 10 of 100)
print(math.sin(math.pi/2))  # 1.0 (sin of 90 degrees)

# Practical: area of a circle
radius = 7
area = math.pi * radius ** 2
print(f"Area: {area:.2f}")  # Area: 153.94
```

---

## Today's Project: Scientific Calculator

> Build a CLI calculator that handles all arithmetic operations plus square root, power, and percentage calculations.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 04 Project: Scientific Calculator
=======================================
A command-line calculator with multiple operations.
"""
import math


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base: float, exp: float) -> float:
    """Return base raised to the power of exp."""
    return base ** exp


def square_root(n: float) -> float:
    """Return the square root of n. Raises ValueError if n < 0."""
    if n < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(n)


def main() -> None:
    """Run the interactive calculator."""
    operations = {
        "1": ("Addition (+)", add, 2),
        "2": ("Subtraction (-)", subtract, 2),
        "3": ("Multiplication (*)", multiply, 2),
        "4": ("Division (/)", divide, 2),
        "5": ("Power (^)", power, 2),
        "6": ("Square Root (√)", square_root, 1),
    }

    print("=" * 40)
    print("       SCIENTIFIC CALCULATOR")
    print("=" * 40)

    while True:
        print("\nSelect operation:")
        for key, (name, _, _) in operations.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("\nYour choice: ").strip().lower()

        if choice == "q":
            print("\nGoodbye! Keep calculating. 🔢")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        name, func, num_args = operations[choice]

        try:
            if num_args == 2:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = func(a, b)
                print(f"\nResult: {a} {name[name.index('(')+1]} {b} = {result}")
            else:
                a = float(input("Enter number: "))
                result = func(a)
                print(f"\nResult: {result:.6f}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
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

| [← Day 03: Previous Lesson](../day-03/README.md) | [🏠 Home](../../README.md) | [Day 05: Next Lesson →](../day-05/README.md) |
|:---|:---:|---:|

</div>
