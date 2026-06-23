# Day 27 📊 - JSON & CSV Data

<div align="center">

| [← Day 26: Previous Lesson](../day-26/README.md) | [🏠 Home](../../README.md) | [Day 28: Next Lesson →](../day-28/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

JSON and CSV are the two most common data formats you will encounter. Learn to read, write, and process both with Python's standard library.

**What you will learn today:**

- Reading and writing JSON with the `json` module
- Pretty-printing JSON with `indent=2`
- Reading CSV with `csv.DictReader`
- Writing CSV with `csv.DictWriter`
- Using `pathlib` for clean file handling
- Converting between JSON and Python objects

---

## Key Concepts

| Concept | Description |
|---|---|
| `json.dumps()` | Serialize a Python object to a JSON string. Use `indent=2` for readable output. |
| `json.loads()` | Parse a JSON string into a Python object. |
| `json.load() / json.dump()` | Read/write JSON directly to/from a file object. |
| `csv.DictReader` | Read CSV rows as dicts keyed by column header. |
| `csv.DictWriter` | Write dicts to CSV. Specify `fieldnames` to control column order. |

---

## Code Examples

### JSON read and write

```python
import json
from pathlib import Path

data = {
    "name": "Alice",
    "scores": [95, 87, 92],
    "active": True,
    "address": None,
}

# Python -> JSON string
json_str = json.dumps(data, indent=2)
print(json_str)

# JSON string -> Python
parsed = json.loads(json_str)
print(parsed["name"])       # Alice

# Write to file
Path("data.json").write_text(json.dumps(data, indent=2))

# Read from file
with open("data.json") as f:
    loaded = json.load(f)
print(loaded)
```

### CSV read and write

```python
import csv

students = [
    {"name": "Alice", "grade": 92, "subject": "Math"},
    {"name": "Bob",   "grade": 78, "subject": "Science"},
]

# Write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "grade", "subject"])
    writer.writeheader()
    writer.writerows(students)

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['grade']} in {row['subject']}")
```

---

## Today's Project: Grade Book

> Build a grade book that loads CSV data, computes statistics, exports to JSON, and prints a formatted report.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 27 Project: Grade Book
===========================
Read CSV grades, compute stats, export JSON, print report.
"""
import csv
import json
import statistics
from pathlib import Path

SAMPLE_CSV = """name,math,science,english,history
Alice,92,88,95,90
Bob,78,82,74,85
Charlie,65,70,80,72
Diana,95,98,92,96
Eve,55,60,58,62
Frank,88,75,82,79
"""

CSV_FILE  = Path("grades.csv")
JSON_FILE = Path("grades.json")


def letter_grade(avg: float) -> str:
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"


def load_grades(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        records = []
        for row in reader:
            name     = row.pop("name")
            grades   = {k: int(v) for k, v in row.items()}
            average  = round(sum(grades.values()) / len(grades), 1)
            records.append({"name": name, "grades": grades,
                             "average": average, "letter": letter_grade(average)})
    return records


def print_report(records: list[dict]) -> None:
    subjects = list(records[0]["grades"].keys())
    w = 10
    print("\n" + "=" * 70)
    print("                        GRADE REPORT")
    print("=" * 70)
    hdr = f"  {'Name':<12}" + "".join(f"{s.capitalize():>{w}}" for s in subjects) + f"  {'Avg':>6}  Grade"
    print(hdr)
    print("  " + "-" * 68)
    for r in sorted(records, key=lambda x: x["average"], reverse=True):
        cols = "".join(f"{r['grades'][s]:>{w}}" for s in subjects)
        print(f"  {r['name']:<12}{cols}  {r['average']:>6.1f}  {r['letter']}")
    print("  " + "-" * 68)
    print("\n  Subject Averages:")
    for subj in subjects:
        vals = [r["grades"][subj] for r in records]
        print(f"    {subj.capitalize():<12} avg={statistics.mean(vals):.1f}  "
              f"min={min(vals)}  max={max(vals)}  stdev={statistics.stdev(vals):.1f}")
    all_avgs = [r["average"] for r in records]
    top = max(records, key=lambda x: x["average"])
    print(f"\n  Class average  : {statistics.mean(all_avgs):.1f}")
    print(f"  Top student    : {top['name']} ({top['average']}%)")
    print("=" * 70)


def main() -> None:
    CSV_FILE.write_text(SAMPLE_CSV)
    records = load_grades(CSV_FILE)
    print_report(records)
    JSON_FILE.write_text(json.dumps(records, indent=2))
    print(f"\n  Exported to {JSON_FILE}")
    CSV_FILE.unlink(missing_ok=True)
    JSON_FILE.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain each concept without looking at the lesson.

---

<div align="center">

| [← Day 26: Previous Lesson](../day-26/README.md) | [🏠 Home](../../README.md) | [Day 28: Next Lesson →](../day-28/README.md) |
|:---|:---:|---:|

</div>
