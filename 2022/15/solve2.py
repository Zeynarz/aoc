with open("input","r") as inp:
    positions = inp.read().split("\n")[:-1]

posNDis= []
for pos in positions:
    posList = pos.split(": ")
    sensor,beacon = posList[0][10:],posList[1][21:]
    sensor,beacon = sensor.split(", "),beacon.split(", ")
    x1,y1 = int(sensor[0][2:]),int(sensor[1][2:])
    x2,y2 = int(beacon[0][2:]),int(beacon[1][2:])
    
    d = abs(y2-y1) + abs(x2-x1)

    posNDis.append(((x1,y1),(x2,y2),d))


def findNoDistressRange(y):
    # ps: even if a beacon is in the range of cantBeDistress, its not a distress beacon
    cantBeDistress = []
    
    for sensorPos,beaconPos,closestD in posNDis:
        sensorX,sensorY = sensorPos
        if abs(sensorY - y) <= closestD:
            leftMost = sensorX - (closestD - abs(sensorY-y))
            rightMost = sensorX + (closestD - abs(sensorY-y))
    
            cantBeDistress.append((leftMost,rightMost))
    
    # merge to avoid overlaps
    cantBeDistress.sort(key=lambda kv: kv[0])
    
    i = 0
    while True:
        if (i+1) >= len(cantBeDistress):
            break
    
        mergedStartX,mergedEndX = cantBeDistress[i]
        nextStartX,nextEndX = cantBeDistress[i+1]
    
        if nextStartX <= mergedEndX:
            if nextEndX < mergedEndX:
                cantBeDistress.pop(i+1)
                continue
    
            cantBeDistress[i] = mergedStartX,nextEndX
            cantBeDistress.pop(i+1)
    
        else: 
            i += 1

    return cantBeDistress


# find distress beacon
for i in range(4000000):
    noDistress = findNoDistressRange(i)
    if len(noDistress) > 1 and noDistress[0][1] < 4000000:
        # if a row doesnt have a distress beacon, noDistress is only gonna contain 1 range
        distressX = noDistress[0][1] + 1
        distressY = i
        frequency = distressX*4000000 + i
        print(distressX,distressY,frequency)
        break
    
