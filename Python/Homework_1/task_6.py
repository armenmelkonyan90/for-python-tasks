#!/usr/bin/python3
sen = input("enter sentence: ").split()
if sen == "":
    print("you didn't enter sentence")
else:
      for i in sen:
          print(i[::-1], end = " ")
print()
     
