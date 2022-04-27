#!/bin/python3
print("if you want to exit the programm enter '/' ")
while True:    
    num = input("enter the number: ")
    if num == "/":
        break
    if num.isdigit():
        if int(num) % 2 == 0:
            print("entered number is even.")
        else:
            print("entered number is odd.")
    else:
        print("you are entered the symbol, please enter the number")

