with open("input","r") as inp:
    pairs = inp.read().split("\n")
    pairs = pairs[:-1]

noOverlap = 0
for i in pairs:
    elfs = i.split(",")
    elf1 = elfs[0].split("-")
    elf2 = elfs[1].split("-")

    start1,end1 = int(elf1[0]),int(elf1[1]) 
    start2,end2 = int(elf2[0]),int(elf2[1]) 
    
    if start1 < start2:
        if end1 < start2:
            noOverlap += 1

    elif start1 > start2:
        if end2 < start1:
            noOverlap += 1

print(1000 - noOverlap)
     
