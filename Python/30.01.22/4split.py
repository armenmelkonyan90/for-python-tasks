#!/bin/python3
def my_split(mstr, sym):
    ml = []
    temp = ""
    for i in mstr:
        if i  == sym:
            ml.append(temp)
            temp = ""
        else:
            temp += i
    ml.append(temp)
    return ml
print(my_split("london is a capital of great britain", " "))
