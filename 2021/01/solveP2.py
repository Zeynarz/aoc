allDepths = []
threeMDepths = []

prev = 10000 # initialize at 10000 so the first line won't count as increased
increased = 0
startIndex = 0

with open("input","r") as inputFile:
    allDepths = inputFile.read().split("\n") 

allDepths.pop() # get rid of the last element because it is an empty string

while True:
    total = 0
    
    # Stop when there are not enough measurements
    if (startIndex + 2) >= len(allDepths):
        break

    for i in range(3):
        total += int(allDepths[startIndex+i])
    
    threeMDepths.append(total)
    startIndex += 1
    

for i in threeMDepths:
    if int(i) > prev:
        increased += 1

    prev = int(i)

print(increased)
