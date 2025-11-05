def calculate_puppy_age(human_years):
    """Convert dog's age in human years to puppy years (1 human year = 7 puppy years)."""
    if not isinstance(human_years, (int, float)):
        return "Invalid input. Please enter a number."
    elif human_years < 0:
        return "Age cannot be negative."
    puppy_years = human_years * 7
    return puppy_years




def main():
    try:
        human_years = int(input("Enter your puppy's age in human years: "))
        puppy_age = calculate_puppy_age(human_years)
        print(f"Your puppy's age in puppy years is: {puppy_age}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
main()