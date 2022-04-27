#!/bin/python3
while True:
    sym = input("please enter number or letter. if you want to exit the script enter '/'")
    if sym == "/":
        break
    elif sym.isalnum():
      if sym.isdigit():
             sym = int(sym)
             print(chr(sym))
      else:
             print(ord(sym))
    else:
         print("incorrect input")


