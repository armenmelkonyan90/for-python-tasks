#!/usr/bin/python3
sen = input("enter sentence: ")
maxvalue = 1
minvalue = 1
mul = ""
lul = ""
new_sen = ""
if sen == "":
    print("You didn't enter sentence")
else:
    for i in sen:
         if sen.count(i) >= maxvalue:
            maxvalue = sen.count(i)
            mul = i
   
         if sen.count(i) <= minvalue:
            minvalue = sen.count(i)
            lul = i
    for i in sen:
        if i == mul:
            new_sen += lul 
         
        elif i == lul:
             new_sen += mul
         
        else:
             new_sen += i
    print(new_sen)                             
