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
