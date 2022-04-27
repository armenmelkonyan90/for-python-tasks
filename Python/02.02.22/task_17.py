#!/bin/python3
nds = [2,44,34,5,-2,5,77,8,91,-4,15,23,-8,21,9]
smval = min(nds)
lel = nds[len(nds)-1]
n = 0
print("defined list is ",nds)
print("last element is ",nds[len(nds)-1])
for i in range(len(nds)):
    if nds[i] == smval:
        n = i
        nds[i],nds[len(nds)-1] = nds[len(nds)-1],nds[i]
        break
print("smalest element is ",smval)
print("changed list is ",nds)
 
