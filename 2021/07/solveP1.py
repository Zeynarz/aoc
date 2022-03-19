crabsPos = []
totalFuel = 0

with open("input","r") as inputFile:
    crabsPos = inputFile.read().split(",")

crabsPos[-1] = crabsPos[-1][:-1]

for index,crab in enumerate(crabsPos):
    crabsPos[index] = int(crab)

crabsPos.sort()
median = crabsPos[round(len(crabsPos) / 2)]

for crab in crabsPos:
    totalFuel += abs(crab - median)

print(totalFuel)
