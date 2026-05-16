import random
import string

print("Welcome to the Password Generator!")

length = int(input("Enter password length: "))

use_letters = input("Do you want letters? (y/n): ").lower() == 'y'
use_digits = input("Do you want digits? (y/n): ").lower() == 'y'
use_symbols = input("Do you want symbols? (y/n): ").lower() == 'y'

characters = ""

if use_letters:
    characters += string.ascii_letters

if use_digits:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

if not characters:
    print(" You must select at least one option.")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\nGenerated Password:", password)

    # Strength checker
    if length < 6:
        print("Password Strength: Weak ")
    elif length < 12:
        print("Password Strength: Moderate ")
    else:
        print("Password Strength: Strong ")
