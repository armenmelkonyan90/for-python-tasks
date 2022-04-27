#!/bin/python3
count = 0 
num = input("enter number")
if num.isdigit():
    bin_num = bin(int(num))
    bin_num = bin_num[2:]
    for i in bin_num:
        if int(i) == 1:
            count += 1
    print(count, "ones in the binary number", num)
else:
    print("please enter the number")
