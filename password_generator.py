import random
import string


def get_yes_no(prompt):
    """Ask the user a yes/no question and return True for yes, False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def get_password_length():
    """Ask the user for a valid password length."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    """Generate a password based on selected criteria."""
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return None

    password = ""
    for _ in range(length):
        password += random.choice(character_pool)

    return password


def main():
    print("Welcome to the Python Password Generator!")

    length = get_password_length()
    use_upper = get_yes_no("Include uppercase letters? (yes/no): ")
    use_lower = get_yes_no("Include lowercase letters? (yes/no): ")
    use_numbers = get_yes_no("Include numbers? (yes/no): ")
    use_special = get_yes_no("Include special characters? (yes/no): ")

    password = generate_password(length, use_upper, use_lower, use_numbers, use_special)

    if password is None:
        print("You must select at least one character type.")
    else:
        print("\nGenerated Password:")
        print(password)


if __name__ == "__main__":
    main()