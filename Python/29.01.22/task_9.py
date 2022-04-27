#!/bin/python3
sum = 0
num1 = input("enter the first name")
num2 = input("enter the second number")
if num1.isdigit() and num2.isdigit():
    sum = int(num1) + int(num2)
    if sum < 1000:
        print("Sum of numbers is", sum)
    else:
        print("Multiply of numbers is", int(num1)*int(num2))

else:
    print("please enter only numbers")
