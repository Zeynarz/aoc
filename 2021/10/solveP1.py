with open("input","r") as inputFile:
    allLines = inputFile.read().split("\n")
    allLines.pop()


def findSyntaxError(line):
    openings = []
    correspondClosing = {"(":")","[":"]","{":"}","<":">"}
    pointsSystem = {")":3,"]":57,"}":1197,">":25137}
    for char in line:
        if char in ["(","[","{","<"]:
            openings.append(char)

        else:
            # this is a closing
            lastOpening = openings[-1]
            if char == correspondClosing[lastOpening]:
                openings.pop()

            else:
                return pointsSystem[char]

    return 0
                
            
score = 0
for line in allLines:
    score += findSyntaxError(line) 

print(score)
