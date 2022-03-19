#function to flip tile
#e,se,sw,w,nw,ne
class Tile(object):
    def __init__(self,tileNumber):
        self.tileNumber = tileNumber
        self.surroundTiles = {"E":None,"SE":None,"SW":None,"W":None,"NW":None,"NE":None}
        self.side = True

with open("puzzleInput","r") as puzzle:
    line = puzzle.read()
    line = line[:-1]
    allInput = line.split("\n")

#Create the first Tile
allTilesDict = {}
tileNumber = 0
firstTile = Tile(tileNumber)
allTilesDict[tileNumber] = firstTile
allDirections = ["E","SE","SW","W","NW","NE"]
toBeProcessed = []
backwardsDirections = {"E":"W","W":"E","SE":"NW","NW":"SE","SW":"NE","NE":"SW"}
for layers in range(3):
    if layers == 0:
        for key in firstTile.surroundTiles:
            tileNumber += 1
            firstTile.surroundTiles[key] = Tile(tileNumber)
            allTilesDict[tileNumber] = firstTile.surroundTiles[key]
            toBeProcessed.append(tileNumber)
            secondKey = backwardsDirections[key] #For pairing back the way it came from
            firstTile.surroundTiles[key].surroundTiles[secondKey] = firstTile
        
        for i,key in enumerate(firstTile.surroundTiles):
            #pair with left and right
            if i == 5:
                indexToAdd = 1
            else:
                indexToAdd = i + 1 + 1
            if key == "NE" or key == "NW":
                if key == "NE":
                    indexToAdd2 = 1
                else:
                    indexToAdd2 = 0
            else:
                indexToAdd2 = allDirections.index(key) + 2
            
            tileToAdd = allTilesDict[indexToAdd]
            tileToPair = firstTile.surroundTiles[key]
            directionToPair = allDirections[indexToAdd2]
            tileToPair.surroundTiles[directionToPair] = tileToAdd
            tileToAdd.surroundTiles[backwardsDirections[directionToPair]] = tileToPair
        print(toBeProcessed)
        continue
    
    
    for tileNo in toBeProcessed[::-1]:
        tile = allTilesDict[tileNo]




#seperateLines
for line in allInput:
    try:
        firstLetter , secondLetter = line[0], line[1]
    except:
        firstLetter = line[0]

    if firstLetter == 'e' or 'w':
        pass
        line = line[1:]
    else:
        pass
        line = allInput[2:]

       
