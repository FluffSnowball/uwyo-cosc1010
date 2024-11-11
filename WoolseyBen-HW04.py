# Ben Woolsey
# Lab Section: 11
# Submition Date: 11/11/2024
# Worked with: Cole Jordan
from pathlib import Path

path = Path('prompt.txt')
pathOut = Path('out.txt')

contents = path.read_text()
lines = contents.splitlines()
outputCurrentLine = ""

def wordProcess(input:str):
    """Gets the numbers of white space and asterisks"""
    return int(input[2:])

for i in lines:
    currentLine = i.split('\t')
    del currentLine[-1]
    for x in currentLine:
        outputCount = wordProcess(x)
        if x.startswith('w'):
            outputCurrentLine += (" " * outputCount)
        else: 
            outputCurrentLine += ("*" * outputCount)
    outputCurrentLine += '\n'

    pathOut.write_text(outputCurrentLine)