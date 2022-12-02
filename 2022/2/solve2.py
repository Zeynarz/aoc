# A:1, B:2, C:3
# X:lose, Y:draw, Z:win

with open("input","r") as inp:
    rounds = inp.read().split("\n")
    rounds = rounds[:-1]

# rock is 1 point , paper is 2, scissors is 3
a = {"X": 3,"Y": 1,"Z": 2} 
b = {"X": 1,"Y": 2,"Z": 3} 
c = {"X": 2,"Y": 3,"Z": 1} 

xyz = {"X":0,"Y":3,"Z":6}

points = 0

for r in rounds:
    opponent = r[0]
    own = r[2]

    # points = ownChoicePoints + resultPoints
    if opponent == "A":
        points += a[own] + xyz[own] 

    elif opponent == "B":
        points += b[own] + xyz[own] 

    elif opponent == "C":
        points += c[own] + xyz[own] 

print(points)
