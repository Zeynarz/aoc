# A:1, B:2, C:3
# X:A, Y:B, Z:C

with open("input","r") as inp:
    rounds = inp.read().split("\n")
    rounds = rounds[:-1]

a = {"X":3,"Y":6,"Z":0}
b = {"X":0,"Y":3,"Z":6}
c = {"X":6,"Y":0,"Z":3}

xyz = {"X":1,"Y":2,"Z":3}

points = 0

for r in rounds:
    opponent = r[0]
    own = r[2]

    if opponent == "A":
        points += a[own] + xyz[own] 

    elif opponent == "B":
        points += b[own] + xyz[own] 

    elif opponent == "C":
        points += c[own] + xyz[own] 

print(points)
