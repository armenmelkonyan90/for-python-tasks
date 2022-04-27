#!/usr/bin/python3
counter = 0 
while True:
    num = input("enter number: ")
    if num.lower() == "c":
        break
    elif num.isdigit():
        if int(num) % 2 == 0:
            counter += 1
    else:
        print("you didn't enter number")
        
    print("you entered", counter, " even numbers")


