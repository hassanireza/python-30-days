# Day 26 🔍 - Regular Expressions

<div align="center">

| [← Day 25: Previous Lesson](../day-25/README.md) | [🏠 Home](../../README.md) | [Day 27: Next Lesson →](../day-27/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Regular expressions are a mini language for matching patterns in text. Master them and you can parse, validate, and transform any text data.

**What you will learn today:**

- The `re` module: `re.match()`, `re.search()`, `re.findall()`, `re.sub()`
- Character classes: `\d`, `\w`, `\s`, `[abc]`
- Quantifiers: `*`, `+`, `?`, `{n,m}`
- Groups `()` and named groups `(?P<name>...)`
- Flags: `re.IGNORECASE`, `re.MULTILINE`
- Compiling patterns with `re.compile()`

---

## Key Concepts

| Concept | Description |
|---|---|
| `re.search()` | Search anywhere in the string for the pattern. Returns a Match object or None. |
| `re.findall()` | Return all non-overlapping matches as a list of strings. |
| `re.sub()` | Replace all matches with a replacement string. |
| `re.compile()` | Pre-compile a pattern for reuse — more efficient when the same pattern is used many times. |

---

## Code Examples

### Core regex patterns

```python
import re

text = "Alice's email is alice@example.com and her phone is 415-555-1234"

# Search anywhere in the string
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(match.group())    # 415-555-1234

# Find all email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)               # ['alice@example.com']

# Named groups
pattern = re.compile(r"(?P<area>\d{3})-(?P<exchange>\d{3})-(?P<line>\d{4})")
m = pattern.search(text)
if m:
    print(m.group("area"))      # 415
    print(m.group("exchange"))  # 555
```

### re.sub and flags

```python
import re

# Remove all punctuation
text = "Hello, World! How are you?"
clean = re.sub(r"[^\w\s]", "", text)
print(clean)    # Hello World How are you

# IGNORECASE flag
sentence = "Python is great. PYTHON rocks. python wins."
count = len(re.findall(r"python", sentence, re.IGNORECASE))
print(count)    # 3

# MULTILINE: ^ matches start of each line
multiline = "first\nsecond\nthird"
starts = re.findall(r"^\w+", multiline, re.MULTILINE)
print(starts)   # ['first', 'second', 'third']
```

---

## Today's Project: Text Parser

> Extract emails, phone numbers, URLs, and names from raw text using compiled regex patterns.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 26 Project: Text Parser
=============================
Extract structured data from unstructured text using regex.
"""
import re


EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")
URL_RE   = re.compile(r"https?://(?:www\.)?[-\w@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-\w()@:%_+.~#?&/=]*")
NAME_RE  = re.compile(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b")


def extract_all(text: str) -> dict[str, list[str]]:
    """Extract emails, phones, URLs, and names from text."""
    return {
        "emails": EMAIL_RE.findall(text),
        "phones": PHONE_RE.findall(text),
        "urls":   URL_RE.findall(text),
        "names":  NAME_RE.findall(text),
    }


def mask_email(email: str) -> str:
    """Mask an email: al***@example.com"""
    local, domain = email.split("@", 1)
    return local[:2] + "***@" + domain


def validate_email(email: str) -> bool:
    """Return True if email looks valid."""
    return bool(EMAIL_RE.fullmatch(email))


SAMPLE = """
Contact us at support@example.com or sales@company.org.
Reach Alice Johnson at 415-555-1234 or (800) 555-9876.
Visit https://www.example.com or http://docs.example.com.
Email Bob Smith at press@newsroom.io for press inquiries.
"""


def main() -> None:
    print("=" * 55)
    print("              TEXT PARSER")
    print("=" * 55)

    results = extract_all(SAMPLE)
    print(f"\nEmails  : {results['emails']}")
    print(f"Phones  : {results['phones']}")
    print(f"URLs    : {results['urls']}")
    print(f"Names   : {results['names']}")

    print("\nMasked emails:")
    for email in results["emails"]:
        print(f"  {email} -> {mask_email(email)}")

    print("\nEmail validation:")
    tests = ["valid@example.com", "not-an-email", "also@valid.org", "@missing.com"]
    for t in tests:
        status = "VALID" if validate_email(t) else "INVALID"
        print(f"  {t:<28} {status}")

    pattern_str = input("\nEnter a regex pattern to test (or press Enter to skip): ").strip()
    if pattern_str:
        try:
            matches = re.findall(pattern_str, SAMPLE)
            print(f"  Matches: {matches}")
        except re.error as e:
            print(f"  Invalid pattern: {e}")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain each concept without looking at the lesson.

---

<div align="center">

| [← Day 25: Previous Lesson](../day-25/README.md) | [🏠 Home](../../README.md) | [Day 27: Next Lesson →](../day-27/README.md) |
|:---|:---:|---:|

</div>
