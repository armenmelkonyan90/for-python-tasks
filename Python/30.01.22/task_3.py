#!/bin/python3
import random
import math
count = 0
ran_num = random.randint(1,100)
print("I thinking of a number from 1 to 100.\nCan you guess it? ")
while True:
    if count == 5:
        print("You lose. the number is", ran_num)
        break
    num = input("enter number ")
    if num.isalpha() or num in '/.,?><\|][}{=-+_)(*&^%$#@!`~':
        print("enter only number")
        continue
    if int(num) == ran_num:
        print("WOW!!! YOU GUESSED IT!!")
        break
    else:
        if abs(ran_num - int(num)) > 50:
            print("too cold")
        elif abs(ran_num - int(num)) <50 and abs(ran_num - int(num)) >20:
            print("cold")
        elif abs(ran_num - int(num)) < 20 and abs(ran_num - int(num)) > 5:
            print("hot")
        else:
            print("too hot")
    count+=1
            

