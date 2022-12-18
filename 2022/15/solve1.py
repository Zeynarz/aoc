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


cantBeBeacon = []
y = 2000000
for sensorPos,beaconPos,closestD in posNDis:
    sensorX,sensorY = sensorPos
    if abs(sensorY - y) <= closestD:
        leftMost = sensorX - (closestD - abs(sensorY-y))
        rightMost = sensorX + (closestD - abs(sensorY-y))

        cantBeBeacon.append((leftMost,rightMost))

# merge to avoid overlaps
cantBeBeacon.sort(key=lambda kv: kv[0])

# pretty proud of this own merging idea/algorithm lol
i = 0
while True:
    if (i+1) >= len(cantBeBeacon):
        # ady in final element, nothing more to merge
        break

    mergedStartX,mergedEndX = cantBeBeacon[i]
    nextStartX,nextEndX = cantBeBeacon[i+1]

    if nextStartX <= mergedEndX:
        # mergeable
        if nextEndX < mergedEndX:
            # does not need to merge since alr contain it
            cantBeBeacon.pop(i+1)
            continue

        cantBeBeacon[i] = mergedStartX,nextEndX
        cantBeBeacon.pop(i+1)

    else: 
        # alr not mergeable
        i += 1


n = 0
for x1,x2 in cantBeBeacon:
    n += (x2-x1) + 1

# remove all beacon in row y
removed = []
for sensorPos,beaconPos,closestD in posNDis:
    beaconX,beaconY = beaconPos
    if beaconY == y and beaconPos not in removed:
        removed.append((beaconX,beaconY))
        n -= 1

print(n)
