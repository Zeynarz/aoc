#subject number is always 7 ._.
cardPublic = 9717666
#cardPublic = 5764801
doorPublic = 20089533
#doorPublic = 17807724
cardLoopSize = 0 
doorLoopSize = 0 
#Used to find out LoopSize 
value = 1
i = 1
while True:
    value *= 7
    value %= 20201227
    if value == cardPublic:
        cardLoopSize = i
    if value == doorPublic:
        doorLoopSize = i

    if cardLoopSize != 0 and doorLoopSize != 0:
        break
    i += 1

print(cardLoopSize,doorLoopSize)

#encryption of door subjectNumber using card loop size
cardEncryption = 1
for loop in range(cardLoopSize):
    cardEncryption *= doorPublic
    cardEncryption %= 20201227

#encryption of card subjectNumber using door loop size
doorEncryption = 1
for loop in range(doorLoopSize):
    doorEncryption *= cardPublic
    doorEncryption %= 20201227

print(cardEncryption,doorEncryption)
