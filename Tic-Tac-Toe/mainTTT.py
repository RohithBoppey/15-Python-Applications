from printFunction import printTable as pT
import random
from checkWin import win as WWW

l = [" ", " ", " "," ", " ", " "," ", " ", " "]


list_index = []

for i in range(1,10):
    list_index.append(i)

dup_list_index = list_index.copy()

print("The positions possible in the tic-tac-toe is: ")
pT(list_index)
chances = 9
flag = 0
win = 1

while(chances >= 0 and (win != "X" or win != "O")):
    flag = 0
    loc = int(input("The location you want to insert X is: "))
    if(loc not in dup_list_index):
        print("Wrong input or Wrong Location or Used Location Entered")
        flag = 1
    else:
        l[loc-1] = "X"
        dup_list_index.remove(loc)
        pT(l)
        chances-=1
        win = WWW(l)
        if(win != 0 and win != 1 and win != " "):
            print(win, "wins the game!")
            break
    #computer
    if(flag == 0 and chances >= 1):
        c_loc = random.choice(dup_list_index)
        print("Computer has chose to keep O at position", c_loc)
        l[c_loc-1] = "O"
        dup_list_index.remove(c_loc)
        pT(l)
        chances-=1
        win = WWW(l)
        if(win != 0 and win != 1 and win != " "):
            print(win, "wins the game!")
            break
    if(" " not in l):
        print("It's a draw!")
        break

    

