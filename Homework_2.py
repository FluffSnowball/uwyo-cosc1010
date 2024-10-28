# Ben Woolsey
# UWYO COSC 1010
# 10/28/2024
# HW 02
# Lab Section: 11
# Worked with: Cole Jordan

inputString = str(input("Input your message: "))

morseCode = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."
}

outputString = ""
for entry in inputString:
    if not entry.isalpha():
        outputString += "  "
    else:
        outputString += (morseCode[entry.upper()] + " ")

print(outputString)