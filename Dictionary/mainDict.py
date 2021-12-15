# Read from json and print list from that

# importing difflib to get the closest match

import json
from difflib import get_close_matches

def Fancyprint(l):
    for i in range(0,len(l)):
        print(i + 1, l[i])


dictionary = json.load(open("data.json"))
word = input("The word you want to search is: ")
word = word.lower()
word = (get_close_matches(word, dictionary, n = 1, cutoff = 0.5))[0]
print("Word Found: ", word, "\n\n")

if word in dictionary:
    print("Meaning found")
    Fancyprint(dictionary[word])
elif word.upper() in dictionary:
    print("Meaning found")
    Fancyprint(dictionary[word.upper()])
elif word.title() in dictionary:
    print("Meaning found")
    Fancyprint(dictionary[word.title()])
else:
    print("Meaning not found")