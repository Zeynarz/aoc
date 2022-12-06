with open("input","r") as inp:
    signal = inp.read()[:-1]

currentMarker = []
for index,char in enumerate(signal):
    if char in currentMarker:
        dupCharIndex = currentMarker.index(char)
        currentMarker = currentMarker[dupCharIndex+1:]

    currentMarker.append(char)

    # if len(currentMarker) == 4:  for part 1
    if len(currentMarker) == 14:
        print(index+1)
        break

