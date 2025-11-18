from typing import Any

CURRENT_YEAR: int = 2025


# 1. Define a Function for the Profile & Calculations: generate_profile
def generate_profile(age: int) -> str:
    """
    Determines the user's 'life stage' based on their age (Child, Teenager, or Adult).
    """
    life_stage: str = "Adult"

    if 0 <= age <= 12:
        life_stage = "Child"
    elif 13 <= age <= 19:
        life_stage = "Teenager"

    return life_stage


# Function to display the profile (corresponds to step 4)
def display_profile(user_profile: dict[str, Any]) -> None:
    """
    Formats and prints the user profile summary.
    """
    print("\n" + "-" * 3)

    # Print name, current age, life stage
    print(f"Name: {user_profile['name']}")
    print(f"Current Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")

    hobbies_list: list[str] = user_profile["hobbies"]

    # Check and display hobbies list
    if not hobbies_list:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(hobbies_list)}):")
        # Loop to print each hobby with a bullet point
        for hobby in hobbies_list:
            print(f"- {hobby}")

    print("-" * 3)


def main() -> None:
    """
    Main execution function: handles input, calculation, processing (steps 2 & 3), and output.
    """

    # 2. Get User Input

    # Collect name and birth year
    user_name: str = input("Enter your full name: ").strip().title()
    birth_year_str: str = input("Enter your birth year: ").strip()

    # Convert year
    birth_year: int = int(birth_year_str)

    # Calculate current age
    current_age: int = CURRENT_YEAR - birth_year
    hobbies: list[str] = []

    # Loop to collect hobbies until 'stop' is entered
    while True:
        hobby_input: str = (
            input("Enter a favorite hobby or type 'stop' to finish: ").strip().title()
        )

        if hobby_input.lower() == "stop":
            break

        if hobby_input:
            hobbies.append(hobby_input)

    # 3. Process and Generate the Profile

    # Call function to get life stage
    life_stage: str = generate_profile(current_age)

    # Create the final user_profile dictionary
    user_profile: dict[str, Any] = {
        "name": user_name,
        "age": current_age,
        "life_stage": life_stage,
        "hobbies": hobbies,
    }

    # 4. Display the Output
    display_profile(user_profile)


if __name__ == "__main__":
    main()
