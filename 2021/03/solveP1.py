binaryNums = []
amountOfOne = [0,0,0,0,0,0,0,0,0,0,0,0]

gammaNum = 0
epsilonNum = 0
finalBinStr = ""

with open("input","r") as inputFile:
    binaryNums = inputFile.read().split("\n")

binaryNums.pop()

for i in binaryNums:
    for index,j in enumerate(i):
        if j == "1":
            amountOfOne[index] += 1

 
for i in amountOfOne:
    if i > (len(binaryNums) / 2):
        finalBinStr += "1"
    
    else:
        finalBinStr += "0"

# can just negate gamma rate to find epsilon rate
gammaNum = int(finalBinStr,2)
epsilonNum = gammaNum ^ int("111111111111",2) # 010 ^ 111 = 101 = NOT(010)

print(gammaNum * epsilonNum)
