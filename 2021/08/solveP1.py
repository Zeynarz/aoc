n = 0

with open("input","r") as inputFile:
    for i in range(200):
        line = inputFile.readline()
        startIndex = line.index("|") + 2
        outputVals = line[startIndex:-1].split(" ")
        for val in outputVals:
            if len(val) in [2,3,4,7]:
                n += 1



print(n)
