with open("input","r") as inputFile:
    allOcto = inputFile.read().split("\n")
    allOcto.pop()

    for index,row in enumerate(allOcto):
        rowArr = []
        for char in row:
            rowArr.append(int(char))

        allOcto[index] = rowArr



def advanceStep():
    flashes = 0
    for row in allOcto:
        for index2,num in enumerate(row):
            row[index2] = num + 1

    flashList = toFlash()
    while len(flashList) != 0:
        for index1,index2 in flashList:
            flash(index1,index2)

        flashList = toFlash()

    for row in allOcto:
        for index2,num in enumerate(row):
            if num == "X":
                row[index2] = 0
                flashes += 1
    
    return flashes

def toFlash():
    flashList = []

    for index1,row in enumerate(allOcto):
        for index2,num in enumerate(row):
            if num != "X":
                if num > 9:
                    flashList.append((index1,index2))

    return flashList
            
           
def flash(index1,index2):
    indicesToChg = []

    # X means that has flashed before
    allOcto[index1][index2] = "X"


    # FIXME 
    # there is prob a better way to do this part
    if index1 != 0:
        indicesToChg.append((index1-1,index2)) # up
        if index2 != 0:
            indicesToChg.append((index1-1,index2-1)) # top left

        if index2 != (len(allOcto[0])-1):
            indicesToChg.append((index1-1,index2+1)) # top right

    if index1 != (len(allOcto)-1):
        indicesToChg.append((index1+1,index2)) # down
        if index2 != 0:
            indicesToChg.append((index1+1,index2-1)) # bottom left
        
        if index2 != (len(allOcto[0])-1):
            indicesToChg.append((index1+1,index2+1)) # bottom right

    if index2 != 0:
        indicesToChg.append((index1,index2-1)) # left

    if index2 != (len(allOcto[0])-1):
        indicesToChg.append((index1,index2+1)) # right
    
    for index1,index2 in indicesToChg:
        val = allOcto[index1][index2]
        if val != "X":
            allOcto[index1][index2] = val + 1  


i = 0
while True:
    i += 1
    if advanceStep() == 100:
        print(i)
        break

