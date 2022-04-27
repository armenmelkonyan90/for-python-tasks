#!/bin/python3
num = input("enter the number: ")
#if num == "" or num.isalpha():
#    print("enter only number please")
if num == "0":
    print("incorrect input")
elif num == "1":
    print("1 : 0")
else:
    fib_d={1: 0, 2: 1 }
    for i in range(3, int(num)+1):
        fib_d[i] = fib_d[i-1] + fib_d[i-2]
    fib_s =str(fib_d)
    fib_s = fib_s.replace("{"," ")
    fib_s = fib_s.replace("}","")
    print(fib_s.replace(",","\n"))

