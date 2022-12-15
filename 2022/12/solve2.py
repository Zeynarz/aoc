# Good sources:
# https://www.youtube.com/watch?v=ySN5Wnu88nE&ab_channel=Computerphile
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

with open("input","r") as inp:
    rows = inp.read().split("\n")[:-1]

class Square:
    def __init__(self,pos,elevation):
        self.pos = pos
        self.elevation = elevation
        self.parent = None
        self.gCost = 99999999
        self.hCost = 99999999
        self.fCost = 99999999


def backtrack(square,startPos):
    distance = 0
    current = square
    while current.pos != startPos:
        distance += 1
        current = current.parent

    return distance


startSquares = []
# Make everything a square
squares = []
for i,row in enumerate(rows):
    tempRow = []

    for j,char in enumerate(row):
        if char == "S":
            rows[i] = rows[i][:j] + 'a' + rows[i][j+1:]
        elif char == "E":
            endPos = i,j
            rows[i] = rows[i][:j] + 'z' + rows[i][j+1:]

        # if I write ord(char) instead of ord(rows[i][j]), then end square will be
        # created with elevation "E", and start square will be created with elevation "S"
        square = Square((i,j),ord(rows[i][j]))
        tempRow.append(square)

        if char == "a" or char == "S":
            startSquares.append(square)
    
    squares.append(tempRow)


endRow,endColumn = endPos
fewestSteps = 999999

for start in startSquares:
    startRow,startColumn = start.pos
    openList = [squares[startRow][startColumn]]
    closedList = [] # expanded squares

    while openList:
        # Find best square
        currentSquare = openList[0]
        for square in openList:
            if square.fCost < currentSquare.fCost:
                currentSquare = square
    
        if currentSquare.pos == endPos:
            steps = backtrack(currentSquare,start.pos)
            print(steps)
            if steps < fewestSteps:
                fewestSteps = steps
    
        openList.remove(currentSquare)
        closedList.append(currentSquare)
    
        # Calculate fCost of surrounding squares and add to open list
        currentRow,currentColumn = currentSquare.pos
        surroundingPos = [(currentRow,currentColumn-1),
                (currentRow,currentColumn+1),
                (currentRow-1,currentColumn),
                (currentRow+1,currentColumn)] 
    
        for row,column in surroundingPos:
            if row < 0 or row >= len(squares) or column < 0 or column >= len(squares[0]):
                # Out of bounds
                continue
    
            square = squares[row][column]
    
            # Go to next square if elevation too high
            if square.elevation > (currentSquare.elevation + 1) or square in closedList:
                continue
    
            g = backtrack(currentSquare,start.pos) + 1     
            h = (endColumn - startColumn) ** 2 + (endRow - endColumn) ** 2 
            f = g + h
            
            if square in openList:
                if g > square.gCost:
                    continue
                openList.remove(square)
    
            square.parent = currentSquare
            square.gCost = g
            square.hCost = h
            square.fCost = f
       
            openList.append(square)
            
print("FEWEST: " + str(fewestSteps))
