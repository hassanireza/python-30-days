"""
Day 07 Project: Unique Word Counter
=====================================
Analyze text for unique words using sets.
"""
import string


def clean_words(text: str) -> set[str]:
    """Extract a set of unique lowercase words from text."""
    # Remove punctuation and split into words
    translator = str.maketrans("", "", string.punctuation)
    cleaned = text.lower().translate(translator)
    return set(cleaned.split())


def word_frequency(text: str) -> dict[str, int]:
    """Count how often each word appears."""
    translator = str.maketrans("", "", string.punctuation)
    words = text.lower().translate(translator).split()
    freq: dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def main() -> None:
    print("=" * 50)
    print("         UNIQUE WORD COUNTER")
    print("=" * 50)

    print("\nPaste Text 1 (press Enter twice when done):")
    lines1 = []
    while True:
        line = input()
        if line == "":
            break
        lines1.append(line)
    text1 = " ".join(lines1)

    print("\nPaste Text 2 (press Enter twice when done):")
    lines2 = []
    while True:
        line = input()
        if line == "":
            break
        lines2.append(line)
    text2 = " ".join(lines2)

    words1 = clean_words(text1)
    words2 = clean_words(text2)
    freq1 = word_frequency(text1)

    print(f"\n--- Text 1 Analysis ---")
    print(f"Total unique words : {len(words1)}")
    top5 = sorted(freq1, key=freq1.get, reverse=True)[:5]
    print(f"Top 5 words        : {top5}")

    print(f"\n--- Comparison ---")
    print(f"Words in both      : {words1 & words2}")
    print(f"Only in Text 1     : {words1 - words2}")
    print(f"Only in Text 2     : {words2 - words1}")


if __name__ == "__main__":
    main()
