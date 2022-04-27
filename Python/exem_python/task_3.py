#!/usr/bin/python3
def mstr(mstr):
    ml=mstr.split()
    max_word=""
    count=1
    for el in ml:
        if len(el) > count:
            count = len(ml)
            max_word = el
    return max_word

print(mstr("hello my dear frienddddddd"))
