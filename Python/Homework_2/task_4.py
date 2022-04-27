#!/bin/python3
sentence = input("enter the sentence: ")
if sentence == "":
    print("please enter the sentence: ")
sym = input("enter the symbol: ")
if sym == "" or len(sym) > 1:
    print("please enter (the/one) symbol")
for i in range(len(sentence)):
    if sentence[i] != sym:
        print(sentence[i], end = "")
    else:
        print()
print()
