# Day 12 ⚙️ - Functions Basics

<div align="center">

| [← Day 11: Previous Lesson](../day-11/README.md) | [🏠 Home](../../README.md) | [Day 13: Next Lesson →](../day-13/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Functions let you write code once and reuse it everywhere. Learn to define functions, pass arguments, return values, and write proper docstrings.

**What you will learn today:**

- Defining functions with `def`
- Parameters vs arguments
- Return values and `return`
- Default parameter values
- Docstrings (PEP 257)
- The DRY principle (Don't Repeat Yourself)

---

## Key Concepts

| Concept | Description |
|---|---|
| `def` | Defines a function. The function body runs only when the function is called. |
| `parameters` | Variables listed in the function definition: `def greet(name, greeting):` |
| `arguments` | The actual values passed when calling the function: `greet('Alice', 'Hello')`. |
| `return` | Sends a value back to the caller. A function without `return` returns `None`. |
| `docstring` | A string literal as the first statement of a function. Explains what the function does. |

---

## Code Examples

### Defining and calling functions

```python
# Define once, call anywhere
def greet(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!
print(greet("Bob"))     # Hello, Bob!


# Default parameter values
def power(base: float, exp: float = 2) -> float:
    """Return base raised to exp. Default is squaring."""
    return base ** exp

print(power(3))       # 9.0  (uses default exp=2)
print(power(2, 10))   # 1024.0
```

### Return values

```python
# Functions can return any type
def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0

print(is_even(4))    # True
print(is_even(7))    # False

# Return multiple values (as a tuple)
def stats(numbers: list[float]) -> tuple[float, float, float]:
    """Return the min, max, and average of a list."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = stats([4, 7, 2, 9, 1])
print(f"Min: {low}, Max: {high}, Avg: {avg:.1f}")

# Early return
def safe_divide(a: float, b: float) -> float | None:
    """Divide a by b, or return None if b is zero."""
    if b == 0:
        return None     # Early exit
    return a / b
```

---

## Today's Project: Password Generator

> Build a function-based password generator that creates secure random passwords based on user-specified length and character sets.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 12 Project: Password Generator
====================================
Generate secure random passwords using functions.
"""
import random
import string


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a secure random password.

    Args:
        length: Number of characters in the password (default 16).
        use_upper: Include uppercase letters.
        use_lower: Include lowercase letters.
        use_digits: Include digits.
        use_symbols: Include symbols.

    Returns:
        A random password string.

    Raises:
        ValueError: If no character sets are selected or length is too short.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    charset = ""
    guaranteed: list[str] = []

    if use_upper:
        charset += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        charset += string.ascii_lowercase
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        charset += string.digits
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        charset += string.punctuation
        guaranteed.append(random.choice(string.punctuation))

    if not charset:
        raise ValueError("Select at least one character type.")

    remaining_length = length - len(guaranteed)
    rest = [random.choice(charset) for _ in range(remaining_length)]
    all_chars = guaranteed + rest
    random.shuffle(all_chars)
    return "".join(all_chars)


def rate_password(password: str) -> str:
    """Rate the strength of a password."""
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    ratings = {5: "Very Strong", 4: "Strong", 3: "Moderate", 2: "Weak", 1: "Very Weak"}
    return ratings.get(score, "Very Weak")


def main() -> None:
    print("=" * 45)
    print("         PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("\nPassword length (default 16): ") or "16")
        use_upper = input("Include uppercase? (Y/n): ").strip().lower() != "n"
        use_lower = input("Include lowercase? (Y/n): ").strip().lower() != "n"
        use_digits = input("Include digits? (Y/n): ").strip().lower() != "n"
        use_symbols = input("Include symbols? (Y/n): ").strip().lower() != "n"
        count = int(input("How many passwords? (default 5): ") or "5")

        print(f"\n{'Password':<{length + 4}} Strength")
        print("-" * (length + 20))
        for _ in range(count):
            pw = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            strength = rate_password(pw)
            print(f"  {pw:<{length + 2}} {strength}")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain:

1. What is the main concept covered today?
2. Write a short example from memory without looking at the lesson.
3. What is one common mistake with this concept, and how do you avoid it?
4. How will you use this in real projects?

---

<div align="center">

| [← Day 11: Previous Lesson](../day-11/README.md) | [🏠 Home](../../README.md) | [Day 13: Next Lesson →](../day-13/README.md) |
|:---|:---:|---:|

</div>
