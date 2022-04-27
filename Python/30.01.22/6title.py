#!/bin/python3
def my_title(mstr):
    title_mstr = ""
    nmstr = ""
    nmstr = mstr.split()
    for i in range(len(nmstr)):
        title_mstr += nmstr[i].capitalize() + " "
    return title_mstr
print(my_title("lonDon iS a caPItal of grEat brItain"))

