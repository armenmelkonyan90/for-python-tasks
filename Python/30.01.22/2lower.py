#!/bin/python3
def my_lowwer(mstr):
    nmstr = ""
    for i in mstr:
        if i.isupper():
            nmstr += i.lower()
        else:
            nmstr += i
    return nmstr
print(my_lowwer("London Is a CaPital of grEat brItain"))
