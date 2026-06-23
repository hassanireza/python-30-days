# Day 07 🎯 - Tuples, Sets & Booleans

<div align="center">

| [← Day 06: Previous Lesson](../day-06/README.md) | [🏠 Home](../../README.md) | [Day 08: Next Lesson →](../day-08/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Understand when to use tuples (immutable sequences), sets (unique collections), and how Boolean logic powers decisions in your code.

**What you will learn today:**

- Tuples: immutable sequences
- When to use tuples vs lists
- Sets: unordered unique collections
- Set operations: union, intersection, difference
- Boolean operators: `and`, `or`, `not`
- Truthiness and falsy values

---

## Key Concepts

| Concept | Description |
|---|---|
| `tuple` | An immutable sequence. Use when data should not change: coordinates, RGB values, database records. |
| `set` | An unordered collection of unique items. Adding a duplicate has no effect. |
| `frozenset` | An immutable version of a set. |
| `Truthy/Falsy` | In Python, `0`, `''`, `[]`, `{}`, `None` are all falsy. Everything else is truthy. |

---

## Code Examples

### Tuples

```python
# Create with parentheses (or just commas)
point = (10, 20)
rgb = (255, 128, 0)
single = (42,)          # Note the trailing comma for single-item tuples

# Unpack tuples
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

# Tuples are immutable
# point[0] = 5  # TypeError: 'tuple' object does not support item assignment

# Functions can return multiple values as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)  # 1 9
```

### Sets

```python
# Create a set with curly braces
unique_colors = {"red", "green", "blue", "red", "green"}
print(unique_colors)    # {'blue', 'green', 'red'} - duplicates removed

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)    # Union:        {1,2,3,4,5,6,7,8}
print(a & b)    # Intersection: {4, 5}
print(a - b)    # Difference:   {1, 2, 3}
print(a ^ b)    # Symmetric diff: {1,2,3,6,7,8}

# Fast membership testing
words = {"hello", "world", "python"}
print("python" in words)    # True - O(1) average time
```

### Boolean logic

```python
# Boolean operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Short-circuit evaluation
x = None
name = x or "default"  # "default" (x is falsy)
print(name)

# Falsy values: 0, 0.0, "", [], {}, set(), None, False
values = [0, "", [], None, False, 42, "hi", [1]]
for v in values:
    status = "truthy" if v else "falsy"
    print(f"{str(v):<10} is {status}")
```

---

## Today's Project: Unique Word Counter

> Read a block of text from the user and report unique word count, most common words, and set operations on two texts.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 07 Project: Unique Word Counter
=====================================
Analyze text for unique words using sets.
"""
import string


def clean_words(text: str) -> set[str]:
    """Extract a set of unique lowercase words from text."""
    # Remove punctuation and split into words
    translator = str.maketrans("", "", string.punctuation)
    cleaned = text.lower().translate(translator)
    return set(cleaned.split())


def word_frequency(text: str) -> dict[str, int]:
    """Count how often each word appears."""
    translator = str.maketrans("", "", string.punctuation)
    words = text.lower().translate(translator).split()
    freq: dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def main() -> None:
    print("=" * 50)
    print("         UNIQUE WORD COUNTER")
    print("=" * 50)

    print("\nPaste Text 1 (press Enter twice when done):")
    lines1 = []
    while True:
        line = input()
        if line == "":
            break
        lines1.append(line)
    text1 = " ".join(lines1)

    print("\nPaste Text 2 (press Enter twice when done):")
    lines2 = []
    while True:
        line = input()
        if line == "":
            break
        lines2.append(line)
    text2 = " ".join(lines2)

    words1 = clean_words(text1)
    words2 = clean_words(text2)
    freq1 = word_frequency(text1)

    print(f"\n--- Text 1 Analysis ---")
    print(f"Total unique words : {len(words1)}")
    top5 = sorted(freq1, key=freq1.get, reverse=True)[:5]
    print(f"Top 5 words        : {top5}")

    print(f"\n--- Comparison ---")
    print(f"Words in both      : {words1 & words2}")
    print(f"Only in Text 1     : {words1 - words2}")
    print(f"Only in Text 2     : {words2 - words1}")


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

| [← Day 06: Previous Lesson](../day-06/README.md) | [🏠 Home](../../README.md) | [Day 08: Next Lesson →](../day-08/README.md) |
|:---|:---:|---:|

</div>
