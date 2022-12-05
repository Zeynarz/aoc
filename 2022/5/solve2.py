with open("input","r") as inp:
    cratesNMoves = inp.read().split("\n\n")
    crates,moves = cratesNMoves[0].split("\n"), cratesNMoves[1].split("\n")[:-1]

stacks = [[],[],[],[],[],[],[],[],[]] 
# if use "stacks = [[]] * 9", then all 9 arrs point to the same address?
# like stacks[0] and stacks[7] both point to the same place right? 

for row in crates[-2::-1]:
    for index,crate in enumerate(row[1::4]):
        if crate != " ":
            stacks[index].append(crate)

for move in moves:
    words = move.split(" ")
    n,src,dest = int(words[1]),int(words[3]),int(words[5])

    toMove = stacks[src-1][0-n:]
    stacks[src-1] = stacks[src-1][:0-n]
    for crate in toMove:
        stacks[dest-1].append(crate)
        
for stack in stacks:
    print(stack[-1],end="")

print()
