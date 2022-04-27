#!/usr/bin/python3

def find_pol(num):
    cnt=0
    while True:
        num1=str(int(num)+cnt)
        num2=str(int(num)-cnt)
        if num1 == num1[::-1]:
            if num2 == num2[::-1]:
                return num1, num2
                break
            else:
                return num1
        if num2 == num2[::-1]:
            return  num2

        
        cnt+=1

def main():
    num = input("enter the number")
    print(find_pol(num))
if __name__ == "__main__":
    main()




