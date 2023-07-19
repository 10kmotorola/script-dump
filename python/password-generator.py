import sys
import getopt
import string
import secrets
import pyperclip

# Variables
simple_string = string.ascii_letters + string.digits
complex_string = simple_string + string.punctuation

try:
    # Options    
    options, arguments = getopt.getopt(sys.argv[1:], "hs:c:", ["help", "simple=", "complex="])
    # Password generator    
    for currentArgument, currentValue in options:
        # Displays help information        
        if currentArgument in ("-h", "--help"):
            print("password-generator v2.0.0\npassword-generator.py [OPTIONS] [PASSWORD LENGTH]"
                  "\n-h, --help    = displays help!\n-s, --simple  = generates password using"
                  "only numbers and letters\n-c, --complex = generates password using"
                  "numbers, letters, and punctuation")
        # Generates simple password        
        elif currentArgument in ("-s", "--simple"):
            currentArgument = simple_string
            password = ''.join(secrets.choice(currentArgument) for i in range(int(currentValue)))
            print(password)
            print("Copied to clipboard!")
            pyperclip.copy(password)
        # Generates complex password        
        elif currentArgument in ("-c", "--complex"):
            currentArgument = complex_string
            password = ''.join(secrets.choice(currentArgument) for i in range(int(currentValue)))
            print(password)
            print("Copied to clipboard!")
            pyperclip.copy(password)
# Prints errors
except getopt.error as error:
    print(str(error))
    print("Please read --help.")
except ValueError:
    print("Please provide an answer in the form of an integer. (¬_¬ )")
