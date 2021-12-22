# Reference Diagram:

# -----------
#      | 
#      |
#   \  O  /  
#      |
#     / \    

# -----------
#      |     
#      |
#      O       
#     /|\    
#     / \      



def printH(n):
    if(n == 9):
        print("                         -----------")
    if(n == 8):
        printH(9)
        print("                              |     ")
    if(n == 7):
        printH(8)
        print("                              |     ")
    if(n == 6):
        printH(7)
        print("                              O     ")
    if(n == 5):
        printH(7)
        print("                           \  O     ")
    if(n == 4):
        printH(7)
        print("                           \  O  /  ") 
    if(n == 3):
        printH(4)
        print("                              |     ")
    if(n == 2):
        printH(3)
        print("                             /      ")       
    if(n == 1):
        printH(3)
        print("                             / \    ")
    if(n == 0):
        printH(6)
        print("                             /|\    ")
        print("                             / \    ")