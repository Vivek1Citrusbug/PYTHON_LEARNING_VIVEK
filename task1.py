import re

def get_user_info() -> None:
    name_pattern = r"^[A-Za-z\s]+$"
    age_pattern = r"^[1-9]\d*$"

    while True:
        user_name: str = input("Enter Your Name: ").strip()
        if re.match(name_pattern, user_name):
            break
        else:
            print("Name should be a valid input (only letters and spaces).")

    while True:
        age_input: str = input("Enter Your Age: ").strip()
        if re.match(age_pattern, age_input):
            age = int(age_input)
            break
        else:
            print("Age should be a valid positive integer.")

    print(f"You will be 100 years old after {100 - age} years.")


if __name__ == "__main__":
    get_user_info()
