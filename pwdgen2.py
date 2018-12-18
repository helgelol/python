#!/usr/bin/python

import string
from random import choice

# Defines chars is ascii letters, special chars and digits
characters = string.ascii_letters + string.punctuation + string.digits

# Takes input for password length
def take_input():
    inputData = input("Passwordlength: ")

    # Check if input was int
    try:
        inputData = int(inputData)

    # If not int then prompts user
    except ValueError:
        print("Not a valid lenth, use numbers")

        # And tries again
        inputData = take_input()
    return inputData

# Puts length from variable
length = take_input()

# Joins it together and generates based on length
password = "".join(choice(characters) for x in range(length))

# And prints it
print(password)