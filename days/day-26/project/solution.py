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
