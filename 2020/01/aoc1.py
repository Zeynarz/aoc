number = []
with open("listAoc") as numberList:
    number = numberList.readlines()
    
for index,i in enumerate(number):
    number[index] = i[:-1]

for x in number:
    for y in number:
        for z in number:
            x = int(x)
            y = int(y)
            z = int(z)
            if x + y + z == 2020:
                print(x*y*z)
