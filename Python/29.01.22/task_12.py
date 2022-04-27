#!/bin/python3
ml = [2, 4 ,5, 11, 8, 9, 45, 22, 34, 12]
print("my list is:\n", ml)
nml = []
for i in range(len(ml)):
    nml.append(int(ml[i])**2)
print("my new list is:\n", nml)
