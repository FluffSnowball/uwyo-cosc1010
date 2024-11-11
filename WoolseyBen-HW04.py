# Ben Woolsey
# Lab Section: 11
# Submition Date: 11/11/2024
# Worked with: Cole Jordan
from pathlib import Path

path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()
outputCurrentLine = ""

def wordProcess(input:str):
    """"""

for i in lines:
    currentLine = i.split('\t')
    del currentLine[-1]
    for x in currentLine:
        if x.startswith('w'):

    print(currentLine)