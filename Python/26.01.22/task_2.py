#!/bin/python3
mstr = input("enter the sentence: ")
if mstr == "":
    print("enter something: ")
word = input("enter the word to be replaced: ")
if word == "":
    print("you did not enter the word: ")
if word not in mstr:
    print("There is no such word in the sentence. ")
new_word = input("what word should be replaced? ")
ml = list()
temp = ""
for i in mstr:
    if i  == " ":
        ml.append(temp)
        temp = ""
    else:
        temp += i
ml.append(temp)
for i in range(len(ml)):
    if ml[i] == word:
         ml[i] = new_word
print(ml)
