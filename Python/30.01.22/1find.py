#!/bin/python3
def my_find(mstr, sym):
    pas = ""
    for i in range(len(mstr)):
        if mstr[i] == sym:
            pas = i
    return pas
print(my_find("london is a capital of great britain","c"))
