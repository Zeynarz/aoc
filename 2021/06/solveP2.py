# I only wrote this after seeing the solution https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/hnftdfg/?context=3
# So thanks a lot to this guy

days = [0] * 9

with open("input","r") as inputFile:
    startingFish = inputFile.read().split(",")
    startingFish[-1] = startingFish[-1][:-1]

    for fish in startingFish:
        days[int(fish)] += 1

def nextDay():
    dup = days.copy()
    toBreed = days.pop(0)
    days[6] += toBreed
    days.append(toBreed)

for i in range(256):
    nextDay()

print(sum(days))
