with open("input","r") as inp:
    trees = inp.read().split() 


highestScore = 0
for i,row in enumerate(trees):
    for j,tree in enumerate(row):
        treeHeight = int(tree)
        # [left,right,up,down]
        viewDistance = [0,0,0,0]

        # Find viewDistance to left side of tree
        for k in range(j-1,-1,-1):
            viewDistance[0] += 1
            if int(row[k]) >= treeHeight:
                break

        # Right side
        for k in range(j+1,len(row)):
            viewDistance[1] += 1
            if int(row[k]) >= treeHeight:
                break

        # Up
        for k in range(i-1,-1,-1):
            viewDistance[2] += 1
            if int(trees[k][j]) >= treeHeight:
                break

        # Down
        for k in range(i+1,len(trees)):
            viewDistance[3] += 1
            if int(trees[k][j]) >= treeHeight:
                break

        scenicScore = 1
        for d in viewDistance:
            scenicScore *= d

        if scenicScore > highestScore:
            highestScore = scenicScore

print(highestScore)
