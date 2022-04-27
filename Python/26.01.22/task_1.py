#!/bin/python3
ml = list()
maxalpha = ""
temp = ""
sen = input("enter sentence")
if sen == "":
    print("please enter something")
for i in sen:
    if i  == " ":
        ml.append(temp)
        temp = ""
    else:
        temp += i
ml.append(temp)
if len(ml) == 1:
    print("sentence consists of one word")
n = 1
while n < len(ml):
    for i in range(len(ml)-n):
        if len(ml[i]) > len(ml[i+1]):
            maxalpha = ml[i]
            ml[i] = ml[i+1]
            ml[i+1] = maxalpha
    n+=1
print(ml)

