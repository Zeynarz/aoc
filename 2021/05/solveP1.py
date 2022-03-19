# Store all the points in every line segment, then just count the duplicates
# Is there a better way?

from iteration_utilities import duplicates,unique_everseen

lineOfVents = []
allPoints = []

amountOverlap = 0

with open("input","r") as inputFile:
    lineOfVents = inputFile.read().split("\n")

lineOfVents.pop()


# Add all points
for line in lineOfVents:
    coords = line.split(" -> ")
    firstPoint = coords[0].split(",")
    secondPoint = coords[1].split(",")
    x1,y1 = int(firstPoint[0]),int(firstPoint[1])
    x2,y2 = int(secondPoint[0]),int(secondPoint[1])
    
    if x1 == x2:
        # Vertical line
        rangeArg1,rangeArg2 = min(y1,y2), max(y1,y2)
        for i in range(rangeArg1,rangeArg2+1):
            allPoints.append((x1,i))

    elif y1 == y2:
        # Horizontal line
        rangeArg1,rangeArg2 = min(x1,x2), max(x1,x2)
        for i in range(rangeArg1,rangeArg2+1):
            allPoints.append((i,y1))


# Find duplicates in the list to find intersections of lines
# https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
# I used the method mentioned by MSeifert to find duplicates in lists

print(len(list(unique_everseen(duplicates(allPoints)))))


