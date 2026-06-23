# Day 25 🔒 - Context Managers

<div align="center">

| [← Day 24: Previous Lesson](../day-24/README.md) | [🏠 Home](../../README.md) | [Day 26: Next Lesson →](../day-26/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Context managers ensure resources are properly acquired and released - even when errors occur. The `with` statement is Python's way of making this automatic.

**What you will learn today:**

- The `with` statement and why it exists
- How `__enter__` and `__exit__` work
- Using `contextlib.contextmanager` with `yield`
- Writing reusable context managers
- Nested context managers
- Common use cases: files, locks, timing, temp directories

---

## Key Concepts

| Concept | Description |
|---|---|
| `with` | Guarantees cleanup code runs, even if an exception occurs inside the block. |
| `__enter__` | Called when entering the `with` block. The return value is bound to the `as` variable. |
| `__exit__` | Called when leaving the block, receiving exception info if one occurred. Return `True` to suppress the exception. |
| `@contextmanager` | Decorator from `contextlib` that turns a generator function into a context manager. Much simpler than a class. |

---

## Code Examples

### Class-based context manager

```python
class Timer:
    """Context manager that measures elapsed time."""
    import time

    def __enter__(self):
        import time
        self._start = time.perf_counter()
        return self          # bound to the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False         # do not suppress exceptions


with Timer() as t:
    total = sum(range(1_000_000))

print(f"Result: {total}")
print(f"Time: {t.elapsed:.4f}s")
```

### contextlib.contextmanager

```python
from contextlib import contextmanager
import os
import tempfile


@contextmanager
def temp_directory():
    """Create a temporary directory and clean it up afterward."""
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()
    print(f"Created temp dir: {tmpdir}")
    try:
        yield tmpdir          # pause and hand control to the `with` block
    finally:
        shutil.rmtree(tmpdir) # always runs
        print(f"Cleaned up: {tmpdir}")


with temp_directory() as tmpdir:
    # Create files in the temp directory
    filepath = os.path.join(tmpdir, "test.txt")
    with open(filepath, "w") as f:
        f.write("Temporary data")
    print(f"File exists: {os.path.exists(filepath)}")

print(f"After block - dir gone: {not os.path.exists(tmpdir)}")
```

---

## Today's Project: File Manager Context Manager

> Build a collection of context managers for safe file operations, atomic writes, and managed working directories.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 25 Project: File Manager Context Managers
================================================
Safe file operations using context managers.
"""
import os
import shutil
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path


class SafeWriter:
    """Write to a file atomically: write to temp file, then rename.

    This prevents partial writes from corrupting the target file.
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._tmp_path: Path | None = None
        self._file = None

    def __enter__(self):
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, prefix=".tmp_")
        os.close(fd)
        self._tmp_path = Path(tmp)
        self._file = open(self._tmp_path, "w", encoding="utf-8")
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        if exc_type is None:
            # Success: replace target with temp file
            self._tmp_path.replace(self.path)
            print(f"  [SafeWriter] Committed -> {self.path}")
        else:
            # Error: delete temp file, do not touch original
            self._tmp_path.unlink(missing_ok=True)
            print(f"  [SafeWriter] Rolled back (exception: {exc_type.__name__})")
        return False  # do not suppress exceptions


@contextmanager
def working_directory(path: str | Path):
    """Temporarily change the working directory."""
    original = Path.cwd()
    os.chdir(path)
    print(f"  [CD] -> {path}")
    try:
        yield Path(path)
    finally:
        os.chdir(original)
        print(f"  [CD] <- {original}")


@contextmanager
def timer(label: str = ""):
    """Measure execution time of a block."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        tag = f"[{label}] " if label else ""
        print(f"  {tag}elapsed: {elapsed*1000:.2f}ms")


def main() -> None:
    print("=" * 55)
    print("         FILE MANAGER DEMO")
    print("=" * 55)

    # Demo 1: Safe atomic write
    print("\n1. SafeWriter (atomic write):")
    with SafeWriter("output.txt") as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    print(f"   File content: {Path('output.txt').read_text().strip()!r}")
    Path("output.txt").unlink(missing_ok=True)

    # Demo 2: working_directory
    print("\n2. working_directory context manager:")
    with tempfile.TemporaryDirectory() as tmpdir:
        with working_directory(tmpdir):
            print(f"   Inside: {Path.cwd()}")
            Path("local.txt").write_text("hello")
        print(f"   Back to: {Path.cwd()}")

    # Demo 3: timer
    print("\n3. timer context manager:")
    with timer("sum 1M"):
        result = sum(range(1_000_000))
    print(f"   Result: {result}")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain each concept without looking at the lesson.

---

<div align="center">

| [← Day 24: Previous Lesson](../day-24/README.md) | [🏠 Home](../../README.md) | [Day 26: Next Lesson →](../day-26/README.md) |
|:---|:---:|---:|

</div>
