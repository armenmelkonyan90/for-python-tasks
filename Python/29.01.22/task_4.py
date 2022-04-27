#!/bin/python3
print("if you want to exit the programm enter '/' ")
while True:
    num1 = input("enter the first number: ")
    if num1 == "/":
        break
    if num1.isalpha() or num1 in '/><~`\|{}[])(@#$%^&*_- +=' or num1 == "":
        print("enter only numbers please")
        break
    num2 = input("enter the second number: ")
    if num2 == "/":
        break
    if num2.isalpha() or num2 in '/><~`\|{}[])(@#$%^&*_- +=' or num2 == "":
        print("enter only numbers please")
        break
    num3 = input("enter the third number: ")
    if num2 == "/":
        break
    if num3.isalpha() or num3 in '/><~`\|{}[])(@#$%^&*_- +=' or num3 == "":
        print("enter only numbers please")
        break
    if num1 >= num2 and num1 >= num3:
        print("the bigest number is ", num1)
    if num2 >= num1 and num2 >= num3:
        print("the bigest number is ", num2)
    if num3 >= num1 and num3 >= num2:
        print("the bigest number is ", num3)

