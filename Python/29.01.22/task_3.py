#!/bin/python3
print("if you want to exit the programm enter '/' ")
while True:
    num = input("enter the number: ")
    if num == "/":
        break
    if num.isdigit():
        if int(num) % 3 == 0 and int(num) % 2 == 0:
            print("entered number is devisible by both three and two.")
        else:
            print("the entered number is not divisible by three and two.")
    else:
        print("you are entered the symbol, please enter the number")             

