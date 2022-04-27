#!/bin/python3
import sys
fstr = input("enter fisrt list")
if len(fstr) == 0:
    print("enter something")
    exit()
sstr = input("enter second list")
if len(sstr) == 0:
    print("enter something")
    exit()
if len(fstr) < len(sstr):
    fstr,sstr = sstr,fstr
flist = list(fstr.split())
slist = list(sstr.split())
print(flist)
print(slist)
sum_list = list()
for i in range(len(slist), len(flist)):
    if flist[i].isdigit():
        slist.append(0)
    else:
        slist.append("")
for i in range(len(flist)):
    if flist[i].isdigit() and slist[i].isdigit():
        sum_list.append(int(flist[i]) + int(slist[i]))
    else:
        sum_list.append(flist[i] + slist[i])
print("summary list is", sum_list)
