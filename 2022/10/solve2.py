with open("input","r") as inp:
    instr = inp.read().split("\n")[:-1]

X = 1
V = 0
cycle = 0

waited = 0
instrIndex = 0
strengthSum = 0

while cycle < 240:
    # cpu
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

    # crt
    spritePos = [X-1,X,X+1]
    # convert cycle into drawing which currentPos of row
    currentPos = (cycle - 1) % 40 

    if currentPos in spritePos:
        print("#",end="")
    else:
        print(".",end="")

    if (cycle % 40) == 0:
        print()


