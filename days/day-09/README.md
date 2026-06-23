# Day 09 🔀 - Conditionals

<div align="center">

| [← Day 08: Previous Lesson](../day-08/README.md) | [🏠 Home](../../README.md) | [Day 10: Next Lesson →](../day-10/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Write programs that make decisions. `if`, `elif`, and `else` are the backbone of every program that responds differently to different inputs.

**What you will learn today:**

- `if`, `elif`, `else` syntax
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Chaining conditions with `and`, `or`, `not`
- The ternary (one-line) operator
- Nested conditionals
- Python 3.10+ `match` statement

---

## Key Concepts

| Concept | Description |
|---|---|
| `if / elif / else` | Execute different blocks of code based on conditions. Python uses indentation (4 spaces) to define blocks. |
| `Comparison operators` | `==` checks equality. `=` is assignment. One of the most common beginner mistakes is mixing them up. |
| `Ternary operator` | One-line conditional: `value_if_true if condition else value_if_false`. |
| `match statement` | Python 3.10+ structural pattern matching. Cleaner than long `elif` chains for matching values. |

---

## Code Examples

### if / elif / else

```python
temperature = 22

if temperature < 0:
    print("Freezing! Stay inside.")
elif temperature < 10:
    print("Cold. Wear a coat.")
elif temperature < 20:
    print("Cool. A light jacket works.")
elif temperature < 30:
    print("Comfortable. Enjoy the weather!")
else:
    print("Hot! Stay hydrated.")

# Multiple conditions with and/or
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
elif age >= 18 and not has_id:
    print("Please bring your ID next time.")
else:
    print("Entry denied. Must be 18+.")
```

### Ternary and match

```python
# Ternary operator (one-line if/else)
score = 75
grade = "Pass" if score >= 60 else "Fail"
print(grade)   # Pass

# Longer example
age = 20
status = "adult" if age >= 18 else "minor"

# match statement (Python 3.10+)
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":
        print("Stopping.")
    case _:
        print(f"Unknown command: {command}")
```

---

## Today's Project: BMI Calculator

> Calculate a user's Body Mass Index from their weight and height, then classify the result and provide context.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 09 Project: BMI Calculator
================================
Calculate and classify BMI from weight and height.
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI. Raises ValueError for invalid inputs."""
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> tuple[str, str]:
    """Return the BMI category and advice."""
    if bmi < 18.5:
        return "Underweight", "Consider consulting a nutritionist."
    elif bmi < 25:
        return "Normal weight", "Great! Maintain your healthy lifestyle."
    elif bmi < 30:
        return "Overweight", "Regular exercise and a balanced diet can help."
    else:
        return "Obese", "Please consult a healthcare professional."


def main() -> None:
    print("=" * 45)
    print("           BMI CALCULATOR")
    print("=" * 45)

    try:
        weight = float(input("\nEnter your weight (kg): "))
        height_cm = float(input("Enter your height (cm): "))
        height_m = height_cm / 100

        bmi = calculate_bmi(weight, height_m)
        category, advice = classify_bmi(bmi)

        print(f"\n  BMI       : {bmi:.1f}")
        print(f"  Category  : {category}")
        print(f"  Advice    : {advice}")

        # Visual BMI bar
        bar_pos = min(max(int((bmi - 10) / 30 * 30), 0), 30)
        bar = "-" * bar_pos + "^" + "-" * (30 - bar_pos)
        print(f"\n  [Underweight|Normal|Overweight|Obese]")
        print(f"  [{bar}]")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain:

1. What is the main concept covered today?
2. Write a short example from memory.
3. What is one common mistake with this concept?
4. How will you use this in real projects?

---

<div align="center">

| [← Day 08: Previous Lesson](../day-08/README.md) | [🏠 Home](../../README.md) | [Day 10: Next Lesson →](../day-10/README.md) |
|:---|:---:|---:|

</div>
