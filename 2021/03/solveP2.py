binaryNums = []

with open("input","r") as inputFile:
    binaryNums = inputFile.read().split("\n")

binaryNums.pop()
oxyNums = binaryNums.copy()
co2Nums = binaryNums.copy()


def determineMostCommon(index,arr):
    oneAmount = 0
    for binary in arr:
        if binary[index] == "1":
            oneAmount += 1

    if oneAmount >= (len(arr) / 2):
        # 1 is most common or equally common as "0"
        return "1"

    else:
        # 0 is most common
        return "0"

index,mostCommon = 0,""

while len(oxyNums) != 1 and index < 12:
    mostCommon = determineMostCommon(index,oxyNums)
    oxyNumLen = len(oxyNums)

    # Iterate the array from behind to make sure there are no skipped elements
    for i in range(oxyNumLen-1,-1,-1):
        if oxyNums[i][index] != mostCommon:
            oxyNums.pop(i) 

    index += 1


index,mostCommon = 0,""

while len(co2Nums) != 1 and index < 12:
    mostCommon = determineMostCommon(index,co2Nums)
    co2NumLen = len(co2Nums)

    # Iterate the array from behind to make sure there are no skipped elements
    for i in range(co2NumLen-1,-1,-1):
        if co2Nums[i][index] == mostCommon:
            co2Nums.pop(i) 

    index += 1

print(int(oxyNums[0],2) * int(co2Nums[0],2))
