class Tile(object):
    def __init__(self,tile,tileNumber):
        self.tiles = tile.split("\n")
        self.tiles.remove(self.tiles[0])
        self.tileNumber = tileNumber
        self.border = []
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        leftList = []
        rightList = []
        for i in self.tiles:
            leftList.append(i[0])
            rightList.append(i[-1])
        
        self.border.append(self.tiles[0])
        self.border.append("".join(rightList))
        self.border.append(self.tiles[-1])
        self.border.append("".join(leftList))

    def pair(self,orientation,tileNumber):
        if orientation == 0:
            self.up = tileNumber
        elif orientation == 1:
            self.right = tileNumber
        elif orientation == 2:
            self.down = tileNumber
        elif orientation == 3:
            self.left = tileNumber
        self.pairs = [self.up,self.right,self.down,self.left]
    
    def flip(self,xy):
        if xy == "x":
            originalRight = self.border[1]
            originalLeft = self.border[3]
            Left = self.left
            Right = self.right 
            self.left = Right
            self.right = Left
            self.border[0] = self.border[0][::-1]
            self.border[2] = self.border[2][::-1]
            self.border[1] = originalLeft
            self.border[3] = originalRight
        elif xy == "y":
            originalUp = self.border[0]
            originalDown = self.border[2]
            Up = self.up
            Down = self.down
            self.up = Down
            self.down = Up
            self.border[1] = self.border[1][::-1]
            self.border[3] = self.border[3][::-1]
            self.border[0] = originalDown
            self.border[2] = originalUp

    def rotate(self,way):
        copyBorder = self.border.copy()
        Up , Right , Down, Left = self.up,self.right,self.down,self.left
        if way == 1:#AntiClockwise
            self.up,self.right,self.down,self.left  = Left,Up,Right,Down
            for i in range(3):
                if i != 3:
                    self.border[i] = copyBorder[i+1]
                else:
                    self.border[i] = copyBorder[0]
        elif way == 2:#Clockwise
            self.up,self.right,self.down,self.left  = Right,Down,Left,Up
            for i in range(3):
                if i != 0:
                    self.border[i] = copyBorder[i-1]
                else:
                    self.border[i] = copyBorder[3]
        
allTiles = []
allTilesDict = {}
borderTiles = {}
with open("tiles2","r") as tilesFile:
    allTilesStrings = tilesFile.read()
    allTilesList = allTilesStrings.split("\n\n")

allTilesList[-1] = allTilesList[-1][:-1]
for tile in allTilesList:
    tileNumber = tile[5:9]
    tileObject = Tile(tile,tileNumber)
    allTiles.append(tileObject)
    allTilesDict[tileNumber] = tileObject

#Pairing
for x in allTiles:
    for y in allTiles:
        xNumber = x.tileNumber
        yNumber = y.tileNumber
        if xNumber == yNumber:
            continue
        for orientation,bdx in enumerate(x.border):
            for bdy in y.border:
                if bdx == bdy or bdx == bdy[::-1]:
                    #Check if tile is flipped
                    if bdx == bdy[::-1]:
                        if (bdy == y.border[1] or bdy == y.border[3]):
                            y.flip("y")
                        elif (bdy == y.border[0] or bdy == y.border[2]):
                            y.flip("x")
                        
                    if x.border[1] == y.border[1] :
                        y.flip("x")
                    elif x.border[3] == y.border[3]:
                        orientation = 1
                        print(orientation)
                        x.flip("x")
                    elif x.border[0] == y.border[0] or x.border[2] == y.border[2]:
                        y.flip("y")

                    if x.border[0] == y.border[1] or x.border[1] == y.border[2] or x.border[2] == y.border[3] or x.border[3] == y.border[0]:
                        y.rotate(2) #Clockwise 
                    if x.border[0] == y.border[3] or x.border[1] == y.border[0] or x.border[2] == y.border[1] or x.border[3] == y.border[2]:
                        y.rotate(1) #AntiClockWise
                    x.pair(orientation,yNumber)

#assign borders
borderTiles["topLeft"] = None
borderTiles["bottomLeft"] = None
borderTiles["topRight"] = None
borderTiles["bottomRight"] = None
for tile in allTiles:
    if tile.pairs.count(None) == 2:
        print(tile.pairs,tile.tileNumber)
        if tile.up == None:
            if tile.left == None:
                borderTiles["topLeft"] = tile
            if tile.right == None:
                borderTiles["topRight"] = tile
        if tile.down == None:
            if tile.left == None:
                borderTiles["bottomLeft"] = tile
            elif tile.right == None:
                borderTiles["bottomRight"] = tile


firstTile = borderTiles["topLeft"]
while False:
    if nextTile.right != None:
        nextTile = allTilesDict[nextTile.right]
    elif nextTile.right == None and nextTile.right != borderTiles["bottomRight"].tileNumber:
        firstTile = allTilesDict[firstTile.down]
        nextTile = firstTile
    elif nextTile.right == borderTiles["bottomRight"].tileNumber:
        break

#Debug
for i in allTiles:
    print(i.pairs,i.tileNumber)

for key in allTilesDict:
    print(key)
    for i in allTilesDict[key].tiles:
        print(i)


