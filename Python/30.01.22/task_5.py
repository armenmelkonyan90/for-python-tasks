#!/bin/python3
num_string = ""
even_nums = ""
odd_nums = ""
print("enter numbers")
while True:
    num = input("")
    if num == "c":
        break
    if num.isdigit() and num not in even_nums and num not in odd_nums:
        if int(num) % 2 == 0:
            even_nums += num + " "   
        else:

            odd_nums += num + " "
elist = list(even_nums.split())
olist = list(odd_nums.split())
n = 1
while n < len(elist):
    for i in range(len(elist) - n):
        if int(elist[i]) > int(elist[i+1]):
            maxval = elist[i]
            elist[i] = elist[i+1]
            elist[i+1] = maxval
    n+=1
n = 1
while n < len(olist):
    for i in range(len(olist) - n):
        if int(olist[i]) > int(olist[i+1]):
            olist[i],olist[i+1] = olist[i+1],olist[i]
    n+=1
if len(elist) >= len(olist):
    for i in range(len(olist)):
        num_string += elist[i] + " " + olist[i] + " "
    for i in range(len(olist), len(elist)):
        num_string += elist[i] + " "
            
else:
    for i in range(len(elist)):
        num_string += elist[i] + " " + olist[i] + " "
    for i in range(len(elist), len(olist)):
        num_string += olist[i] + " "
print(num_string)
