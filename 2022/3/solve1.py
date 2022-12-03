with open("input","r") as inp:
    rucksacks = inp.read().split()

def convertToPriority(char):
    charAscii = ord(char)

    if charAscii < ord("a"):
        # Uppercase
        return charAscii-ord("A")+27

    elif charAscii >= ord("a"):
        # Lowercase
        return charAscii-ord("a")+1

prioritySum = 0
for r in rucksacks:
    halfIndex = len(r) // 2
    firstHalf = r[:halfIndex]
    secondHalf = r[halfIndex:]
    commonItem = set(firstHalf).intersection(secondHalf)
    prioritySum += convertToPriority("".join(commonItem))

print(prioritySum)
