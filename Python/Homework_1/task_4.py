#!/usr/bin/python3
sen = input("enter sentence: ")
sum=0
if sen == "":
    print("you didn't enter sentence")
else:
    for i in sen:
        if i.isdigit():
            sum += 1
    print("this sentence has ", sum,  " numbers")

