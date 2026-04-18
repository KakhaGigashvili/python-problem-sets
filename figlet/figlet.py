import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid font")

    text = input("Input: ")
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")