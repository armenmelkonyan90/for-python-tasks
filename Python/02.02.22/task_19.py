#!/bin/python3
nds = [2,4,5,6,7,43,8,9,43,2,12,23,43,11,]
maxel = 0
count = 0
for i in nds:
    if i > maxel:
        maxel = i
for i in nds:
    if i == maxel:
        count += 1
print("the bigest element in list is repaeted ",count," times")

