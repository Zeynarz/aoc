with open("input","r") as inputFile:
    allEntries = inputFile.read().split("\n")
    allEntries.pop()


def figureOutMapping(entry):
    endIndex = entry.index(" | ")
    allUSP = entry[:endIndex].split(" ") 

    displayMapping = {} # "A" : "e" "B" : ...
    uspMapping = {} # "1" : "ab" "2" : ... 

    lenFive = []
    lenSix = []

    for usp in allUSP:
        uspLen = len(usp)

        if uspLen == 2:
            uspMapping["1"] = usp
        elif uspLen == 4:
            uspMapping["4"] = usp
        elif uspLen == 3:
            uspMapping["7"] = usp
        elif uspLen == 7:
            uspMapping["8"] = usp

        elif uspLen == 5:
            lenFive.append(usp)

        elif uspLen == 6:
            lenSix.append(usp)
   
    letter1,letter2 = uspMapping["1"][0],uspMapping["1"][1]

    for usp in lenSix:
        if letter1 not in usp or letter2 not in usp:
            uspMapping["6"] = usp
            lenSix.remove(usp) # So we can differentiate 0 from 9 later without any problems
            if letter1 not in usp:
                displayMapping["C"] = letter1
                displayMapping["F"] = letter2

            elif letter2 not in usp:
                displayMapping["C"] = letter2
                displayMapping["F"] = letter1
    

    for usp in lenFive:
        if displayMapping["C"] in usp and displayMapping["F"] in usp:
            uspMapping["3"] = usp

        elif displayMapping["C"] in usp:
            uspMapping["2"] = usp

        elif displayMapping["F"] in usp:
            uspMapping["5"] = usp
 
    # Find difference between "2" and "3"
    setNum2 = set(uspMapping["2"])
    setNum3 = set(uspMapping["3"])

    displayMapping["E"] = list(setNum2.difference(setNum3))[0]

    for usp in lenSix:
        if displayMapping["E"] in usp:
            uspMapping["0"] = usp

        elif displayMapping["E"] not in usp:
            uspMapping["9"] = usp


    return uspMapping
    
def findOutDigit(entry,uspMapping):
    finalDigit = ""

    startIndex = entry.index(" | ") + 3
    fourDigits = entry[startIndex:].split(" " )

    for key in uspMapping:
        sortedList = sorted(uspMapping[key])
        uspMapping[key] = "".join(sortedList)

    for index,digit in enumerate(fourDigits):
        sortedList = sorted(digit)
        fourDigits[index] = "".join(sortedList)

    for digit in fourDigits:
        for key in uspMapping:
            if uspMapping[key] == digit:
                finalDigit += key
                break
    
    return int(finalDigit)

sumVal = 0
for entry in allEntries:
    sumVal += findOutDigit(entry,figureOutMapping(entry))

print(sumVal)




