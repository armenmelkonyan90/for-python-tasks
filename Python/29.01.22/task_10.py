#!/bin/python3
import random
import sys
ran_num = random.randint(1,100)
print("I thinking of a number from 1 to 100.\nCan you guess it? ")
while True:
    num = input("enter number ")
    if num.isalpha() or num in '/.,?><\|][}{=-+_)(*&^%$#@!`~':
        print("enter only number")
        continue
    if int(num) == ran_num:
        print("WOW!!! YOU GUESSED IT!!")
        break
    else:
        if int(num) < ran_num:
            if ran_num - int(num) <= 10:
                print("very hot, add a little")
                continue
            if ran_num - int(num) > 10 and ran_num - int(num) <= 40:
                print("heat, add more")
                continue
            else:
                print("cold, try a bigger number")
                continue
        if int(num) > ran_num:
            if int(num) - ran_num <= 10:
                print("very hot, turn it down a bit")
                continue
            if int(num) - ran_num > 10 and int(num) - ran_num <= 40:
                print("heat, turn down more")
                continue
            else:
                print("cold, try a smaller number")
                continue
