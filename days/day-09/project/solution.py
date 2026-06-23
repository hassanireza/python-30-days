"""
Day 09 Project: BMI Calculator
================================
Calculate and classify BMI from weight and height.
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI. Raises ValueError for invalid inputs."""
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> tuple[str, str]:
    """Return the BMI category and advice."""
    if bmi < 18.5:
        return "Underweight", "Consider consulting a nutritionist."
    elif bmi < 25:
        return "Normal weight", "Great! Maintain your healthy lifestyle."
    elif bmi < 30:
        return "Overweight", "Regular exercise and a balanced diet can help."
    else:
        return "Obese", "Please consult a healthcare professional."


def main() -> None:
    print("=" * 45)
    print("           BMI CALCULATOR")
    print("=" * 45)

    try:
        weight = float(input("\nEnter your weight (kg): "))
        height_cm = float(input("Enter your height (cm): "))
        height_m = height_cm / 100

        bmi = calculate_bmi(weight, height_m)
        category, advice = classify_bmi(bmi)

        print(f"\n  BMI       : {bmi:.1f}")
        print(f"  Category  : {category}")
        print(f"  Advice    : {advice}")

        # Visual BMI bar
        bar_pos = min(max(int((bmi - 10) / 30 * 30), 0), 30)
        bar = "-" * bar_pos + "^" + "-" * (30 - bar_pos)
        print(f"\n  [Underweight|Normal|Overweight|Obese]")
        print(f"  [{bar}]")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
