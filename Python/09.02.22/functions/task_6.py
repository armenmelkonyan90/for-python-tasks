#!/usr/bin/python3
def upper(mstr):
    nmstr = ""
    for i in range(len(mstr)):
        if mstr[i] == " " or mstr[i] == '/.,?><;":\|][}{=-)(*&^%$#@!~`' or mstr[i].isdigit():
           nmstr += mstr[i]
        else:
            if ord(mstr[i]) in range(97,122):
                nmstr += mstr[i]
            else:
                nmstr +=chr(ord(mstr[i])+32)
    return nmstr
def main():
    mstr = input("enter string: ")
    print(upper(mstr))
if __name__ == "__main__":
    main()     
