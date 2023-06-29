import string
import secrets
import pyperclip

# Variables
simp = string.ascii_letters + string.digits
comp = simp + string.punctuation

# Credits and stuff
print("password-generator v1.1.4")

# Questions
while True:
    try:
        size = int(input("How many characters would you like your password to be? "))
    except ValueError:
        print("Please provide an answer in the form of an integer. (¬_¬ ) ")
        continue
    else:
        break
sc = input("Would you like your password to be (s)imple or (c)omplex? ")

# Password generator
while True:
    if sc == "s":
        password = ''.join(secrets.choice(simp) for i in range(size))
        print(password)
        pyperclip.copy(password)
    elif sc == "c":
        password = ''.join(secrets.choice(comp) for i in range(size))
        print(password)
        pyperclip.copy(password)
    else:
        sc = input('The answer you provided means nothing to my python script headass. '
                   'Please provide an answer containing "s" or "c". ')
        continue
    # Regenerate password
    again = input("Copied to clipboard! Generate again? (y/n) ")
    if again == "y":
        pass
    else:
        break
