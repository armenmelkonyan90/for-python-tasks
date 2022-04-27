#!/bin/python3
num = input("enter the number: ")
if num.isdigit():
    for i in range(2, int(num)):
        if int(num) % i == 0:
            print("NO")
            break
    else:
        print("YES")

else:
    print("you are entered the symbol, please enter the number")
