#!/usr/bin/python3
sen = input("enter sentence: ")
value = 1
mul = ""
if sen == "":
    print("You didn't enter sentence")
else: 
    for i in sen:
         if sen.count(i) >= value:
            value = sen.count(i)
            mul = i
    print("Most used letter is: ", mul)
