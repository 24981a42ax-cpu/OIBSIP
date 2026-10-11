import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:

    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices (example: 1234): ")

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        if len(characters) == 0:
            print("Error: Please select at least one character type.")
            continue

        if len(set(choices)) < 2:
            print("Error: Please select at least two character types.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")