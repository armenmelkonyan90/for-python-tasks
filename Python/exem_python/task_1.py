#!/usr/bin/python3

def lower(mstr):
    newmstr=""
    for i in mstr:
        if i.isalpha():
            if 65 < ord(i)< 92:
                newmstr+=chr(ord(i)+32)
            else:
                newmstr+=i
        else:
            newmstr+=i
    return newmstr


print(lower("hIjas H gfRmkjs 1`122 ASAJKSls"))

