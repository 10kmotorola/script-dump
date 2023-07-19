import sys
import getopt
import ast

try:
    # Options    
    options, arguments = getopt.getopt(sys.argv[1:], "id:h:", ["info", "decimal=", "hex="])
    # Hex converter    
    for currentArgument, currentValue in options:
        # Displays help information        
        if currentArgument in ("-i", "--info"):
            print("hex-converter v1.0.1\nhex-converter [OPTIONS] [VALUE]"                  
                  "\n-i, --info    = how u got here!\n"                  
                  "-d, --decimal = decimal input\n"                  
                  "-h, --hex     = hex input")
        # Converts decimal to hex        
        elif currentArgument in ("-d", "--decimal"):
            dec_value = int(currentValue)
            print(hex(dec_value))
        # Converts hex to decimal        
        elif currentArgument in ("-h", "--hex"):
            print(ast.literal_eval(currentValue))
# Prints errors
except getopt.error as error:
    print(str(error))
    print("Please read --info.")
except ValueError:
    print("Please provide a value in the form of an integer.")
except SyntaxError:
    print("Please provide a value in hexadecimal form.")
