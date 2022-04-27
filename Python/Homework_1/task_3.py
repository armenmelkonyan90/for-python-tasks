#!/usr/bin/python3
sen = input("enter sentence: ")
if sen == "":
    print("you didn't enter sentence")
else:
    for i in sen:
       print(i.swapcase(), end="")
    print()

