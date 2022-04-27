#!/usr/bin/python3
sen = input("enter sentence: ").split()
maxword = ""
if sen == "":
    print("you didn't enter sentence")
else:
    for i in sen:
        if len(i) > len(maxword):
            maxword = i
    print("longest word in a sentence: ", maxword)

