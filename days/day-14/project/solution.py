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
