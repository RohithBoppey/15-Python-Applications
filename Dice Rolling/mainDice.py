import printDice
import random

c = 'y'
while(c != 'Y' or c != 'y'):
    number = random.randint(1, 6)
    printDice.printingDice(number)
    print("Press Y to roll the dice again and N to end-> ", end = "")
    c = input()
    if(c == 'Y' or c == 'y'):
        pass
    else:
        break