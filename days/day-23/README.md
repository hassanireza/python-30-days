# Day 23 🎀 - Decorators

<div align="center">

| [← Day 22: Previous Lesson](../day-22/README.md) | [🏠 Home](../../README.md) | [Day 24: Next Lesson →](../day-24/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Decorators modify or enhance functions without changing their source code. They are used everywhere in Python frameworks for caching, logging, authentication, and more.

**What you will learn today:**

- What a decorator is and how it works
- Writing your first decorator
- `@functools.wraps` to preserve metadata
- Decorators with arguments
- Stacking multiple decorators
- Real-world decorator patterns

---

## Key Concepts

| Concept | Description |
|---|---|
| `decorator` | A function that takes another function and returns a modified version of it. Applied with the `@` syntax. |
| `@wraps` | From `functools`. Copies the original function's name, docstring, and metadata to the wrapper. Always use it. |
| `closure` | Decorators rely on closures: the inner `wrapper` function closes over the original `func`. |
| `parametrized decorator` | A decorator factory: a function that returns a decorator. Needs three levels of nesting. |

---

## Code Examples

### Your first decorator

```python
import functools
import time


def timer(func):
    """Measure and print execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [{func.__name__}] ran in {elapsed:.4f}s")
        return result
    return wrapper


@timer
def slow_sum(n: int) -> int:
    """Sum numbers from 0 to n."""
    return sum(range(n))


result = slow_sum(1_000_000)
print(result)    # 499999500000
# [slow_sum] ran in 0.0312s
```

### Decorators with arguments

```python
import functools


def repeat(times: int):
    """Return a decorator that calls the function `times` times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(times=3)
def greet(name: str) -> str:
    print(f"Hello, {name}!")
    return f"Hello, {name}!"


greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

---

## Today's Project: Function Profiler

> Build a decorator toolkit with `@timer`, `@retry`, `@cache`, and `@log_calls` to profile and enhance functions.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 23 Project: Function Profiler Decorator Toolkit
=====================================================
A set of useful, production-quality decorators.
"""
import functools
import time
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable)


def timer(func: F) -> F:
    """Measure and print the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [TIMER] {func.__name__}() -> {elapsed*1000:.3f}ms")
        return result
    return wrapper  # type: ignore


def retry(times: int = 3, exceptions: tuple = (Exception,), delay: float = 0.0):
    """Retry a function up to `times` times on specified exceptions."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    print(f"  [RETRY] {func.__name__}() attempt {attempt}/{times} failed: {e}")
                    if delay and attempt < times:
                        time.sleep(delay)
            raise last_exc  # type: ignore
        return wrapper  # type: ignore
    return decorator


def memoize(func: F) -> F:
    """Cache function results for identical arguments."""
    cache: dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(f"  [CACHE MISS] {func.__name__}{args}")
        else:
            print(f"  [CACHE HIT]  {func.__name__}{args}")
        return cache[args]

    wrapper.cache = cache  # type: ignore
    return wrapper  # type: ignore


def log_calls(func: F) -> F:
    """Log every call to a function with its arguments and return value."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
        result = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__}({arg_str}) -> {result!r}")
        return result
    return wrapper  # type: ignore


# --- Demo ---

@timer
@log_calls
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@memoize
def fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


import random

@retry(times=3, exceptions=(ValueError,))
def flaky_function() -> str:
    """Randomly fails to simulate an unreliable operation."""
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"


def main() -> None:
    print("=" * 55)
    print("          DECORATOR TOOLKIT DEMO")
    print("=" * 55)

    print("\n1. @timer + @log_calls (stacked):")
    add(10, 20)

    print("\n2. @memoize (caching Fibonacci):")
    for n in [5, 5, 7, 5]:
        print(f"  fibonacci({n}) = {fibonacci(n)}")

    print("\n3. @retry (unreliable function):")
    try:
        result = flaky_function()
        print(f"  Result: {result}")
    except ValueError:
        print("  All retries failed.")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain each concept without looking at the lesson.

---

<div align="center">

| [← Day 22: Previous Lesson](../day-22/README.md) | [🏠 Home](../../README.md) | [Day 24: Next Lesson →](../day-24/README.md) |
|:---|:---:|---:|

</div>
