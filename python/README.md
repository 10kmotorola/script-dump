# Scripts
## hex-converter
Simply converts hex to decimal and decimal to hex. 
Please ensure to prefix your hex values with `0x`.
Made for personal use to streamline the process of developing for RetroAchievements. 
Written in Python 3.10.6.
```
hex-converter.py [OPTIONS] [VALUE]
-i, --info    = how u got here!
-d, --decimal = decimal input
-h, --hex     = hex input
```
## password-generator
Generates a string of characters primarily used for obtaining secure passwords. 
It utilizes Python's secrets library instead of its random library, as secrets provides cryptographically strong randomization compared to random's pseudo-random approach.
Written in Python 3.10.6 and requires [pyperclip 1.8.2](https://pypi.org/project/pyperclip/).
```
password-generator.py [OPTIONS] [PASSWORD LENGTH]
-h, --help    = displays help!
-s, --simple  = generates password using only numbers and letters
-c, --complex = generates password using numbers, letters, and punctuation
```
