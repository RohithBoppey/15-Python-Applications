import random

def Win(a, b):
    if(a == "Rock" and b == "Scissors"):
        return a
    elif(a == "Scissors" and b == "Rock"):
        return b
    elif(a == "Paper" and b == "Scissors"):
        return b
    elif(a == "Scissors" and b == "Paper"):
        return a
    elif(a == "Rock" and b == "Paper"):
        return b
    elif(a == "Paper" and b == "Rock"):
        return a

ch = ['Rock', 'Paper', 'Scissors']

u_score = 0
c_score = 0

while(1):
    u = input("Your choice is: ")
    c = random.choice(ch)
    print("Computer chose",c)
    if(Win(u,c) == u):
        print("Player Wins")
        u_score+=1
    elif(Win(u,c) == c):
        print("Computer Wins")
        c_score+=1
    else:
        print("Its a draw!")
    replay =  input("Y to play again and N to quit: ")
    if(replay == 'Y' or replay == 'y'):
        pass
    else:
        break
print("Computer Score: ",c_score, "     Player Score: ",u_score)
