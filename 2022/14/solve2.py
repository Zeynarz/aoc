with open("input","r") as inp:
    rocks = inp.read().split("\n")[:-1]

# draw path of rocks, x is just gonna be from 300-699, and y is gonna be 0-199
cave = []
temp = []
for i in range(400):
    temp.append([])

for i in range(200):
    cave.append(temp.copy())


highestY = 0
for path in rocks:
    points = path.split(" -> ")
    for i,point in enumerate(points[:-1]):
        point = point.split(",")
        point2 = points[i+1].split(",")
        x,y = int(point[0]),int(point[1])
        x2,y2 = int(point2[0]),int(point2[1])

        if x != x2:
            for j in range(min(x,x2),max(x,x2)+1):
                # can only draw left to right lines
                cave[y][j-300] = "#"

            if y > highestY:
                highestY = y

        elif y != y2:
            for j in range(min(y,y2),max(y,y2)+1):
                # can only draw top to down lines
                cave[j][x-300] = "#"


# draw floor
floorLevel = highestY + 2
for i in range(len(cave[0])):
    cave[floorLevel][i] = "#"



def sandNextStep(sandPos):
    global cave
    x,y = sandPos
    
    # look downwards
    if cave[y+1][x] == []:
        for i in range(y+1,200):
            if cave[i][x] != []:
                return x,i-1
        
    # look diagonal left
    if not cave[y+1][x-1]:
        return x-1,y+1

    # look diagonal right
    if not cave[y+1][x+1]:
        return x+1,y+1

    return x,y


n = 0
while True:
    currentPos = None
    newPos = 200,0
    while newPos != currentPos:
        currentPos = newPos
        newPos = sandNextStep(currentPos)

    sandX,sandY = newPos
    cave[sandY][sandX] = 'o'
    n += 1

    # source is blocked
    if cave[0][200] == "o":
        print(n)
        break

