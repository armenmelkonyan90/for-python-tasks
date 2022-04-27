#!/bin/python3

sentence = input("enter the sentence: ")
if sentence == "":
    print("you did not enter sentance")
num = input("enter number:  ")
if not num.isdigit() or num == "":
    print("you did not enter number")
if (len(sentence) < int(num)):
    print("enter a smaller number")
k = int(num)*(-1)
print(sentence[:k])



