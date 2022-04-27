#!/usr/bin/python3
def lines_count(mstr):
    ml=[]
    ml=mstr.split()
    return len(ml)
def main():
    mstr = input("enter list ")
    print(lines_count(mstr))
if __name__ == "__main__":
    main()


