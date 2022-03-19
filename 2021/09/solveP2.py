# Length of one row = 100
# A total of 100 columns

with open("input","r") as inputFile:
    heightMap = inputFile.read().split("\n")
    heightMap.pop()

def isLowPoint(index1,index2):
    # Initialize them to 10, so the code below will still work if it is a corner/edge point
    left,right,up,down = 10,10,10,10

    currentPoint = int(heightMap[index1][index2])
     
    if index2 != 0:
        left = int(heightMap[index1][index2-1])
    
    if index2 != 99:
        right = int(heightMap[index1][index2+1])

    if index1 != 0:
        up = int(heightMap[index1-1][index2])

    if index1 != 99:
        down = int(heightMap[index1+1][index2])

    if currentPoint < left and currentPoint < right and currentPoint < up and currentPoint < down:
        return True
    else:
        return False
     
# Recursive function
def findBasinSize(index1,index2):
    basinSize = 0

    # Every place which have been checked is replaced with "X"
    heightMap[index1] = heightMap[index1][:index2] + "X" + heightMap[index1][index2+1:]
    basinSize += 1

    left,right,up,down = 9,9,9,9
    if index2 != 0:
        left = heightMap[index1][index2-1]
        if left != "9" and left != "X":
            basinSize += findBasinSize(index1,index2-1)
    
    if index2 != 99:
        right = heightMap[index1][index2+1]
        if right != "9" and right != "X":
            basinSize += findBasinSize(index1,index2+1)

    if index1 != 0:
        up = heightMap[index1-1][index2]
        if up != "9" and up != "X":
            basinSize += findBasinSize(index1-1,index2)

    if index1 != 99:
        down = heightMap[index1+1][index2]
        if down != "9" and down != "X":
            basinSize += findBasinSize(index1+1,index2)
      
    return basinSize

    
allLowPoints = []
allBasinSize = []
finalAns = 1

for index1,row in enumerate(heightMap):
    for index2,point in enumerate(row):
        if isLowPoint(index1,index2):
            allLowPoints.append((index1,index2))


for index1,index2 in allLowPoints:
    allBasinSize.append(findBasinSize(index1,index2))

for i in range(3):
    finalAns *= max(allBasinSize)
    allBasinSize.remove(max(allBasinSize))

print(finalAns)
