import sys

# Bingo boards are going to be stored this way
# [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],[another board]]
# Numbers that are drawn has an X behind it, so if 1 is drawn [1X,2,3,4,5]

with open("input","r") as inputFile:
    numbers = inputFile.readline().split(",")

    # Get rid of the \n char at the last element of numbers
    numbers[-1] = numbers[-1][:-1]
    inputFile.readline() # Get rid of line 2

    bingoBoards = inputFile.read().split("\n\n")
    for index,board in enumerate(bingoBoards):
        bingoBoards[index] = board.split("\n") 
        
        for index2,row in enumerate(bingoBoards[index]):
            bingoBoards[index][index2] = row.split()

    # Get rid of an empty row that is in the last board
    bingoBoards[-1].pop()
            

def drawNumber(num):
    for board in bingoBoards:
        for row in board:
            for index,n in enumerate(row):
                if n == num:
                    row[index] = num + "X"


# TODO: Is there a better way to check if a board has won?

def checkBoardWin(board):
    # (0,0) = bottom left number, (5,5) = top right number
    # True = win False = no win

    for row in board:
        for num in row:
            if "X" not in num:
                break 
            
            if num == row[-1]:
                return True
    
    for columnNum in range(5):
        for row in board:
            if "X" not in row[columnNum]:
                break

            if row == board[-1]:
                return True

    return False


# Starting from the 5th move, check if someone won everytime after a move
for index,num in enumerate(numbers):
    drawNumber(num)

    if index >= 4:
        for board in bingoBoards:
            if checkBoardWin(board):
                # Find the sum of all unmarked numbers
                ans = 0
                for row in board:
                    for n in row:
                        if "X" not in n:
                            ans += int(n)
                
                ans *= int(num)
                print(ans)
                sys.exit()


