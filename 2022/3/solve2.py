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
for r in rucksacks[::3]:
    firstIndex = rucksacks.index(r)
    common1 = set(r).intersection(rucksacks[firstIndex+1]) 
    common2 = common1.intersection(rucksacks[firstIndex+2])
    prioritySum += convertToPriority("".join(common2))
     
print(prioritySum)
