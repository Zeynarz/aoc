from math import sqrt

with open("input","r") as inp:
    motions = inp.read().split("\n")[:-1]

# x,y
headPos = [0,0]
tailPos = [0,0]
directionRef = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
visited = [(0,0)]

def isAdjacent(headPos,tailPos):
    x1,x2 = headPos[0],tailPos[0]
    y1,y2 = headPos[1],tailPos[1]

    d = sqrt((y2-y1)**2 + (x2-x1)**2)

    # if head & tail is adjacent, then distance is sqrt(0) or sqrt(1) or sqrt(2)
    # distance isn't possible to be sqrt(3), and sqrt(4) = 2

    if d < 2:
        return True
    
    return False

for steps in motions:
    # move n steps in direction
    direction,n = steps[0],int(steps[2:])
    
    for i in range(n):
        x,y = directionRef[direction]
        headPos[0] += x 
        headPos[1] += y


        if not isAdjacent(headPos,tailPos):
            if tailPos[1] > headPos[1]:
                tailPos[1] -= 1
            elif tailPos[1] < headPos[1]:
                tailPos[1] += 1
            
            if tailPos[0] > headPos[0]:
                tailPos[0] -= 1
            elif tailPos[0] < headPos[0]:
                tailPos[0] += 1


            # only check when tail moves
            tailCoordinate = tailPos[0],tailPos[1]

            if tailCoordinate not in visited:
                visited.append(tailCoordinate) 


print(len(visited))
