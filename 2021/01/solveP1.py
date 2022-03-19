depths = []
prev = 1000 # initialize at 1000 so the first line won't count as increased
increased = 0

with open("input","r") as inputFile:
    depths = inputFile.read().split("\n") 

depths.pop() # get rid of the last element because it is an empty string

for i in depths:
    if int(i) > prev:
        increased += 1

    prev = int(i)

print(increased)
