#!/bin/python3
def my_join(mstr, sym):
    nmstr = ""
    for i in mstr:
        if i == " ":
            nmstr += sym
        else:
            nmstr += i
    return nmstr
print(my_join("london is a capital of great britain","-"))
