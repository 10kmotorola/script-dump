# Scripts
## password-generator
This script generates a string of characters primarily used for obtaining secure passwords. 
It utilizes Python's secrets library instead of its random library, as secrets provides cryptographically strong randomization compared to random's pseudo-random approach.
Written in Python 3.11.4 and requires [pyperclip 1.8.2](https://pypi.org/project/pyperclip/). If error occurs when using pyperclip on Linux, run `sudo apt install xclip`.
