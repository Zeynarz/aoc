with open("input","r") as inp:
    pairs = inp.read().split("\n\n")

# not gonna use "eval", cause its dangerous
def parse(string):
    index = 0
    toAdd = ""
    current = []

    while index < len(string):
        char = string[index]
        if char == "[":
            endBracket = findEnd(string,index)
            toAdd = parse(string[index+1:endBracket])
            index = endBracket + 1

        elif char == ",":
            if type(toAdd) == str:
                # int
                toAdd = int(toAdd)

            current.append(toAdd)
            toAdd = ""
            index += 1

        else:
            # char is an int
            toAdd += char
            index += 1

    # Add last char
    if toAdd != "":
        if type(toAdd) == str:
            toAdd = int(toAdd)

        current.append(toAdd)

    return current
           
def findEnd(string,start):
    nesting = 0
    for index,char in enumerate(string[start+1:]):
        if char == "[":
            nesting += 1
        elif char == "]":
            nesting -= 1

        if nesting == -1:
            return index+start+1


# python3 can actually compare stuff like
# [1,[2,[3,[4,[5,6,7]]]],8,9] < [1,[2,[3,[4,[5,6,0]]]],8,9
# but Im gonna try implementing it myself

def compare(left,right):
    for index,leftItem in enumerate(left):
        try:
            rightItem = right[index]
        except IndexError:
            # out of bounds
            return False

        if type(leftItem) == int == type(rightItem):
            if leftItem < rightItem:
                return True
            elif leftItem > rightItem:
                return False


        elif type(leftItem) == list or type(rightItem) == list:
            if type(leftItem) == int:
                leftItem = [leftItem] 

            elif type(rightItem) == int:
                rightItem = [rightItem]

            result = compare(leftItem,rightItem)

            if result == None:
                continue
            else: 
                return result

    if len(left) < len(right):
        # after checking everything,left side ran out first
        return True

    # returning None means further checking/comparison needs to be made
    return None


indexSum = 0
for index,pair in enumerate(pairs):
    pairList = pair.split("\n")
    left,right = parse(pairList[0][1:-1]),parse(pairList[1][1:-1])

    if compare(left,right) == True:
        indexSum += (index+1)

print(indexSum)
