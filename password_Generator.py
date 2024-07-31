import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while len(pwd) < min_length or not meets_criteria:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' or 'n'.")

min_length = int(input("Enter the minimum length for the password: "))
has_number = get_yes_no_input("Do you want to include numbers? (y/n): ")
has_special = get_yes_no_input("Do you want to include special characters? (y/n): ")

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)