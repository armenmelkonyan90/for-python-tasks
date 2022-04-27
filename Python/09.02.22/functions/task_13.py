#!/usr/bin/python3
def get_letters(mstr, num):
    ml = []
    ml.append(mstr[num])
    ml.append(mstr[len(mstr)-num-1])
    return ml
def main():
    mstr = input("enter the sentence ")
    num = int(input("enter ten number "))
    print(get_letters(mstr, num))
if __name__ == "__main__":
    main() 
