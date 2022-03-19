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
     
finalSum = 0

for index1,row in enumerate(heightMap):
    for index2,point in enumerate(row):
        if isLowPoint(index1,index2):
            finalSum += int(point) + 1

print(finalSum)
