#!/bin/python3
alpha_dict = {}
for i in range(65,91):
    alpha_dict[chr(i)] = i
    alpha_dict[chr(i+32)] = i+32
print(alpha_dict) 

