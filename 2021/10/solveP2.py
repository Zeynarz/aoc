import math
with open("input","r") as inputFile:
    allLines = inputFile.read().split("\n")
    allLines.pop()


def findSyntaxError(line):
    ownClosing = ""
    openings = []
    correspondClosing = {"(":")","[":"]","{":"}","<":">"}
    pointsSystem = {")":1,"]":2,"}":3,">":4}

    for char in line:
        if char in ["(","[","{","<"]:
            openings.append(char)

        else:
            # this is a closing
            lastOpening = openings[-1]
            if char == correspondClosing[lastOpening]:
                openings.pop()

            else:
                # corrupted line
                return False
    
    # The file only has corrupted and incomplete lines, no complete lines 
    for i in range(len(openings)-1,-1,-1):
        ownClosing += correspondClosing[openings[i]]

    # Calculate score
    score = 0

    for char in ownClosing:
        score *= 5
        score += pointsSystem[char]

    return score

            
allScores = []
for line in allLines:
    score = findSyntaxError(line)

    if score != False:
        # incomplete line
        allScores.append(score)

allScores.sort()
midIndex = math.floor(len(allScores)/2)
print(allScores[midIndex])
