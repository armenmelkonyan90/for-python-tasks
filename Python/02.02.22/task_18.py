#!/bin/python3
nds = [2,44,34,5,-2,5,77,8,91,-4,15,23,8,-21,9]
first_index = 0
last_index = 0
print("defined list is\n",nds)
for i in range(len(nds)):
    if nds[i] < 0:
        first_index = i
        break
for i in range(len(nds)-1,-1,-1):
    if nds[i] < 0:
        if i == first_index:
            print("list contain only one negative element")
            break
        
        else:
             if nds[i] == nds[first_index]:
                 print("first and last negative elements in list is equal")
             else:
                 nds[i],nds[first_index] = nds[first_index],nds[i]
        break
print("changed list is \n",nds)

