#!/bin/python3
seq = input("enter the sequence of real numbers")
new_seq = ""
max_count = 0
val = ""
print(seq)
for i in seq:
    if i.isdigit():
        new_seq += i
print(new_seq)
for i in new_seq:
    for j in new_seq:
        if i == j:
            max_count = j
            val = j
print("more common number: ",val)


