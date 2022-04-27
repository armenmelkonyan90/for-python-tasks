#!/bin/python3
print("if you want to exit the programm enter '/' ")
while True:
    num = input("enter the number: ")
    if num == "/":
        break
    if num.isdigit():
        for i in range(2, int(num)):
            if int(num) % i == 0:
                print("entered number is not prime.")
                break
        else:
            print("entered number is prime")
    else:
         print("you are entered the symbol, please enter the number")


