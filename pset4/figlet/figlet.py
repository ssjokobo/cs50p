# import module
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# check cmd-line arg
if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        pass
else:
    sys.exit("Invalid usage")

# input
text = input("Input: ")

# if no specified font
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print("Output: \n")
    print(figlet.renderText(text))

# if specified font
elif len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
    print("Output: \n")
    print(figlet.renderText(text))