with open("input","r") as inp:
    instr = inp.read().split("\n")[:-1]

X = 1
V = 0
cycle = 0

waited = 0
instrIndex = 0
strengthSum = 0

while cycle < 220:
    cycle += 1

    if waited == 2:
        X += V
        waited = 0
        instrIndex += 1

    if waited == 0:
        if instr[instrIndex][0:4] == "noop":
            instrIndex += 1
        
        elif instr[instrIndex][0:4] == "addx":
            V = int(instr[instrIndex][5:])
            waited = 1 # tick  

    elif waited == 1:
        waited += 1


    if ((cycle - 20) % 40) == 0:
        signalStrength = X * cycle
        strengthSum += signalStrength

print(strengthSum)
