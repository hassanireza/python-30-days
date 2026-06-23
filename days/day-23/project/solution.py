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
