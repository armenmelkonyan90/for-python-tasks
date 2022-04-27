#!/bin/python3
a = []
b = []
c = []
n = input("enter n: ")
for i in range(int(n)):
    a.append(i*2)
m = input("enter m: ")
for i in range(int(m)):
    b.append(i*3)
for i in range(len(a)):
    c.append(a[i])
for i in range(len(b)):
    c.append(b[i])
k = 1
while k<len(c):
    for i in range(len(c) - k):
        if c[i] > c[i+1]:
            c[i],c[i+1] = c[i+1],c[i]
    k += 1

print(c)
    

