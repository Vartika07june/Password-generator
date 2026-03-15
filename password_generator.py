import random
import string

# Function to generate password
def generate_password(length):

    # Letters, digits and symbols
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    password = ""

    # Loop to generate password
    for i in range(length):
        char = random.choice(all_characters)
        password = password + char

    return password


# Main program
print("------ PASSWORD GENERATOR ------")

# User input
length = int(input("Enter the length of password: "))

# Calling function
password = generate_password(length)

print("Your Generated Password is:", password)

print("Thank you for using Password Generator!")