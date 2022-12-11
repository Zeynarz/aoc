from math import sqrt

with open("input","r") as inp:
    motions = inp.read().split("\n")[:-1]

directionRef = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}

class Knot:
    def __init__(self,nextKnot):
        self.x = 0
        self.y = 0
        self.nextKnot = nextKnot

    def followKnot(self):
        # works for same row,same column,and also diagonal knots
        if not isAdjacent(self,self.nextKnot):
            if self.y > self.nextKnot.y:
                self.y -= 1
            elif self.y < self.nextKnot.y:
                self.y += 1

            if self.x > self.nextKnot.x:
                self.x -= 1
            elif self.x < self.nextKnot.x:
                self.x += 1


def isAdjacent(frontKnot,backKnot):
    x1,x2 = frontKnot.x,backKnot.x
    y1,y2 = frontKnot.y,backKnot.y

    d = sqrt((y2-y1)**2 + (x2-x1)**2)

    # if head & tail is adjacent, then distance is sqrt(0) or sqrt(1) or sqrt(2)
    # distance isn't possible to be sqrt(3), and sqrt(4) = 2

    if d < 2:
        return True
    
    return False


visited = []
knots = [Knot(None),0,0,0,0,0,0,0,0,0]
for i in range(1,10):
    knots[i] = Knot(knots[i-1])


for steps in motions:
    # move n steps in direction
    direction,n = steps[0],int(steps[2:])
    
    for i in range(n):
        x,y = directionRef[direction]
        knots[0].x += x 
        knots[0].y += y

        for knot in knots[1:]:
            knot.followKnot()
    
        tailCoordinate = knots[-1].x,knots[-1].y
        if tailCoordinate not in visited:
            visited.append(tailCoordinate)


print(len(visited))
