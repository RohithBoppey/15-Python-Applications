from printHangman import printH as hangmanPrint

import random
import json

def enterScore(chances):
    name = input("Enter your Name: ")
    file = open("score.txt", "a")
    StringToPrint = name+"-"+word+"-"+str(chances)+"\n"
    file.write(StringToPrint)

Dict = json.load(open("data.json"))
listofWords = []
for d in Dict:
    listofWords.append(d)
word = "********"
while(len(word) >= 8):
    word = listofWords[random.randrange(0, len(listofWords))]

word = word.lower()
print(word)
printWord = "_"*len(word)
print("The length of the word is: ",len(word))

userword = ""
chances = 10
while(userword != word and chances > 0 and printWord != word):
    print("                 You have", chances, "chances left")
    userword = input("Word: ")
    if(len(userword) > len(word)):
        print("Given length of the word should be less than ", len(word))
        break
    if(userword == word or userword == printWord):
        print("Hurray! You have found the word!")
        print("Your Score is: ", chances)
        break
    else:
        userwordList = list(userword)
        wordList = list(word)
        for i in userwordList:
            for j in wordList:
                if(i == j):
                    ind = wordList.index(i)
                    printWordList = list(printWord)
                    printWordList[ind] = i
                    printWord = ("").join(printWordList)
        chances-=1
    print(printWord)
    hangmanPrint(chances)
    
    if(chances == 0):
        print("OOPS! You ran out of choices!")
        print("The word is: ", word)

        print("\n\nBetter Luck Next Time!")

if(word == userword or word == printWord):
        log = input("Do you want to store the score? Y or N: ")
        if(log == 'y' or log == 'Y'):
            enterScore(chances)

    