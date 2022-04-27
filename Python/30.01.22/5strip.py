#!/bin/python3
def my_strip(mstr):
    startindex = 0
    endindex = 0
    for i in range(len(mstr)):
        if mstr[i].isalpha():
            startindex = i
            break
    for i in range(len(mstr)-1, -1, -1):
        if mstr[i].isalpha():
            endindex = i
            break
    newmstr = mstr[startindex:endindex+1]
    return newmstr
print(my_strip("    london is a capital of great britain     "))
