# Day 14 🔭 - Scope & Closures

<div align="center">

| [← Day 13: Previous Lesson](../day-13/README.md) | [🏠 Home](../../README.md) | [Day 15: Next Lesson →](../day-15/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Understanding scope tells you where a variable can be accessed. Closures take this further, letting inner functions remember their enclosing environment.

**What you will learn today:**

- The LEGB rule: Local, Enclosing, Global, Built-in
- `global` keyword to modify module-level variables
- `nonlocal` keyword to modify enclosing scope variables
- What a closure is and when to use one
- Practical closure patterns
- Why closures matter for decorators (preview)

---

## Key Concepts

| Concept | Description |
|---|---|
| `LEGB rule` | Python looks up names in this order: Local scope, then Enclosing function scope, then Global (module) scope, then Built-in names. |
| `global` | Declares that a variable inside a function refers to the module-level name. Use sparingly. |
| `nonlocal` | Lets an inner function modify a variable in its enclosing (but not global) scope. |
| `closure` | A function that remembers variables from its enclosing scope even after the outer function has returned. |

---

## Code Examples

### LEGB and global

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # local (local scope wins)

    inner()
    print(x)        # enclosing

outer()
print(x)            # global


# global keyword
count = 0

def increment():
    global count    # modify the module-level count
    count += 1

increment()
increment()
print(count)        # 2
```

### Closures

```python
def make_counter(start: int = 0, step: int = 1):
    """Return a counter function that remembers its state."""
    current = start

    def counter() -> int:
        nonlocal current
        value = current
        current += step
        return value

    return counter      # Return the function, not the result!

count_by_one = make_counter()
count_by_five = make_counter(step=5)

print(count_by_one())   # 0
print(count_by_one())   # 1
print(count_by_one())   # 2
print(count_by_five())  # 0
print(count_by_five())  # 5
# Each closure has its own independent state!
```

---

## Today's Project: Counter Factory

> Build a closure-based counter factory that creates independent counters with configurable start, step, and max values.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 14 Project: Counter Factory
=================================
Closure-powered independent counters.
"""
from typing import Callable


def make_counter(
    start: int = 0,
    step: int = 1,
    max_value: int | None = None,
    cycle: bool = False,
) -> Callable[[], int | None]:
    """Create an independent counter function.

    Args:
        start: Initial value (default 0).
        step: Increment per call (default 1).
        max_value: Upper bound. None means unlimited.
        cycle: If True, resets to start when max_value is reached.

    Returns:
        A callable that returns the next counter value,
        or None if max_value was reached and cycle is False.
    """
    current = start

    def counter() -> int | None:
        nonlocal current

        if max_value is not None and current > max_value:
            if cycle:
                current = start
            else:
                return None

        value = current
        current += step
        return value

    return counter


def main() -> None:
    print("=" * 45)
    print("          COUNTER FACTORY DEMO")
    print("=" * 45)

    # Standard counter
    c1 = make_counter(start=1)
    print("\nCounter 1 (start=1, step=1):", [c1() for _ in range(5)])

    # Step counter
    c2 = make_counter(start=0, step=10)
    print("Counter 2 (start=0, step=10):", [c2() for _ in range(5)])

    # Cycling counter
    c3 = make_counter(start=1, step=1, max_value=3, cycle=True)
    print("Counter 3 (cycling 1-3):", [c3() for _ in range(9)])

    # Bounded counter
    c4 = make_counter(start=10, step=-2, max_value=10)
    print("Counter 4 (countdown from 10):", end=" ")
    results = []
    while (val := c4()) is not None:
        results.append(val)
    print(results)

    print("\nAll counters are independent - they never interfere with each other!")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain each concept without looking at the lesson.

---

<div align="center">

| [← Day 13: Previous Lesson](../day-13/README.md) | [🏠 Home](../../README.md) | [Day 15: Next Lesson →](../day-15/README.md) |
|:---|:---:|---:|

</div>
