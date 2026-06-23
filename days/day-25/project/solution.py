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
