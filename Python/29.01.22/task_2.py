#!/bin/python3
print("if you want to exit the programm enter '/' ")
while True:
    num = input("enter the number: ")
    if num == "/":
        break
    if num.isdigit():
        if int(num) % 3 == 0:
            print("entered number is devisible by three.")
        else:
            print("entered number is not devisible by three.")
    else:
        print("you are entered the symbol, please enter the number")                                                                 
