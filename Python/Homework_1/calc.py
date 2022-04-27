#!/bin/python3
while True:
    action = input("enter action:\n ").split()
    if action[0] == "c":
        break
    if len(action) == 0 or len(action) == 1 or len(action) == 2: 
        print("enter correct action")
        continue 
       
          # if action[0] in 'a-z'
       # print("enter correct action")
       # continue
    num1 = int(action[0])
    sym = action[1]
    num2 = int(action[2])
    value = 0
    if sym == "+":
        value = num1 + num2
        print("result: ",value)
    elif sym == "-":
        value = num1 - num2
        print("result: ",value)
    elif sym == "*":
        value = num1 * num2
        print("result: ",value)
    elif sym == "/":
        value = num1 / num2
        print("result: ",value)
    elif sym == "%":
        value = num1 % num2
        print("result: ",value)
    elif sym =="**":
        value = num1 ** num2
        print("result: ",value)
    else:
        print("I'm not so smart yet )))")
