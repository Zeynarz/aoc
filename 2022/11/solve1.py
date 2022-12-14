with open("input","r") as inp:
    notes = inp.read().split("\n\n")

class Monkey:
    def __init__(self,startingItems,operation,test):
        self.items = startingItems
        self.operation = operation
        self.activity = 0

        # test is expressed in the form
        # [divisible by what num,if true throw to which monkey, if false ...]
        self.test = test

    def inspectItems(self):
        global monkeys

        for item in self.items:
            worryLevel = item
            operator,value = self.operation[0],self.operation[2:]
            
            if value == "old":
                value = item


            if operator == "+":
                worryLevel += int(value)
            elif operator == "*":
                worryLevel *= int(value)

            worryLevel //= 3

            if (worryLevel % self.test[0]) == 0:
                monkeys[self.test[1]].items.append(worryLevel)

            else:
                monkeys[self.test[2]].items.append(worryLevel)


            self.activity += 1

        self.items = []


monkeys = []
for monkeyNote in notes:
    traits = monkeyNote.split("\n")
    startingItems = traits[1][18:].split(", ")
    startingItems = list(map(int,startingItems))
    operation = traits[2][23:]
    test = [traits[3][21:],traits[4][29:],traits[5][30:]]
    test = list(map(int,test))

    monkeys.append(Monkey(startingItems,operation,test))

for i in range(20):
    for monkey in monkeys:
        monkey.inspectItems()

twoMostActive = [0,0]

for monkey in monkeys:
    lowerActivity = min(twoMostActive)
    if monkey.activity > lowerActivity:
        twoMostActive[twoMostActive.index(lowerActivity)] = monkey.activity

print(twoMostActive)
print(twoMostActive[0] * twoMostActive[1])
