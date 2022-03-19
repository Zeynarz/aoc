puzzle_input = "523764819"
inputList = []
pickedUp = []
for i in puzzle_input:
    inputList.append(int(i))

currentCup = inputList[0]
destinationCup = 0

def pickDestination(cC):
    lowestNumber = min(inputList)
    for i in range(1,11):
        minusNumber = cC - i
        if minusNumber >= lowestNumber:
            if minusNumber in inputList:
                return minusNumber
        else:
            return max(inputList)

highestNumber = max(inputList)
for i in range(1000000):
    numberToAdd = highestNumber + i
    if numberToAdd <= 1000000:
        inputList.append(numberToAdd)
    if numberToAdd % 100000 == 0:
        print(numberToAdd)

for times in range(10000000):
    #print(currentCup)
    if times % 100 == 0:
        print(times)
    wentInfront = 0
    for i in range(1,4):
        try:
            cupNumber = inputList[inputList.index(currentCup) + i]
        except:
            cupNumber = inputList[0 + wentInfront]
            wentInfront += 1

        finally: 
            pickedUp.append(cupNumber)

    for i in pickedUp:
        inputList.remove(i)

    destinationCup =  pickDestination(currentCup)
    #print(destinationCup)
    for index,number in enumerate(pickedUp):
        index += 1
        addIndex  = inputList.index(destinationCup) + index
        inputList.insert(addIndex,number)

    pickedUp = []

    try:
        currentCup = inputList[inputList.index(currentCup) + 1]
    except:
        currentCup = inputList[0]
    

indexOfOne = inputList.index(1)
print(inputList[indexOfOne + 1],inputList[indexOfOne + 2])
    


