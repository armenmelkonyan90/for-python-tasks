#!/bin/python3
def my_zfill(mstr, width):
    nmstr = ""
    if int(width) > len(mstr):
        for i in range(len(mstr),width):
            nmstr += "0"
        nmstr += mstr
        return nmstr
    else:
        return mstr
print(my_zfill("london is a capital of great britain",50))

