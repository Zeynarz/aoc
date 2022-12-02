with open("input","r") as data:
    calories = data.read().split("\n\n")
    for index,i in enumerate(calories):
        calories[index] = i.split()
        
highest = [0,0,0]
for i in calories:
    currentCalories = 0
    for j in i:
        currentCalories += int(j)

    for j in highest:
        if currentCalories > j:
            highest[highest.index(min(highest))] = currentCalories
            break

print(highest)
print(sum(highest))
