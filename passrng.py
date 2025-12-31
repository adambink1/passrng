#password generator
#generates a random password including lowercase letters, uppercase letters, symbols, and numbers
#will give password of desired length, from 6-128 characters based on user input

import secrets
import random

def password_generator(password_length):
    password_list = []
    password_list.append(secrets.choice(UPPERCASE))
    password_list.append(secrets.choice(LOWERCASE))
    password_list.append(secrets.choice(NUMBERS))
    password_list.append(secrets.choice(SYMBOLS))
    for _ in range(password_length - 4):
        password_list.append(secrets.choice(CHARACTER_LIST))
    random.shuffle(password_list)
    password = "".join(password_list)
    return password

def get_password_length():
    while True:
            print()
            password_length_str = input("How many characters would you like your password to be? (6-128): ")
            try:
                password_length = int(password_length_str)
            except ValueError:
                print()
                print("Please enter a number.")
                continue
            if password_length < 6 or password_length > 128:
                print()
                print("Number must be between 6 and 128.")
                continue
            break
    return password_length

LOWERCASE = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
UPPERCASE = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
NUMBERS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
SYMBOLS = ("!", "@", "#", "$", "%", "&")
CHARACTER_LIST = LOWERCASE + UPPERCASE + NUMBERS + SYMBOLS


print("Welcome to PassRNG!")
while True:
    password_length = get_password_length()

    print()
    print(f"Your randomly generated password is: {password_generator(password_length)}")

    while True:
        print()
        restart = input("Press enter to generate another password, or type 'q' to quit:")
        if restart.strip() == "":
            break
        elif restart.lower() == "q":
            break
        else:
            print()
            print("Invalid input. Please try again.")
            continue
    if restart.lower() == "q":
        break

print()
print("Thank you for using PassRNG!")
print()







