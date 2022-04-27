#!/usr/bin/python3
def word(mstr):
    ml = mstr.split()
    ml.sort(key=len, reverse = True)
    return ml[0]
def main():
    mstr = input("enter string: ")
    print(word(mstr))
if __name__ == "__main__":
    main()             
