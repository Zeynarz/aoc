crabsPos = []
totalFuel = 0
mean = 0

with open("input","r") as inputFile:
    crabsPos = inputFile.read().split(",")

crabsPos[-1] = crabsPos[-1][:-1]

for index,crab in enumerate(crabsPos):
    crabsPos[index] = int(crab)

for crab in crabsPos:
    mean += crab

mean /= len(crabsPos)
# -1 to round 490.568 to 490 to try if 490 as the mean will work
mean = round(mean) 

# n(n+1) / 2
for crab in crabsPos:
    n = abs(crab - mean)
    totalFuel += (n * (n+1)) / 2

print(totalFuel)
    
