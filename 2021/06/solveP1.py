allFish = []

with open("input","r") as inputFile:
    allFish = inputFile.read().split(",")

allFish[-1] = allFish[-1][:-1]

def passOneDay():
    fishToAdd = 0
    for index,timer in enumerate(allFish):
        if timer == "0":
            allFish[index] = "6"
            fishToAdd += 1
        
        else:
            allFish[index] = str(int(timer) - 1)
    
    for i in range(fishToAdd):
        allFish.append(8)


            
for i in range(80):
    print("Day " + str(i))
    passOneDay()

print(len(allFish))

