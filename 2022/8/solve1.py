with open("input","r") as inp:
    trees = inp.read().split() 

visible = 0

for i,row in enumerate(trees):
    if i == 0 or i == len(trees)-1:
        visible += len(trees[i])
        continue

    for j,tree in enumerate(row):
        treeHeight = int(tree)

        if j == 0 or j == len(trees)-1:
            visible += 1
            continue

        # Check left
        isVisible = True
        for k in range(j):
            if int(row[k]) >= treeHeight:
                isVisible = False
                break

        # Check right
        if not isVisible:
            isVisible = True
            for k in range(j+1,len(row)):
                if int(row[k]) >= treeHeight:
                    isVisible = False
                    break

        # Check up
        if not isVisible:
            isVisible = True
            for k in range(i):
                if int(trees[k][j]) >= treeHeight:
                    isVisible = False
                    break

        # Check down
        if not isVisible:
            isVisible = True
            for k in range(i+1,len(trees)):
                if int(trees[k][j]) >= treeHeight:
                    isVisible = False
                    break
        
        if isVisible:
            visible += 1

        
print(visible)
