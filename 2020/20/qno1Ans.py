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
            self.down = tileNumber
        elif orientation == 1:
            self.right = tileNumber
        elif orientation == 2:
            self.up = tileNumber
        elif orientation == 3:
            self.left = tileNumber
        self.pairs = [self.up,self.right,self.down,self.left]

allTiles = []
allTilesDict = {}
with open("tiles","r") as tilesFile:
    allTilesStrings = tilesFile.read()
    allTilesList = allTilesStrings.split("\n\n")

allTilesList[-1] = allTilesList[-1][:-1]
for tile in allTilesList:
    tileNumber = tile[5:9]
    tileObject = Tile(tile,tileNumber)
    allTiles.append(tileObject)
    allTilesDict[tileNumber] = tile

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
                    x.pair(orientation,yNumber)

#Print out positions
for tile in allTiles:
    if tile.pairs.count(None) == 2:
        print(tile.tileNumber)
