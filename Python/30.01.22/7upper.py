#!/bin/python3
def my_upper(mstr):
    nmstr = ""
    for i in mstr:
        if i.islower():
            nmstr += i.upper()
        else:
            nmstr += i
    return nmstr
print(my_upper("loNDon Is a CapItal of graet BrItain"))
