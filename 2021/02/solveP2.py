commands = []
horizontal = 0
depth = 0
aim = 0

curCommand = ""
val = 0

with open("input","r") as inputFile:
    commands = inputFile.read().split("\n")
    
commands.pop() # Remove last element that is an empty string

for i in commands:
    val = int(i[-1])
    curCommand = i[:-2]

    if curCommand == "forward":
        horizontal += val
        depth += aim * val

    elif curCommand == "down":
        aim += val

    elif curCommand == "up":
        aim -= val

print(horizontal * depth)


