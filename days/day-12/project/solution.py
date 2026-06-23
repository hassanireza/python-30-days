"""
Day 12 Project: Password Generator
====================================
Generate secure random passwords using functions.
"""
import random
import string


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a secure random password.

    Args:
        length: Number of characters in the password (default 16).
        use_upper: Include uppercase letters.
        use_lower: Include lowercase letters.
        use_digits: Include digits.
        use_symbols: Include symbols.

    Returns:
        A random password string.

    Raises:
        ValueError: If no character sets are selected or length is too short.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    charset = ""
    guaranteed: list[str] = []

    if use_upper:
        charset += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        charset += string.ascii_lowercase
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        charset += string.digits
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        charset += string.punctuation
        guaranteed.append(random.choice(string.punctuation))

    if not charset:
        raise ValueError("Select at least one character type.")

    remaining_length = length - len(guaranteed)
    rest = [random.choice(charset) for _ in range(remaining_length)]
    all_chars = guaranteed + rest
    random.shuffle(all_chars)
    return "".join(all_chars)


def rate_password(password: str) -> str:
    """Rate the strength of a password."""
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    ratings = {5: "Very Strong", 4: "Strong", 3: "Moderate", 2: "Weak", 1: "Very Weak"}
    return ratings.get(score, "Very Weak")


def main() -> None:
    print("=" * 45)
    print("         PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("\nPassword length (default 16): ") or "16")
        use_upper = input("Include uppercase? (Y/n): ").strip().lower() != "n"
        use_lower = input("Include lowercase? (Y/n): ").strip().lower() != "n"
        use_digits = input("Include digits? (Y/n): ").strip().lower() != "n"
        use_symbols = input("Include symbols? (Y/n): ").strip().lower() != "n"
        count = int(input("How many passwords? (default 5): ") or "5")

        print(f"\n{'Password':<{length + 4}} Strength")
        print("-" * (length + 20))
        for _ in range(count):
            pw = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            strength = rate_password(pw)
            print(f"  {pw:<{length + 2}} {strength}")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
