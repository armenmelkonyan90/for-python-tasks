#!/usr/bin/python3
def ren(mstr, num1, num2):
    nmstr = ""
    for i in range(num1, num2):
        nmstr += mstr[i]
    return nmstr
def main():
    mstr = input("enter string: ")
    num1 = int(input("enter first number "))
    num2 = int(input("enter second number "))
    print(ren(mstr, num1, num2))
if __name__ == "__main__":
    main()     
