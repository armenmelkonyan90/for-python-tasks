#!/usr/bin/python3
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
minnum = num1
maxnum = num2
if num1 > num2:
    maxnum = num1
    minnum = num2
for i in range(minnum, maxnum):
    if i % 15 == 0:
         print(i, " is fizzBuzz")
         continue
    elif i % 5 == 0:
        print(i, " is Buzz")
    elif i % 3 == 0:
        print(i, " is Fizz")


